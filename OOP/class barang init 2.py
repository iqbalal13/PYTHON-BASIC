class orang:
    def __init__(self, nama, umur, tinggi):
        self.nama = nama
        self.umur = umur
        self.tinggi = tinggi
    
    def orang_atribut (self, x, y, z):
        return x, y, z

orang1 = orang("iqbal", 23, 170)
orang2 = orang("al", 27, 189)

print(orang1.nama)

