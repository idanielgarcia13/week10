student_xnums = ["X000321", "X000111", "X000123"]

my_num = input('please enter num to look for: ')
if my_num in student_xnums:
    print('its in there')
else:
    print('its not in there')

student_xnums.append("X000101") #adds to the list

my_num = input('please enter num to look for: ')
if my_num in student_xnums:
    print('its in there')
else:
    print('its not in there')
