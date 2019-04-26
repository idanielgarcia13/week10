student_xnums = ["X000321", "X000111", "X000123"]

my_xnum = input('please enter num to look for: ')

try:
    result = student_xnums.index(my_xnum)
    print(result)
except ValueError:
    print(result, "- Value is not found.")