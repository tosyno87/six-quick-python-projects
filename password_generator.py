import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*?0123456789'

print('Welcome To Your Password Generator')
number = int(input("How many passwords would you like to generate? "))
length = int(input("Enter a password length? "))

print("\nHere are your passwords:")
for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)

print("Hello World, what is up?")