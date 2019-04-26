list1 = [1, 2, 3]
list1 += [4, 5, 6]

new_list = list1[2:6] #slices and returns that chunk

print(new_list)

for num in new_list:

    print(num, ", ", sep="", end="")