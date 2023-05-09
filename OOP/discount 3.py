class barang:
    discount = 0.5
    def __init__(self, nama: str, harga: float, jumlah: int):

        assert harga >=0
        assert jumlah >=0

        self.nama = nama
        self.harga = harga
        self.jumlah = jumlah
       
    def total(self):
        return self.harga*self.jumlah / self.discount
    
    

barang1 = barang("iphone", 12,4)
barang1.total()

barang2 = barang("android", 13, 2)
barang2.total()

print(barang1.total())
print(barang2.total())