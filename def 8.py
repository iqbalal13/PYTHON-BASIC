def trapezium_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

try:
    base1 = float(input("Enter the length of the first base: "))
    base2 = float(input("Enter the length of the second base: "))
    height = float(input("Enter the height of the trapezium: "))
    result = trapezium_area(base1, base2, height)
    print("The area of the trapezium with first base", base1, "second base", base2, "and height", height, "is:", result)

except ValueError:
    print("Invalid input. Please enter a number.")

