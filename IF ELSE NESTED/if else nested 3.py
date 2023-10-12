number = int(input("Masukkan angka: "))

if (number >= 0):

    if number == 0:
        print('Number is 0')
    elif number >= 1:
        print('Number is positive')
    else:
        print('Number is negative')
else:
    print('Number is negative')