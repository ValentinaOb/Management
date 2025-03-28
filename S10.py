import socket
import json
import threading
from Crypto.Random import random
import mysql.connector
import os
from datetime import datetime

db = mysql.connector.connect(
    host="localhost",
    user="root", 
    password="12345",
    database="practice"
)
cursor = db.cursor()

def verify_user(user_id, password):
    cursor.execute("SELECT passwords, access_level FROM sec_pswd_users WHERE user_id = %s;", (user_id,))
    row = cursor.fetchone()
    if row:
        password_list = json.loads(row[0])
        access_level = row[1]
        return password in password_list, access_level
    return password in password_list, None

def check_access(user_id, file_name, access_level):

    cursor.execute("SELECT access_level FROM sec_pswd_users WHERE user_id = %s;", (user_id,))
    row = cursor.fetchone()
    access_level = int(row[0])
    #print('Check: ',access_level)

    cursor.execute("SELECT access_level FROM sec_user_files WHERE file_name = %s;", (file_name,))
    row = cursor.fetchone()
    doc_access_level = int(row[0])
    #print('Doc Check: ',doc_access_level)
    
    with open(f"token_{user_id}.json", "r") as f:
        tok_pswd_ident = json.load(f)

    passwords = tok_pswd_ident["passwords"]
    password = random.choice(passwords)
    pswd,access_level = verify_user(user_id, password)
    if access_level ==doc_access_level:
        return True
        
    return False

def server_run():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("localhost", 5001))
    server.listen(5)
    server.settimeout(30)
    print("Server Run")

    try:
        while True:
            try:
                client, addr = server.accept()
                data = client.recv(1024).decode()
                user_data = json.loads(data)

                user_id = user_data.get("user_id")
                access_level = user_data.get("access_level")
                file_name = user_data.get("file_name")

                if check_access(user_id, file_name, access_level):
                    client.send(f"Access_level {access_level} allowed on {file_name}".encode())
                else:
                    client.send(f"Access Denied for access_level {access_level}".encode())

                client.close()
            except socket.timeout:
                print("TimeOut")
    except KeyboardInterrupt:
        print("\nServer Stop")
        server.close()

def register_user(user_id, access_level):

    passwords = [str(random.getrandbits(64)) for i in range(5)]
    
    cursor.execute("INSERT INTO sec_pswd_users (user_id, passwords, access_level) VALUES (%s, %s, %s);",
                   (user_id, json.dumps(passwords), access_level))
    db.commit()
    
    with open(f"token_{user_id}.json", "w") as f:
        json.dump({"user_id": user_id, "passwords": passwords}, f)

    #
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    f = open("logbook.txt", "a")
    f.write(f"\nUser '{user_id}' registered with access_level {access_level}   :   {current_time}")
    f.close()
    #

    print(f"User '{user_id}' registered with access_level '{access_level}'")

def create_file(user_id, file_name):
    cursor.execute("SELECT access_level FROM sec_pswd_users WHERE user_id = %s;", (user_id,))
    row = cursor.fetchone()
    access_level = int(row[0])
    #print('A: ',access_level)

    cursor.execute("INSERT INTO sec_user_files (file_name, access_level) VALUES (%s, %s);", (file_name, access_level))
    db.commit()
    f = open("secret.txt", "w")
    f.write("This secret!")
    f.close()

    #
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    f = open("logbook.txt", "a")
    f.write(f"\n{user_id}: File '{file_name}' created with {access_level}   :   {current_time}")
    f.close()
    #

    print(f"\nFile '{file_name}' created with {access_level}")

def read_file(user_id,file_name):
    cursor.execute("SELECT access_level FROM sec_pswd_users WHERE user_id = %s;", (user_id,))
    row = cursor.fetchone()
    access_level = int(row[0])
    #print('R: ',access_level)

    if check_access(user_id, file_name, access_level):
        with open(file_name, "r", encoding="utf-8") as f:
            content = f.read()
        return content
    else:
        return "Access Denied"

def edit_file(user_id, file_name, text):
    cursor.execute("SELECT access_level FROM sec_pswd_users WHERE user_id = %s;", (user_id,))
    row = cursor.fetchone()
    access_level = int(row[0])
    #print('Edit: ',access_level)

    if check_access(user_id, file_name, "edit"):
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(text)
        return "File updated"
    else:
        return "Access Denied"

def delete_file(user_id, file_name):
    cursor.execute("SELECT access_level FROM sec_pswd_users WHERE user_id = %s;", (user_id,))
    row = cursor.fetchone()
    access_level = int(row[0])
    #print('Delete: ',access_level)

    if check_access(user_id, file_name, "delete"):
        os.remove(file_name)
        return "File deleted"
    else:
        return "Access Denied"


server_thread = threading.Thread(target=server_run, daemon=True)
server_thread.start()

cursor.execute("DELETE FROM sec_user_files;")
cursor.execute("DELETE FROM sec_pswd_users;")
db.commit()

f = open("logbook.txt", "w")

register_user('admin_user', 4)
register_user('one_user', 3)
register_user('two_user', 2)
register_user('three_user', 1)

register_user('zero_user', 3)

#
create_file('one_user', 'logbook.txt')
#
create_file('one_user', 'secret.txt')

f = open("logbook.txt", "a")

user_id='two_user'
file_name='secret.txt'
res = read_file(user_id, file_name)
print('\nRes two_user - read_file: ',res)


current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
f.write(f"\n{user_id}: Read file '{file_name}' - {res}   :   {current_time}")


user_id='admin_user'
res=edit_file(user_id, file_name,'New data')
print('\nRes admin_user - edit_file: ',res)

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
f.write(f"\n{user_id}: Edit file '{file_name}' - {res}   :   {current_time}")


user_id='admin_user'
res=edit_file(user_id, file_name,'New data')
print('\nRes one_user - edit_file: ',res)

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
f.write(f"\n{user_id}: Edit file '{file_name}' - {res}   :   {current_time}")

user_id='three_user'
res=delete_file(user_id, file_name)
print('\nRes three_user - delete_file: ',res)

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
f.write(f"\n{user_id}: Delete file '{file_name}' - {res}   :   {current_time}")

user_id='zero_user'
res=delete_file(user_id, file_name)
print('\nRes zero_user - delete_file: ',res)
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
f.write(f"\n{user_id}: Delete file '{file_name}' - {res}   :   {current_time}")


f.close()