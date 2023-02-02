harga = int(input("Masukkan harga: "))
jumlah = int(input("Masukkan jumlah: "))
diskon = 10/100
hasil = harga*jumlah

if hasil >= 1000 or hasil <= 1500:
    print(str(hasil*diskon)+(str(" hasilnya ratusan")))
elif hasil < 1000 or hasil > 500:
    print(str(hasil)+(str("hasilnya ratusan")))
else:
    print("masukkan input dengan benar")