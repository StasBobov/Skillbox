import os

FILE_PATH = os.path.join(os.path.dirname(__file__), 'students.csv', )

with open(FILE_PATH, 'r', encoding='utf-8') as f:
    headers = f.readline().split(',')
    students_1 = f.read().split('\n')


students = []
for next_student in students_1:
   students.append(next_student.strip().split(','))

course_students = []
# STEP1: input
course_name = input("Enter course name: ")
# STEP 2: search
for next_student in students:  # Loop students
    if course_name == next_student[7]: course_students.append(next_student)
    pass  # End loop students

table_to_print = ""
for hdr in headers:
    table_to_print += f'{hdr:30s}'
table_to_print += '\n'

for next_student in students:
    for fld in next_student:
        table_to_print += f'{fld:30s}'
    table_to_print += '\n'

print(table_to_print)

FILE_PATH = os.path.join(os.path.dirname(__file__), 'course_students.txt')
with open(FILE_PATH, 'w', encoding='utf-8') as f:
    print(table_to_print, file=f)



student_name  = input('')

for next_student in students:
    if next_student[1] == student_name:
        print(next_student)


dict_students = {}
for i in students:
    if i[7] in dict_students:
        dict_students[i[7]].append(i)
    else:
        dict_students[i[7]] = [i]

for k , m in dict_students.items():
    print(k, m)
