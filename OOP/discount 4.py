class barang:
    def __init__(self, nama: str, harga: float, jumlah: int, discount: float):

        assert harga >=0
        assert jumlah >=0
        assert discount >= 0
        self.nama = nama
        self.harga = harga
        self.jumlah = jumlah
        self.discount = discount
       
    def total(self):
        return self.harga*self.jumlah / self.discount
    
    

barang1 = barang("iphone", 12, 4, 0.8)
barang.total()

barang2 = barang("hp brand " + "android", 13, 2, 0.9)
barang2.total()

print(barang1.total())
print(barang2.total())