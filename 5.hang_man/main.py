import picture as pic
import words as wd
import method as md
import random

#start the hang_man
print(pic.hang_man)

#select randomly answer
answer = random.choice(wd.words).lower()
print(answer)

#guess the answer and enter the letter
letter= input("Guess a letter: ").lower()

display_string = []

display_string = md.match_letter(display_string,answer,letter)
print(display_string)

#if alphabet include in words and display the letter

#if alphabet don't include in words 
#You guesed a {alphabet}, that's not in the word. You lose a life
#display the picture