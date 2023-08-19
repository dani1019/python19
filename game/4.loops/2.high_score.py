#print Input a list of student scores
scores_string = input("Input a list of student scores: ")

scores = scores_string.split()

#make a variable save a little time
temp = 0

#convert string to int
#the hightest move right
for n in range(len(scores)):
    scores[n] = int(scores[n])

    if n >= 1:
        print(scores[n - 1])
        print(scores[n])
        if scores[n] < scores[n - 1]:
            temp = scores[n - 1]
            scores[n - 1] = scores[n]
            scores[n] = temp

    #print the highest score in class
    if n == len(scores) - 1:
        print(f"the highest score in the class is {scores[n]}")