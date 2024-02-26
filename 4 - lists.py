# lists, tuples, sets

courses = ['History', 'Math', 'Physics', 'CompSci']

nums = [1,5,2,4,3]

sorted_courses = sorted(courses)
min_course = min(courses)
max_course = max(courses)

nums.sort(reverse=True)

print(courses)
print(sorted_courses)
print(min_course)
print(max_course)
Physics_location = courses.index('Physics')
print(Physics_location)
print(courses[0:Physics_location])

for index, item in enumerate(courses, start=1):
    print(index, item)

#print(nums)
#print(min(nums))
#print(max(nums))
#print(sum(nums))
# print(help(float))

course_str = ' - '.join(courses)
print(course_str)

new_list = course_str.split(' - ')
print(new_list)

#print(help(list))
