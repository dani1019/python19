number = int(input("enter the number: "))

#check if entered number is prime number
def prime_number(number):
    #save count except the divided in 1 or number 
    cnt = 0
    
    #entered number is lower than over, display "entere the number over 0" message
    if number < 0:
        print("enter the number over 0")
        return
    
    #count except  the divided in 1 or number 
    #error if i != 1 enter the number % i == 0
    for i in range(1, number + 1):
        if i == 1 or i == number:
              pass
        else:
            cnt += 1

    #count is 0, It's a prime number.
    if cnt == 0:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

#exist method
prime_number(number)
