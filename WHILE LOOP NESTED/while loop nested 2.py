i = int(input("masukkan angka: "))
while i <= 10:
    j = 4
    print(j, end=' ')
    j += 1
    while j <= i:
        print(j, end=' ')
        j += 1
    print()
    i += 1