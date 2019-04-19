import random

def generate_random():
    return(random.randint(1, 500))

def main():
    nums_file = open("numbers.txt", "w")
    iterations = int(input("How many random numbers would you like generated to the file? "))
    for num in range(iterations):
        nums_file.write(str(generate_random()) + "\n")

    print("\nFile successfully created.")
    nums_file.close()

main()