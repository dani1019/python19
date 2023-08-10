#print Welcome to Python Pizza Deliveries!
print("Welcome to Python Pizza Deliveries!")

#What size pizza do you want? S, M or L
#small Pizza $15
#Medium Pizza $20
#Large Pizza $25

#make the variable to sum_price
sum_price = 0

size = input("What size pizza do you want? S, M or L ")
#Do you want pepperoni? Y or N
want_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

#change entered letter to upper case
size_upper_letter = size.upper()
want_pepperoni_upper = want_pepperoni.upper()
extra_cheeze_upper = extra_cheese.upper()

if size_upper_letter == "S":
    sum_price += 15
    if want_pepperoni_upper == "Y":
        sum_price += 2
elif size_upper_letter == "M":
    sum_price += 20
    if want_pepperoni_upper == "Y":
        sum_price += 4
elif size_upper_letter == "L":
     sum_price += 25
     if want_pepperoni_upper == "Y":
        sum_price += 4
else:
    print("Please enter the S M or L.")

#Extra cheese for any size piza +$1
if extra_cheeze_upper == "Y":
    sum_price += 1

print(f"you pay ${sum_price}")

#add Pepperoni Price +$2 to small size
#add Pepperoni Price +$2 to Medium or Large size

#Do you want extra cheese? Y or N
