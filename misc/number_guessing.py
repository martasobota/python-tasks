''' Write simple number-guessing game. Computer has to draw number in range
from 1 to 100 and:
1. Ask user about the number
2. Aheck if input is number, if not, show proper information and go back to point 1 
3. If number will be too low, high, show information about it
4. If user guessed, show information and close the programme'''

from random import randint

guess = randint(1, 100)
guessed = False

while not guessed:
    try:
        question = int(input("Zgadnij liczbę: "))
    except ValueError:
        print("To nie jest liczba")
        continue
    
