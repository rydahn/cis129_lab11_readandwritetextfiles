# Jesus Ramos
# 04/15/2024
# Module 11 Lab
"""This program demonstrates how to write data to a CSV file"""

# Part 1: Store Grades into a Text File

with open ('grades.txt', mode='w') as grades:
    grades.write('88\n')
    grades.write('90\n')
    grades.write('92\n')
    grades.write('94\n')
    grades.write('96\n')

# Part 2: Read Grades from 'grades.txt' and Calculate Average

with open('grades.txt', mode='r') as grades:
    print(f'{"Grade Number":<15}{"Grade":>5}')
    total = 0
    count = 0
    for record in grades:
        grade = int(record.strip())
        total += grade
        count += 1
        print(f'{count:<15}{grade:>5}')

    if count > 0:
        average = total / count
    else:
        average = 0

    print(f'Total of Grades: {total}')
    print(f'Count of Grades: {count}')
    print(f'Average Grade: {average:.2f}')

# Part 3: Store Data in a CSV File

import csv

with open('grades.csv', mode='w', newline='') as grades:
    writer = csv.writer(grades)
    writer.writerow(['First Name', 'Last Name', 'Exam1', 'Exam2', 'Exam3'])
    writer.writerow(['Chris', 'Redfield', 88, 92, 85])
    writer.writerow(['Leon', 'Kennedy', 98, 80, 92])
    writer.writerow(['Jill', 'Valentine', 94, 90, 96])

with open('grades.csv', 'r', newline='') as grades:
    print(f'{"First Name":<12}{"Last Name":<12}{"Exam1":>5}{"Exam2":>6}{"Exam3":>6}')
    reader = csv.reader(grades)
    next(reader)
    for record in reader:
        first_name, last_name, exam1, exam2, exam3 = record
        print(f'{first_name:<12}{last_name:<12}{exam1:>5}{exam2:>6}{exam3:>6}')