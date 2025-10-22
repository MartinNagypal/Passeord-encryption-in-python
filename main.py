import sqlite3
from argon2 import PasswordHasher
from datetime import datetime

ph = PasswordHasher()

#user inputs for showcase
print("\nlogin/register: ")
mode = input()
print("\nEnter username: ")
username = input()
print("\nEnter password: ")
password = input()

#create sqlite DB
conn = sqlite3.connect("user.db")
cursor = conn.cursor()
cursor.execute(""" 
CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY, 
        username TEXT UNIQUE,
        passwordHashe TEXT,
        createdAt TEXT
               )
""") #id as primary key, UNIQUE so no double usernames

conn.commit()

def createUser(username:str, password:str):
    passwordHash = ph.hash(password) #hash password
    print("\n" + passwordHash) #print for showcase
    cursor.execute("SELECT username FROM user WHERE username = ?", (username,)) #check if user already exists
    row = cursor.fetchone()
    if row:
        return "User already exists" #if yes stop here
    else:
        try:
            cursor.execute("INSERT INTO user (username, passwordHash, createdAt) VALUES (?,?,?)", (username, passwordHash, datetime.now().isoformat(),))
            conn.commit() #if not insert username, hashed pw and creation date in DB as new user
            return "User created"
        except Exception as e:
            return e
    
def verifyUser(username:str, password:str): #verify login
    cursor.execute("SELECT passwordHash FROM user WHERE username = ?", (username,)) #check if user exists
    row = cursor.fetchone()
    if not row:
        return f'No account with username: {username}' #if not stop here
    hash = row[0] #get hashed password
    try:
        ph.verify(hash, password) #verifiy if provided password matches hashed password in DB
        return "Sucsessfully logged in"
    
    except Exception as e:
        return e #return that password doesnt match

#select login or register
if(mode == "register"):
    print(createUser(username, password))
elif(mode == "login"):
    print(verifyUser(username, password))
else:
    pass
