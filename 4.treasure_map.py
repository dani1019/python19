#make a list map
map_items = [['□','□','□'],['□','□','□'],['□','□','□']]
for map_item in map_items:
    print(map_item, end='\n\n')

#answer cols,rows where you want
num1, num2 = input("Where do you want to put the treasue? ")

cols = int(num1) - 1 
rows = int(num2) - 1

#set the x user writed
map_items[rows][cols] = "x"

#print the result
for map_item in map_items:
    print(map_item, end='\n\n')

