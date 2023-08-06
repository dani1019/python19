#print "Welcome to the tip calculator"
print("Welcome to the tip calculator")

#question "What was the total bill? $"
total_bill  = float(input("What wast the total bill? $"))

#question "What percentage tip would you like to give? 10, 12 or 15? "
#caculate total bill * output_value
#caculate total bill + (total bill * output_value)

percentage_tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
#caculate the percentage_tip
percentage_tip = percentage_tip / 100

#caculate the tip_bill
tip_bill  = total_bill * percentage_tip

#caculate the total bill
total_bill_end = total_bill + tip_bill

#question "How many people to split the bill? "
person_number = int(input("How many people to split the bill? "))

#output = person_number
#caculate total bill + (total bill * output_value)/ person_number
each_pay = total_bill_end / person_number
each_pay_as_int = round(each_pay, 2)

#print "Each person should pay: $"
message = f"Each person should pay: {each_pay_as_int}"

print(message)




