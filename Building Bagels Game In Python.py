#!/usr/bin/env python
# coding: utf-8

# # bagels.py

# In[1]:


import random
print("Bagels, a deductive logic game.",flush=True)
print("By RAJ GAURAV (2241007011)",flush=True)
print("I am thinking of a 3-digit number. Try to guess what it is.\
\nHere are some clues:\
\nWhen I say:\t That means:\
\n  Pico\t\t One digit is correct but in the wrong position.\
\n  Fermi\t\t One digit is correct and in the right position.\
\n  Bagels\t No digit is correct.\
\nI have thought up a number.\
\n  You have 10 guesses to get it",flush=True)

def generate_secret_number():
    return ''.join(random.sample("0123456789",3))

def provide_hint(secret_number, guess):
    hint = ''
    for i in range(3):
        if guess[i] == secret_number[i]:
            hint += 'Fermi '
        elif guess[i] in secret_number:
            hint += 'Pico '
    if not hint:
        hint = 'Bagels'
    return hint.strip()

def play_game():
    secret_number = generate_secret_number()   
    attempts = 10
    while attempts > 0:
        guess = input(f"Guess #{11 - attempts}: ")
        while (len(guess) != 3):
            print("Please, Enter a valid 3-Digit number: ")
            guess = input(f"Guess #{11 - attempts}: ")
            
         
        hint = provide_hint(secret_number, guess)
        print(f"{hint}")
        if hint == "Fermi Fermi Fermi":
            print(f"You Got It!!")
            break
        
        attempts -= 1  
        if attempts == 0:
            print(f"Sorry! You ran out of Attempts! The Secret Number was {secret_number}")
def main():
    while True:
        play_game()
        play_again = input(f"Do you want to play again Type (Yes or No): ").lower()
        if play_again != "yes":
            print("Thanks For Playing!")
            break
main()

