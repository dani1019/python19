import os
import process as ps

#print the "Welcome to the secret auction program"
print("Welcome to the secret auction program")

bidder_list = {}

#flag whether if game stop 
stop_flag = False

while not stop_flag:
    #print "What is your name? "
    name = input("What is your name? ").strip()

    #print "What's your bid? $"
    bid = input ("What's your bid? $").strip()

    #check if entered name or bid
    if len(name) == 0 or len(bid) == 0:
        print("please enter the information")
        break

    #Are there any other bidders? Type 'yes' or 'no'.
    exist_other_bidder = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()

    #save the information of name and bid
    bidder_list[name] = int(bid)
    
    #caculate the best bidder
    stop_flag = ps.caculate_best_bidder(bidder_list,exist_other_bidder)
    