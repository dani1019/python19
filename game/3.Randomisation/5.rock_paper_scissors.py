import rock_paper_scissors_picture as pic
import random

#question to user selected rock or paper, scissors 
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

#make the list rps_picture
game_image = [pic.rock, pic.paper, pic.scissors]

#length of rps_picture list
num_items = len(game_image)

#print user's rps selected
if user_choice >= 3 or user_choice < 0:
  print("You typed an invalid number, you lose!")
else:
    print(f"user_choice: {user_choice}")
    print(game_image[user_choice])

    #select randomly index of rps_items to computer choose
    computer_choice = random.randint(0, num_items - 1)
    print("computer choose:")
    #print computer's rps selected randomly
    print(f"computer_choice: {computer_choice}")
    print(game_image[computer_choice])

    #check whether if which win
    if user_choice > computer_choice:
        if user_choice == 2 and computer_choice == 0:
            print("You lose.")
        else:
            print("You win")
    elif computer_choice > user_choice:
        if user_choice == 0 and computer_choice == 2:
            print("You win.")
        else:
            print("You lose.")
    elif user_choice == computer_choice:
        print("It's draw.")
