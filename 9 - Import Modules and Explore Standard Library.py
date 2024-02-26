# import sys # imports directories from Python_Path environment variable and standard library directories
# sys.path.append('../../Desktop')

# import my_module_video_9 as mm   #allows us to import files and rename them to something more convenient
# from my_module_video_9 import find_index, test #allows us to import specific functions from a file

import random
import datetime
import calendar
import os
#import antigravity
import webbrowser

courses = ['History', 'Math', 'Physics', 'CompSci']

# index = find_index(courses, 'Math')
# print(index)
# print(test)

# print(sys.path)

# random_course = random.choice(courses) #random number generator that I need for Gratitude app
# print(random_course)

print(os.getcwd())
print(os.__file__)
# print(random.__file__)
# print(random.__all__)
# print(calendar.__all__)
# print(webbrowser.__all__)
# webbrowser.open("https://www.coachandgeek.com")
