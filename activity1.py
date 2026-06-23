import numpy as np
data_type = [('Name', 'U10'), ('Age', 'i4'), ('Height', 'f4')]
student_details =[('John', 20, 5.9), ('Alice', 22, 5.5), ('Bob', 19, 6.0)]
students = np.array(student_details, dtype=data_type)
print("original array:")
print(students)
print("\nArray after sorting by Age:") 
students_sorted = np.sort(students, order='Age')
print(students_sorted)