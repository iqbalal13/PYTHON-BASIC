while True:
    try:
        user_input = int(input("Enter a number (enter 0 to exit): "))
        
        if user_input == 0:
            print("Exiting the program.")
            break  # Exit the loop if the user enters 0
            
        if user_input > 0:
            print("Positive number")
        elif user_input < 0:
            print("Negative number")
        else:
            print("Zero")
            
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        continue  # Skip the rest of the loop body and ask for input again