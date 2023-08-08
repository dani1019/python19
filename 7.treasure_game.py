#print the start message
print("""
      Welcome to Treasure lsland.
      Your mission is to find the treasure.        
      """)




direction = input("which direction do you go left or right? ").lower()

#question you will go left of right?
#if answer is left, print the next question
if direction == "left":
    #question you will go to swim or wait?
    doing = input("Do you go to swim or wait? ").lower()
    #if answer is wait print the next question
    if doing == "swim":
        door_color = input("Which door Red or Blue or Yellow?").lower()
        #question Which door Red or Blue or Yellow?
        #if answer is Red or Blue , print Game Over and quit game
        if (door_color == "red") or (door_color = "bule"):
            print("Game over.")
        #if answer is Yellow, print You Win!
        else:
            print("You win!")
    #if answer is swim, print Game Over and quit game
    else:
        print("Game over.")

#if answer is right, print Game Over and quit game
else:
    print("Game over.")

#TODO test code in 8/11








