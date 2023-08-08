#print start
print("Welcome to the Love Calculator!")

#quesition user's name
your_name = input("What is your name?\n")
#question somebody's name who caculator love percent with you 
their_name = input("What is their name?\n")

combined_string = your_name + their_name
lower_case_string = combined_string.lower()

#make variable the count of matched TRUE letter
true = 0
#make variable the count of matched LOVE letter
love = 0

#caculator name how match TRUE, LOVE letter
for letter in list('true'):
    true += lower_case_string.count(letter)

for letter in list('love'):
    love += lower_case_string.count(letter)

#convert matched_true + matched_love to two digit
love_score = int(f"{true}{love}")

#print love score with their's name
if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40 )and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")

#test score of if sentence to whethe if operate rightly

#if score is less than 10 or greater than 90
#"Your score is **x**, you go together like coke and mentos."

#if score is between 40 and 50
#"Your score is **y**, you are alright together."

#otherwise
#"Your score is **z**."