class barang:
    def __init__(self, nama: str, harga: float, jumlah: int):
        self.nama = nama
        self.harga = harga
        self.jumlah = jumlah
       
    def total(self):
        return self.harga*self.jumlah

barang1 = barang("iphone", 12000000, 4)
barang2 = barang("android", 13000000, 9)

print(barang1.nama)
print(barang1.harga)
print(barang2.total())