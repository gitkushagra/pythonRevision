
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}



for key in student_scores:
    if(student_scores[key] >= 91):
        grade = "Outstanding"
    elif (student_scores[key] >=81 and student_scores[key] <= 90):
        grade = "Exceeds Expectations"
    elif (student_scores[key] >= 71 and student_scores[key] <= 80):
        grade= "Acceptable"
    else:
        grade = "Fail"
    student_grades[key] = grade


print(student_grades)