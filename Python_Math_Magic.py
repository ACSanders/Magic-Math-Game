# This is a simple math magic game that correctly guesses a user's number

import random

print('''
Hi! I'm going to read your mind and tell you what number you are thinking of.
Think of a number. But don't tell me what it is...
Do you have it?
''')
first_response = input("Type 'yes' if you have your number and are ready to start the game: ")

if first_response == "yes":
    print('''
    Great! Let's begin.
    ''')
    print('''
    First, take the number you first thought of and multiply it by 2
    ''')
    second_response = input("Got your new number? Type 'yes' if you are ready to proceed: ")
    if second_response == "yes":
        print('''
        Now, I want you to take a random number that I'll generate and add it to your new number.
        ''')
        number_even = (random.randint(0, 100)) * 2
        print('''
        OK. Add the following random number to your number:
        ''')
        print(number_even)

print('''
Once you are finished adding those numbers together, please divide your new number by 2
''')

third_response = input("Did you divide by 2? If so, please type 'yes' and we will proceed: ")

if third_response == "yes":
    print('''
    Great! Now I want you to take that number and subtract your ORIGINAL number from it.
    ''')

final_response = input("Type 'yes' once you have subtracted the original number you first thought of to get your new SECRET NUMBER: ")

if final_response == "yes":
    print('''
    Fantastic. Now I'm going to guess what your new secret number is!
    ''')
    secret_number = number_even / 2
    print('''
    Your secret number is...
    ''')
    print(secret_number)