import random
import string

print("Hello! I will make a password for you.")

length = int(input("How long should the password be? "))

characters = string.ascii_letters + string.digits

password = ""

for i in range(length):
    password += random.choice(characters)

print("Your password is:", password)