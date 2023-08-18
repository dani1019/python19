student_scores = {
    "Ronaldo" : 81,
    "Messi" : 78,
    "Kane" : 99,
    "Rooney" : 74,
    "Keane" : 62 
}

student_grades = {}
#check score and set scoring criteria
for name, score in student_scores.items():
    if score >= 91 and score <= 100:
        student_grades[name] = "Outstanding"
    elif score >= 81 and score <= 90:
        student_grades[name] = "Exceeds Expections"
    elif score >= 71 and score <= 80:
        student_grades[name] = "Acceptable"
    else:
        student_grades[name] = "Fail"

print(student_grades)