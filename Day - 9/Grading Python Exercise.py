Student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

print(Student_scores)
for student, score in Student_scores.items():
    if 91 <= score <= 100:
        print(f"{student}: Outstanding")
        student_grades[student] = "Outstanding"
    elif 81 <= score <= 90:
        print(f"{student}: Exceeds Expectations")
        student_grades[student] = "Exceeds Expectations"
    elif 71 <= score <= 80:
        print(f"{student}: Acceptable")
        student_grades[student] = "Acceptable"
    else:
        print(f"{student}: Fail")
        student_grades[student] = "Fail"

print(student_grades)