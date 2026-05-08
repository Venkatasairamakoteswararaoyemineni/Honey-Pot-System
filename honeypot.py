import socket
import sqlite3
from datetime import datetime
import os

HOST = "0.0.0.0"
PORT = 9999

DB_PATH = "database/attacks.db"

os.makedirs("database", exist_ok=True)

# -------------------------
# DATABASE SETUP
# -------------------------

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS attacks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ip TEXT,
    username TEXT,
    password TEXT,
    timestamp TEXT
)
""")

conn.commit()
conn.close()

# -------------------------
# SAVE ATTACK
# -------------------------

def save_attack(ip, username, password):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO attacks(ip, username, password, timestamp)
    VALUES (?, ?, ?, ?)
    """, (
        ip,
        username,
        password,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()

# -------------------------
# START SERVER
# -------------------------

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))

server.listen(5)

print(f"[+] Honeypot running on port {PORT}")

while True:

    client, address = server.accept()

    ip = address[0]

    print(f"[!] Connection from {ip}")

    client.send(b"Fake SSH Server\n")
    client.send(b"Username: ")

    username = client.recv(1024).decode().strip()

    client.send(b"Password: ")

    password = client.recv(1024).decode().strip()

    save_attack(ip, username, password)

    client.send(b"Access Denied\n")

    print(f"[LOGGED] {ip} | {username} | {password}")

    client.close()