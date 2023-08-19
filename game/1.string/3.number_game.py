#user write digit number and add one-digit number and two-digit number
two_digit_number = input("Type a two digit number. ")

sum = 0

for digit_item in two_digit_number:
    digit_item_int = int(digit_item)
    sum += digit_item_int

print(sum)

#other solution
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

result = int(first_digit) + int(second_digit)
print(result)