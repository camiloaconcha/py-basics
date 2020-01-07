student_names = []
student_names = ['Camilo', 'Andrés', 'Wilson']
student_names.append('Homer')

print(student_names[2], student_names[0], student_names[-2], student_names[3])

print("Is Wilson here?:", "Wilson" in student_names)

del student_names[2]

print("Is Wilson here?:", "Wilson" in student_names)
# Utilities
print("Carl" in student_names)
print("Homer" in student_names)
print('The students are: \n\t'+str(len(student_names)))
