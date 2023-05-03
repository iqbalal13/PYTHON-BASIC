class hewan:
    def __init__(self, nama: str, daerah: str, jenis: str ):
     self.nama = nama 
     self.daerah = daerah
     self.jenis = jenis

    def namahewan(self):
        return self.nama
    def ganti_nama(self,nama):
        self.nama = nama

hewan1 = hewan("ceetah", "afrika", "karnivora")
hewan1.ganti_nama("macan")
print(hewan1.nama)