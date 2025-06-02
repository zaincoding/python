import random

print("Welcome to password generator.")

char='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-[]|;:,.?~`0123456789'

number = input("Amount of password you want to generate: ")
number = int(number)

length = input("Enter you password length: ")
length = int(length)

print('\nhere are your password.')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(char)

    print(passwords)