def triangle(base, height):
    return 0.5 * base * height
try:
    base = int(input("Enter the base of the triangle: "))
    height = int(input("Enter the height of the triangle: "))
    result = triangle(base, height)
    print("The area of the triangle with base", base, "and height", height, "is:", result)

except ValueError:
    print("Invalid input. Please enter a number.")

try:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    result = triangle(base, height)
    print("The area of the triangle with base", base, "and height", height, "is:", result)
except ValueError:
    print("Invalid input. Please enter a number.")