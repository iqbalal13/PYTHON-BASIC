harga = int(input("Masukkan harga: "))
jumlah = int(input("Masukkan jumlah: "))
diskon = 10/100
hasil = harga*jumlah

if hasil >= 1000 <= 1500:
    print(hasil*diskon)
elif hasil < 1000 > 500:
    print(hasil)
else:
    print("masukkan input dengan benar")