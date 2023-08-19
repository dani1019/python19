import os

#print the "Welcome to the secret auction program"
print("Welcome to the secret auction program")

bidder_list = {}
while True:
    #print "What is your name? "
    name = input("What is your name? ")

    #print "What's your bid? $"
    bid = int(input("What's your bid? $"))

    #Are there any other bidders? Type 'yes' or 'no'.
    exist_other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")

    #save the information of name and bid
    bidder_list[name] = bid

    print(bidder_list)

    #If yes remove entered all context and What is your Name?:
    if exist_other_bidders.lower() == 'yes':
        os.system('cls')
    #If No The winner is {name} with a bid of {bid}
    elif exist_other_bidders.lower() == 'no':
        winner = max(bidder_list, key=bidder_list.get)
        max_bid = max(bidder_list.values())

        print(f"The winner is {winner} with a bid of {max_bid}")
        break
    else:
        print("you must enter 'yes' or 'no'")