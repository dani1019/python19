import random

#make the list selecting name
name_string = input("write the person's name. ")
name = name_string.split(",")
num_items = len(name)

#select index
index = random.randint(0, num_items - 1)

#select the random name from name_list
selected_name = name[index]

#print the name pay for everybody's food bill
print(f"{selected_name} is going to buy the meal today!")