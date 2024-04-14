#1. Python List Transformation

#Objective: The aim of this assignment is to practice 
# advanced list operations and transformations.

#Task 1: Given the list of grades:

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

#

print("Grades:", 95, 93, 90, 89, 88, 85, 80, 78, 76, 72 )



Average =  (72 + 76 + 78 + 80 + 85 + 88 + 89 + 90 + 93 + 95) / 10 
print("Average Grade is..")
print(Average)

print("Any Grade that is '80' and above is a Passing Grade, any grade below '80' is a Failing Grade:")
for grade in grades:
    if grade <= 79:
        print(grade, 'FAILED!!!')
    else:
        print (grade, 'PASSED!!!')


