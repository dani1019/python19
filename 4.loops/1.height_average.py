#input a list of student heights
height_string = input("input a list of student heights ")

#convert string to list 
height = height_string.split(' ')

#convert element of list to integer
height_int = [int(height_one) for height_one in height]

num_items = len(height_int)

#make variable the sum of height
sum = 0

#the sum of height element
for height_element in height_int:
    sum += height_element

#the average of height
height_average = sum / num_items

#round up decimal
height_average_round = round(height_average)

#print the height_average
print(height_average_round)
    



