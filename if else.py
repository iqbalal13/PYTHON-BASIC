harga = int(input("Masukkan harga: "))
jumlah = int(input("Masukkan jumlah: "))
hasil = harga*jumlah

if hasil >= 1000:
    print(str(hasil) +str(" hasilnya ribuan"))
elif hasil < 1000:
    print(str(hasil) +str(" hasilnya ratusan"))
else:
    print("masukkan input dengan benar")