def check_number(number):
    if number > 0:
        print("Positive number")
    elif number < 0:
        print("Negative number")
    else:
        print("Zero")

# Example usage in a while loop
while True:
    try:
        user_input = int(input("Enter a number (enter 0 to exit): "))
        if user_input == 0:
            print("Exiting the program.")
            break  # Exit the loop if the user enters 0
        check_number(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")