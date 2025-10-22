from argon2 import PasswordHasher
import bcrypt
 
salt=bcrypt.gensalt() #generate salt
ph = PasswordHasher() #create ph object

password ="mySecurePassword" #plain password

passwordSalted = str(salt) + password #password combined with salt

hashedPw = ph.hash(passwordSalted) # hash the password
hashedPw2 = ph.hash(passwordSalted) # hash again

print(f'\nfirst hash: {hashedPw} \nSecond hash: {hashedPw2} \n ')

if(hashedPw == hashedPw2): # since every hash is different even if the same password is hashed twice, it will return false
    print("\nsame pw")
else:
    print("false\n")

print(f'{ph.verify(hashedPw, passwordSalted)} \n') #ph.verify can decrypt the password to verify
