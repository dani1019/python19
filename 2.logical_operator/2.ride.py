print("Welcome to rollarCoaster")
height = int(input("How tall are you? "))

if height > 120:
    print("You can ride.")
    age = int(input("How old are you? "))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("You can't ride.")