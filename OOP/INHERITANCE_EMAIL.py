class pegawai:
    def __init__(self, nama, gaji: int):
        self.nama=nama
        self.email=  nama+ "@gmail.com"
        self.gaji = gaji
    
    def gaji_bersih(self):
        return self.gaji - 0.3
    
def __str__(self):
    return "{} {}".format(self.email), (self.nama)
    
pegawai1= pegawai("iqbalalmaudi", 20000)
print(pegawai1.email)
print(pegawai1.gaji_bersih())

