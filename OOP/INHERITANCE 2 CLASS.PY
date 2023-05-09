class pegawai:
    def __init__(self, nama, gaji: int):
        self.nama=nama
        self.email=  nama+ "@gmail.com"
        self.gaji = gaji
    
    def gaji_bersih(self):
        return self.gaji - 0.3
    
class company(pegawai):
    def __init__(self, nama, gaji: int):
        super().__init__(nama, gaji)
        self.potongan = 0.3
    
    def dipotong(self):
        return self.gaji - 0.3*2

    
    
pegawai1= company("iqbalalmaudi", 20000)
print(pegawai1.email)
print(pegawai1.dipotong())

