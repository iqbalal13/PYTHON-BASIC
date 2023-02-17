numbers = input("Enter a list of numbers separated by spaces: ")
numbers = [int(x) for x in numbers.split()]

for x in numbers:
    if x % 2 == 0:
        print(x, "is even")
    else:
        print(x, "is odd")