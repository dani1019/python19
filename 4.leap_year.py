#enter the year
year = int(input("Whick year do you want to check? "))

#variable
four = 4
one_hundred = 100
four_hundred = 400

#divided result 
divide_four = year % four
divide_one_hundred = year % one_hundred
divide_four_hundred  = year % four_hundred

#whether if check leap year
if divide_four == 0:
    if divide_one_hundred == 0:
        if divide_four_hundred == 0:
            print("leap year")
        else:
            print("Not leap year")
    else:
        print("leap year")
else:
    print("Not leap year")
