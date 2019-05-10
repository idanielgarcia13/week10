thisdict = {
    "Brand" : "Apple",
    "Model" : "iPhone XS Max",
    "Storage" : "512GB"
}
print(thisdict)
print(thisdict["Model"])

print()
for x in thisdict:
    print(x + ": " + thisdict[x])

# searches dictionary if entry matches something on the left side, the object on the right side will print
i = input("Enter something to search: ")
try:
    print(thisdict[i])
except KeyError:
    print("not found")