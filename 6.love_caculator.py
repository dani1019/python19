#print start
print("Welcome to the Love Calculator!")

#quesition user's name
your_name = input("What is your name?\n").upper()
#question somebody's name who caculator love percent with you 
there_name = input("What is their name?\n").upper()

#make variable the count of matched TRUE letter
matched_true = 0
#make variable the count of matched LOVE letter
matched_love = 0

#caculator name how match TRUE, LOVE letter
for letter in list('TRUE'):
    matched_true += your_name.count(letter)

for letter in list('LOVE'):
    matched_love += your_name.count(letter)

#convert matched_true + matched_love to two digit
score = int(f"{matched_true}{matched_love}")

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

#test score of if sentence to whethe if operate rightly 


#print love score with their's name
print("Your score is {score}")

#if score is less than 10 or greater than 90
#"Your score is **x**, you go together like coke and mentos."

#if score is between 40 and 50
#"Your score is **y**, you are alright together."

#otherwise
#"Your score is **z**."