#repeat number in function from up to bottom(only print number inside function without multyplying)
#def angka2(*angka):
    #for angka in angka:
        #print(angka)

#angka2(1, 2, 3, 4)

#repeat number in function by multiplying line
# def angka2(*angka):

    #for angkaa in angka:
        #print(angka)

#angka2(1,2,3,4,5)

def angka2(*angka):
    jumlah = 5
    for angka in angka:
        jumlah *= angka
    return jumlah

print(angka2(1,2,3,4,5))