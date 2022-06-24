import random
import string

# Very rudimentary encryption algorithm
message = input("Enter message:")
allKeys = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*(),.?;:\|+-=_/<>'
numbers = '0123456789'
key = random.randrange(0, 172)
print("Key: " + str(key))
encryption = ''
dencryption = ''

# Encrypting the Key
# keysKey = random.randrange(0, 10)
# print("Key's Key: " + str(keysKey))
# keyEncrypt = ''
# keyDencrypt = ''

# for i in str(key):
#     position = numbers.find(i)
#     newposition = (position + keysKey) % 10
#     keyEncrypt += numbers[newposition]
# print(keyEncrypt)

# for i in str(key):
#     position = numbers.find(i)
#     newposition = (position - keysKey) % 10
#     keyDencrypt += numbers[newposition]
# print(keyDencrypt)

for i in message:
    position = allKeys.find(i)
    newposition = (position + key) % 86
    encryption += allKeys[newposition]
print(encryption)

for i in encryption:
    position = allKeys.find(i)
    newposition = (position - key) % 86
    dencryption += allKeys[newposition]
print(dencryption)