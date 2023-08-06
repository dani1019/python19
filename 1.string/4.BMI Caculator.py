#enter your height.
#enter your weight.
#caculate weight / height**2
#result integer

# your_height = float(input("enter your height. "))
# your_weight = float(input("enter your weight. "))

# print(int(your_weight / (your_height**2)))

#another solution
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = int(weight) / float(height)**2
bmi_as_int = int(bmi)
print(bmi_as_int)
