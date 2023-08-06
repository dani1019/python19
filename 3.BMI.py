#question height to user
height = float(input("enter your height in m: "))
#question weight to user
weight = int(input("enter your weight in kg: "))

#caculate the bmi
bmi_round = round(weight / height ** 2)

#check user's body
if bmi_round < 18.5:
    print(f"Your BMI is {bmi_round}, you are underweight.")
elif bmi_round < 25:
    print(f"Your BMI is {bmi_round}, you have a normal weight.")
elif bmi_round < 30:
    print(f"Your BMI is {bmi_round}, you are slightly overweight.")
elif bmi_round < 35:
    print(f"Your BMI is {bmi_round}, you are obese.")
else:
    print(f"Your BMI is {bmi_round}, you are clinically obese.")


