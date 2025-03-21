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

def verify_user(user_id, password):
    cursor.execute("SELECT passwords FROM sec_pswd_users WHERE user_id = %s;", (user_id,))
    row = cursor.fetchone()
    if row:
        password_list = json.loads(row[0])
        return password in password_list
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

                if verify_user(user_data["user_id"], user_data["password"]):
                    client.send("Authentication Successful".encode())
                else:
                    client.send("Authentication Failed".encode())

                client.close()
            except socket.timeout:
                print("TimeOut")
    except KeyboardInterrupt:
        print("\nServer Stop")
        server.close()

def register_user(user_id):
    cursor.execute("DELETE FROM sec_pswd_users;")
    passwords = [str(random.getrandbits(64)) for _ in range(5)]
    
    cursor.execute("INSERT INTO sec_pswd_users (user_id, passwords) VALUES (%s, %s);", (user_id, json.dumps(passwords)))
    db.commit()
    
    with open("token.json", "w") as f:
        json.dump({"user_id": user_id, "passwords": passwords}, f)

    print(f"User '{user_id}' registrated")


def authenticate():
    if not os.path.exists("token.json"):
        print("token.json not found")
        return

    with open("token.json", "r") as f:
        tok_pswd_ident = json.load(f)

    user_id = tok_pswd_ident["user_id"]
    passwords = tok_pswd_ident["passwords"]
    password = random.choice(passwords)
    print('Password: ',password)

    data = json.dumps({"user_id": user_id, "password": password})

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 5001))
    client.send(data.encode())

    response = client.recv(1024).decode()
    print(f"Server Response: {response}")
    client.close()


server_thread = threading.Thread(target=server_run, daemon=True)
server_thread.start()

register_user("new_user")
authenticate()
