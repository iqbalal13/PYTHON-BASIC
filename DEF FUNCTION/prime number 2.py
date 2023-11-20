try:
    user_input = int(input("Enter a number: "))

    if user_input < 2:
        print(f"{user_input} is not a prime number.")
    else:
        is_prime = True
        for i in range(2, int(user_input**0.5) + 1):
            if user_input % i == 0:
                is_prime = False
                break

        if is_prime:
            print(f"{user_input} is a prime number.")
        else:
            print(f"{user_input} is not a prime number.")

except ValueError:
    print("Error: Please enter a valid integer.")