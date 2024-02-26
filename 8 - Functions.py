
# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #started with 0 because a list always starts with 0, but there's no month at position 0


def is_leap(year):
    """Return True for leap years, False for non-leap years."""  #this is a doc strong that defines what this function does

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    # year 2017
    # month 2
    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

# print(is_leap(2017))
print(days_in_month(2024, 2))

# def hello_func(greeting = "Welcome", name = 'you'):
#     return '{} {}'.format(greeting, name)

# def adder(x, y):
#     """ returns the additon of two numbers """
#     return x+y

# print(hello_func('Hello', 'Sandy'))

# print(adder(3,4))

# x = 0
# while x <= adder(3, 4):
#     print(x)
#     x += 1

# def student_info(*args, **kwargs): #kwargs = key word arguments
#     print(args)
#     print(kwargs)

# courses = ('Math', 'Art')
# info = {'name':'John', 'age': 22}

# student_info(*courses, **info) #the * and ** unpacks the positional and keyword args


