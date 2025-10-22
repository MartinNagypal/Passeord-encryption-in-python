import sqlite3
from argon2 import PasswordHasher
from datetime import datetime

ph = PasswordHasher()

print("\nlogin/register: ")
mode = input()
print("\nEnter username: ")
username = input()
print("\nEnter password: ")
password = input()

conn = sqlite3.connect("user.db")
cursor = conn.cursor()
cursor.execute(""" 
CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE,
        passwordHashe TEXT,
        createdAt TEXT
               )
""")

conn.commit()

def createUser(username:str, password:str):
    passwordHash = ph.hash(password)
    print("\n" + passwordHash)
    cursor.execute("SELECT username FROM user WHERE username = ?", (username,))
    row = cursor.fetchone()
    if row:
        return "User already exists"
    else:
        try:
            cursor.execute("INSERT INTO user (username, passwordHash, createdAt) VALUES (?,?,?)", (username, passwordHash, datetime.now().isoformat(),))
            conn.commit()
            return "User created"
        except Exception as e:
            return e
    
def verifyUser(username:str, password:str):
    cursor.execute("SELECT passwordHash FROM user WHERE username = ?", (username,))
    row = cursor.fetchone()
    if not row:
        return f'No account with username: {username}'
    hash = row[0]
    try:
        if(ph.verify(hash, password) == True):
            return "Sucsessfully logged in"
        else:
            return "Wrong password or username"
    except Exception as e:
        return e


if(mode == "register"):
    print(createUser(username, password))
elif(mode == "login"):
    print(verifyUser(username, password))
else:
    pass
