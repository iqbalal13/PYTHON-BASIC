def square(x):
    return x * x

try:
    num = int(input("Enter a number: "))
    result = square(num)
    print("The square of", num, "is:", result)
except ValueError:
    print("Invalid input. Please enter a number.")