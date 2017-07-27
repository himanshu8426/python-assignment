#coding=utf-8
"""
PROGRAM ---39---
Write a program able to play the "Guess the number"-game, where the number to be guessed is randomly chosen between 1 and 20. (Source: http://inventwithpython.com) This is how it should work when run in a terminal:

Hello! What is your name?
Torbjörn
Well, Torbjörn, I am thinking of a number between 1 and 20.
Take a guess.
10
Your guess is too low.
Take a guess.
15
Your guess is too low.
Take a guess.
18
Good job, Torbjörn! You guessed my number in 3 guesses!
"""
import random
def guess_the_number():
    print "Hello what's Your name"
    name = raw_input()
    x = random.randint(1,20)
    print "well, ",name,", I am thinking of a number between 1 to 20.\n""Take a Guess."
    time = 1
    while True:
            try:
                guess = int(raw_input())
                if guess > x:
                    print "Your guess is too high" 
                elif guess < x:
                    print "Your guess is too low"
                else:
                    break
                time += 1
            except ValueError:
                    print "Enter a integer value."
    print "Good job, ",name," You guessed my number in ",time," guesses."
guess_the_number()
