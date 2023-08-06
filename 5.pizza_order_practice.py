#print Welcome to Python Pizza Deliveries!
print("Welcome to Python Pizza Deliveries!")

#What size pizza do you want? S, M or L
#small Pizza $15
#Medium Pizza $20
#Large Pizza $25

#make the variable to sum_price
sum_price = 0

size = input("What size pizza do you want? S, M or L ")

#change entered letter to upper case
size_upper_letter = size.upper()

if size_upper_letter == "S":
    sum_price += 15
elif size_upper_letter == "M":
    sum_price += 20
elif size_upper_letter == "L":
    sum_price += 25
else:
    print("Please enter the S M or L.")

print(sum_price)




#Do you want pepperoni? Y or N
#add Pepperoni Price +$2 to small size
#add Pepperoni Price +$2 to Medium or Large size

#Do you want extra cheese? Y or N
#Extra cheese for any size piza +$1