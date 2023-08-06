#1.question "what is your current age?"
age = input("what is your current age? ")

age_as_int = int(age)
#2.caculate 90 - 56
standard_age = 90
lift_years = standard_age - age_as_int
#convert years to days, weeks, months
months_of_years = 12
weeks_of_years = 52
days_of_years = 365

lift_months = lift_years * months_of_years
lift_weeks = lift_years * weeks_of_years
lift_days = lift_years * days_of_years

#print "You have {days} days {week} weeks {months} months leff"
message = f"You have {lift_days} days {lift_weeks} weeks {lift_months} months left"

print(message)