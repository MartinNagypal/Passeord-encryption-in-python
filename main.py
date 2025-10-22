from argon2 import PasswordHasher

ph = PasswordHasher() #create ph object

print("\n enter username: ")
username = input()
print("\n enter password: ")
pw = input()

def hashPw(password):
    hashedPw = ph.hash(password) #encrypt with argon2 parameters
    return hashedPw

print(f'\n encrypted PW: \n{hashPw(pw)}')

print(f'\nlogin verify: {ph.verify(hashPw(pw), pw)}\n')