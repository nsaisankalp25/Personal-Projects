import random
print("Welcome to Number Guessing Game - Python")
low = int(input("Enter a small number: "))
high = int(input("Enter a big number: "))
while True:
    r_num = random.randint(low, high)
    num = int(input("Guess the number: "))
    if num != r_num:
        print('Woops, try again, Number ReGenerated')
    else:
        print('nice!')
        break