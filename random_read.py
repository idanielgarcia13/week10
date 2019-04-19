
def main():
    try:
        num_file = open("numbers.txt", "r")
        #random_numbers = open('Unit 4 numbers.txt', 'r')

        line = num_file.readline()
        number = 0
        sum = 0
        iterations = 0

        try:
            while line != " ":
                line = line.rstrip('\n')
                number = int(line)
                print(number)
                sum = sum + int(line)
                #number = number + number
                line = num_file.readline()
                iterations = iterations + 1
        except ValueError:
            pass
    except FileNotFoundError:
        print("File not found. Please check the directory.")

    print("The total of the numbers: " + str(sum))
    print("Total count of numbers read from file: " + str(iterations))
    num_file.close()

main()