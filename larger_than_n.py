def Return_Larger_Than_Asked(numbers, n):
    for num in numbers:
        if num > n:
            print(num)

def main():
    numbers = []
    response = ''
    while response != 'q':
        response = input("Enter a number. Enter q to quit. ")
        if response != 'q':
            numbers.append(int(response))
    n = int(input("Enter the number for n: "))
    Return_Larger_Than_Asked(numbers, n)
    #print(numbers)
    print()




main()