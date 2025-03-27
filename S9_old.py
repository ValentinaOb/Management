import socket
import json
import threading
from Crypto.Random import random
import mysql.connector
import os

db = mysql.connector.connect(
    host="localhost",
    user="root", 
    password="12345",
    database="practice"
)
cursor = db.cursor()

ACCESS_CONTROL = {
    "admin": {"read": True, "edit": True, "delete": True},
    "owner": {"read": True, "edit": True, "delete": True},    
    "editor": {"read": True, "edit": True, "delete": False},
    "reader": {"read": True, "edit": False, "delete": False}    
}

def verify_user(user_id, password):
    cursor.execute("SELECT passwords, user_role FROM sec_pswd_users WHERE user_id = %s;", (user_id,))
    row = cursor.fetchone()
    if row:
        password_list = json.loads(row[0])
        user_role = row[1]
        return password in password_list, user_role
    return password in password_list, None

def check_access(user_id, file_name, action):
    cursor.execute("SELECT owner_name FROM sec_user_files WHERE file_name = %s;", (file_name,))
    row = cursor.fetchone()

    with open(f"token_{user_id}.json", "r") as f:
        tok_pswd_ident = json.load(f)

    passwords = tok_pswd_ident["passwords"]
    password = random.choice(passwords)
    
    if row:
        owner = row[0]
        pswd,role = verify_user(user_id, password)

        if user_id == owner:
            return True
        
        #print('A: ',ACCESS_CONTROL.get(role, {}).get(action, False))
        return ACCESS_CONTROL.get(role, {}).get(action, False)
    
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
                action = user_data.get("action")
                file_name = user_data.get("file_name")

                if check_access(user_id, file_name, action):
                    client.send(f"Action {action} allowed on {file_name}".encode())
                else:
                    client.send(f"Access denied for action {action}".encode())

                client.close()
            except socket.timeout:
                print("TimeOut")
    except KeyboardInterrupt:
        print("\nServer Stop")
        server.close()

def register_user(user_id, role):

    passwords = [str(random.getrandbits(64)) for i in range(5)]
    
    cursor.execute("INSERT INTO sec_pswd_users (user_id, passwords, user_role) VALUES (%s, %s, %s);",
                   (user_id, json.dumps(passwords), role))
    db.commit()
    
    with open(f"token_{user_id}.json", "w") as f:
        json.dump({"user_id": user_id, "passwords": passwords}, f)

    print(f"User '{user_id}' registered with role '{role}'")

def create_file(user_id, file_name):
    cursor.execute("INSERT INTO sec_user_files (file_name, owner_name) VALUES (%s, %s);", (file_name, user_id))
    db.commit()
    f = open("secret.txt", "w")
    f.write("This secret!")
    f.close()

    print(f"File '{file_name}' created by {user_id}")

def read_file(user_id,file_name):
    if check_access(user_id, file_name, "read"):
        with open(file_name, "r", encoding="utf-8") as f:
            content = f.read()
        return content
    else:
        return "Access Denied"

def edit_file(user_id, file_name, text):
    if check_access(user_id, file_name, "edit"):
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(text)
        return "File updated"
    else:
        return "Access Denied"

def delete_file(user_id, file_name):
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

register_user('owner_user', 'owner')
register_user('admin_user', 'admin')
register_user('editor_user', 'editor')
register_user('reader_user', 'reader')

create_file('owner_user', 'secret.txt')

res = read_file('reader_user', 'secret.txt')
print('\nRes reader_user - read_file: ',res)

res=edit_file('reader_user', 'secret.txt','New data')
print('\nRes reader_user - edit_file: ',res)

res=edit_file('editor_user', 'secret.txt','New data')
print('\nRes editor_user - edit_file: ',res)

res=delete_file('editor_user', 'secret.txt')
print('\nRes editor_user - delete_file: ',res)

res=delete_file('owner_user', 'secret.txt')
print('\nRes owner_user - delete_file: ',res)