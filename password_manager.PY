from operator import truediv
import random
import os.path

all_keys = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*(),.?;:\|+-=_/<>'

# Creates the keys for the encryption
def create_key():
    key1 = random.randrange(0, 172)
    key2 = random.randrange(0,172)
    fileExists = os.path.exists("key.txt")
    if fileExists == False:
        with open("key.txt", 'a') as key_file:
            key_file.write(str(key1) + "\n")
            key_file.write(str(key2) + "\n")
    else:
        pass

# Stores keys into variables to be used in both encryption and dencrytion
def load_key(x):
    file = open("key.txt", 'r')
    content = file.readlines()
    key = content[x]
    file.close()
    return int(key)

# Manual encryption for the master password
def encrypt(password):
    encryption = ''
    for i in password:
        position = all_keys.find(i)
        newposition = (position + master_key) % 86
        encryption += all_keys[newposition]
    return encryption

def encrypt2(password):
    encryption = ''
    for i in password:
        position = all_keys.find(i)
        newposition = (position + secondary_key) % 86
        encryption += all_keys[newposition]
    return encryption

def dencrypt(password):
    dencryption = ''
    for i in password:
        position = all_keys.find(i)
        newposition = (position - secondary_key - master_key) % 86
        dencryption += all_keys[newposition]
    # print("Decrypted pass" + dencryption)
    return dencryption

def dencrypt2(password):
    dencryption = ''
    for i in password:
        position = all_keys.find(i)
        newposition = (position - master_key) % 86
        dencryption += all_keys[newposition]
    # print("Decrypted pass" + dencryption)
    return str(dencryption)


# Check if Master Password is correct
def isMasterCorrect(password):
    with open("key.txt", 'r') as file:
        content = file.readlines()
        if encrypted_master == content[3]:
            # print("True")
            return True
        else:
            # print("False")
            return False

# Modules for modes in password manager
def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            account, pwd = data.split(" | ")
            print("_________________________________________\n" + "Account Name: " + account + "\nPassword: " + dencrypt2(pwd))

def add():
    AccName = input("Account Name: ")
    password = input("Password: ")
    with open('passwords.txt', 'a') as f:
        f.write(AccName + " | " + encrypt(password) + "\n")

def delete():
    deletedWord = input("Enter the account you want to delete: ")
    with open("passwords.txt", 'r') as original:
        with open("temp.txt", 'w') as copy:
            for line in original:
                if not line.strip("\n").startswith(deletedWord):
                    copy.write(line)
    os.replace("temp.txt", "passwords.txt")

def password_Generator():
    password_Length = int(input("Enter the size of the password you would like: "))
    password = ''
    for x in range(0,password_Length):
        password_Characters = random.choice(all_keys)
        password = password + password_Characters
    
    print("This is your new password: " + password + "\nEnter this password in the Password Manager.")

# Main
create_key()

master_key = load_key(0)
secondary_key = load_key(1)

# Have the user input the master password
master = (input("Enter the master password (First time entering creates the master password): "))

encrypted_master = encrypt2(encrypt(master))

# Check if there is master password
masterExists = False
with open("key.txt", 'r') as file:
    masterExists = any("Master" in x for x in file)

if masterExists == False:
    with open('key.txt', 'a') as file:
        file.write("Master\n" + encrypted_master)
else:
    pass

# Performs password check
password_Check = isMasterCorrect(encrypted_master)
while password_Check == False:
    master = (input("Password incorrect. Please try again.\nEnter the master password: "))
    encrypted_master = encrypt2(encrypt(master))
    password_Check = isMasterCorrect(encrypted_master)
print("Welcome to Password Manager.")
    
# Takes user input to determine which mode to enter
while True:
    mode = input("Choose your mode (view, add, delete, password generator, quit): ")

    if mode == "quit":
        print("Thank you for using the Password Manager.")
        break

    elif mode == "view":
        view()

    elif mode == "add":
        add()
    
    elif mode == "delete":
        delete()

    elif mode == "password generator":
        password_Generator()

    else:
        print("Mode invalid. Please try again.")