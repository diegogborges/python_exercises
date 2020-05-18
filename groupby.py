from itertools import groupby

students = [
    {'name': 'André', 'grade': 'A'},
    {'name': 'Leticia', 'grade': 'D'},
    {'name': 'Rose', 'grade': 'B'},
    {'name': 'André', 'grade': 'E'},
    {'name': 'João', 'grade': 'B'},
    {'name': 'Diego', 'grade': 'A'},
    {'name': 'Alberto', 'grade': 'D'},
    {'name': 'Karen', 'grade': 'B'},
    {'name': 'Anderson', 'grade': 'C'},
    {'name': 'Antonio', 'grade': 'A'},
]

order = lambda item: item['grade']

# sort is necessary for groupings
students.sort(key=order)
print(students)
print()

for student in students:
    print(student)

students_grouped = groupby(students, order)

for grouping, values_grouped in students_grouped:
    print(f'grouping: {grouping}')
    for student in values_grouped:
        print(student)
    print()

print()
for grouping, values_grouped in students_grouped:
    print(f'grouping: {grouping}')

    quantity = len(list(values_grouped))
    print(f'{quantity} students got the grade {grouping}')

from itertools import tee

print()
for grouping, values_grouped in students_grouped:
    va1, va2 = tee(values_grouped)

    print(f'grouping: {grouping}')

    for student in va1:
        print(f'\t{student}')

    quantity = len(list(va2))
    print(f'\t{quantity} students got the grade {grouping}')
    print()
