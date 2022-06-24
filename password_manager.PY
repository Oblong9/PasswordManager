import random
import os.path
# LINKS TO STUFF TO USE
# https://www.educative.io/answers/how-to-generate-a-random-string-in-python
# https://www.youtube.com/watch?v=FMnW4D4r_E4 
# https://www.youtube.com/watch?v=DLn3jOsNRVE&t=5262s

all_keys = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*(),.?;:\|+-=_/<>'

# Creates the keys for the encryption
def create_key():
    key1 = random.randrange(0, 172)
    key2 = random.randrange(0,172)
    fileExists = os.path.exists("key.txt")
    if fileExists == False:
        with open("key.txt", 'a') as key_file:
            key_file.write(str(key1) + "\n")
            key_file.write(str(key2))
    else:
        pass

create_key()

# Stores keys into variables to be used in both encryption and dencrytion
def load_key(x):
    file = open("key.txt", 'r')
    content = file.readlines()
    key = content[x]
    file.close()
    return int(key)

master_key = load_key(0)
secondary_key = load_key(1)

print(master_key)
print(secondary_key)

# Manual encryption for the master password
def encrypt(password):
    encryption = ''
    for i in password:
        position = all_keys.find(i)
        newposition = (position + master_key) % 86
        encryption += all_keys[newposition]
    print(encryption)
    return encryption

def encrypt2(password):
    encryption = ''
    for i in password:
        position = all_keys.find(i)
        newposition = (position + secondary_key) % 86
        encryption += all_keys[newposition]
    print(encryption)
    return encryption


def dencrypt(password):
    dencryption = ''
    for i in password:
        position = all_keys.find(i)
        newposition = (position - secondary_key - master_key) % 86
        dencryption += all_keys[newposition]
    print(dencryption)

# Have the user input the master password
master = (input("Enter the master password (First time entering creates the master password): "))

encrypted_password = encrypt2(encrypt(master))
dencrypt(encrypted_password)

# Modules for modes in password manager
def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            account, pwd = data.split("|")
            print("_________________________________________\n" + "Account Name: " + account + "\nPassword:" + pwd)

def add():
    AccName = input("Account Name: ")
    password = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(AccName + " | " + password + "\n")

def delete():
    pass

# Takes user input to determine which mode to enter
while True:
    mode = input("Choose your mode (view, add, delete, quit): ")

    if mode == "quit":
        print("Thank you for using the Password Manager.")
        break

    elif mode == "view":
        view()

    elif mode == "add":
        add()
    
    elif mode == "delete":
        delete()

    else:
        print("Mode invalid. Please try again.")