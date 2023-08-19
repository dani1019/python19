import picture as pic
import words as wd
import random

#start the hang_man
print(pic.hang_man)

#select randomly answer
answer = random.choice(wd.words).lower()

#convert display_string to list of letters
display_letter_list = list('-'* len(answer))
#convert answer to list of list of letters
answer_letter_list = list(answer)
death = 0

#picture list
pic = [pic.one, pic.two, pic.three, pic.four, pic.five]

while True:
    #guess the answer and enter the letter
    letter= input("Guess a letter: ").lower()

    #if letter exist answer, update display_string
    if letter in answer:
      for index, answer_letter in enumerate(list(answer)):
          if letter == answer_letter:
              display_letter_list[index] = letter
    #if letter not exist answer, life minus 1
    else:
        death += 1
        if death == 6:
            print("Game over")
            break
        else:
          print(pic[death - 1])

    #if display_string match answer, user win and exit game
    if "".join(display_letter_list) == "".join(answer_letter_list):
          print("You win.")
          break
    
    #print display_string
    print("".join(display_letter_list))