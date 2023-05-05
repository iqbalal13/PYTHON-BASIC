class barang:
    def total(self, x, y):
        return x * y


barang_barang = barang()
barang_barang.name = "VGA"
barang_barang.jumlah = 1
barang_barang.harga = 12000000
print(barang_barang.total(barang_barang.jumlah, barang_barang.harga))

