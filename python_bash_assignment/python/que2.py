
"""Create a dictionary where the keys are student names and the values are their grades. Allow the user to:
Add a new student and grade.
Update an existing student’s grade.
Print all student grades.
Used dictionary and basic operations. Using if else:
"""

#score dict
score_dict={
    "Hrituja": 97,
    "Shalini": 87,
    "Manas": 92
}

#update student grade
score_dict["Shalini"]=89
#Print dict
print(score_dict)

#print grades of student
for key, values in score_dict.items():
    print(values)
