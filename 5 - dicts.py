
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

# student.update({'name': 'Jeff', 'age': 60, 'phone' : '555-5555'})

# print(student.get('phone','Not Found'))

# age = student.pop('age')

print(student)
# print(age)
print("")

length = len(student)
print(length)
print("")

for key, value in student.items():
    print(key, value)
