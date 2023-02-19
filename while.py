while True:
    user_input = input("Enter a number: ")

    i = int(user_input)

    if i in range(0, 5):
        print("i is within the range of 0 to 4")
    elif i in range(5, 10):
        print("i is within the range of 5 to 9")
    else:
        print("i is greater than or equal to 10")
        break
    if i % 2 == 1:
        print("i is odd")