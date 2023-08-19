import os
stop_flag = False

def caculate_best_bidder(bidder_list, exist_other_bidder):
    #If yes remove entered all context and What is your Name?:
    if exist_other_bidder == 'yes':
        os.system('cls')
        stop_flag = False

    #If No The winner is {name} with a bid of {bid}
    elif exist_other_bidder == 'no':
        winner = max(bidder_list, key=bidder_list.get)
        max_bid = max(bidder_list.values())

        print(f"The winner is {winner} with a bid of {max_bid}")
        stop_flag =  True
    
    return stop_flag
