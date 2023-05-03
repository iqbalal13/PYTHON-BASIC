class barang:
    discount = 0.5
    def __init__(self, nama: str, harga: float, jumlah: int):

        assert harga >=0
        assert jumlah >=0

        self.nama = nama
        self.harga = harga
        self.jumlah = jumlah
       
    def total(self):
        return self.harga*self.jumlah
    
    def diskon(self):
         self.harga = self.harga / barang.discount

barang1 = barang("iphone", 12,4, 0.7)
barang1.total()
barang1.diskon()

barang2 = barang("android", 13, 2, 0.4)
barang2.total()
barang2.diskon()

print(barang1.total())
print(barang2.total())