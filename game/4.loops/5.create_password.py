import string
import random

#get string of all letters
all_letters = string.printable
#get alphabet of symbols and convert list
alphabet = list(all_letters[10:62])
#print(alphabet)
#get string of symbols and convert list
symbols = list(all_letters[-32:-1])
#print(symbols)
#get string of alphabet and convert list
numbers = list(all_letters[0:10])
#print(number)

#print How many letters would you like in your password?
letters_num = int(input("How many letters would you like in your password? "))   
#How many symbols would you like?
symbols_num = int(input("How many symbols would you like? "))
#How many numbers would you like?
numbers_num = int(input("How many numbers would you like? "))
#operate alphabet numer
alphabet_num = letters_num - (symbols_num + numbers_num)

#select randomly alphabet and symbol , numbers
alphabet_items = random.sample(alphabet,alphabet_num)
symbol_items = random.sample(symbols, symbols_num)
numbers_items = random.sample(numbers, numbers_num)

#combine list of alphabet and symbol , numbers
letters = alphabet_items + symbol_items + numbers_items
print(letters)

#shuffled the list of element
letters_shuffled = "".join(random.sample(letters,letters_num))

#convert list to string
# letters_combine = ""
# for letter in letters:
#     letters_combine+= letters_shuffled)

#print the letters_combine
print(letters_shuffled)





#Here is your password: