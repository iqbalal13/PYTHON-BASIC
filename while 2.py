while True:
    user_input = input("Enter a number: ")
    i = int(user_input)
    if i == 1:
        j = 1
        while j <= 10:
            if j % 2 == 1:
                print(j)
            j += 1
    elif i in range(2, 10):
        print("i is within the range of 2 to 9")
    else:
        print("i is greater than or equal to 10")
        break

