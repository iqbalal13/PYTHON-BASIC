while True:
    user_input = input("Enter a number: ")
    i = int(user_input)
    if i in range(2,20):
        j = 1
        while j <= 20:
            if j % 2 == 1:
                print(j)
            j += 1
    elif i in range(1,19):
        j = 2
        while j <= 20:
            if j % 2 == 0:
                print(j)
            j += 1
    else:
        print("input salah")
        break