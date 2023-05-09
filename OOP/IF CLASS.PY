class murid:
    def __init__(self, nama, umur, peringkat):
        self.nama = nama
        self.umur = umur
        self.peringkat = peringkat
    
    def peringkatnya(self):
        return self.peringkat
    
class pelajaran:
    def __init__(self, nama, max_murid):
        self.nama = nama
        self.max_murid = max_murid
        self.murid = []
    
    def add_murid(self, murid):
        if len(self.murid) < self.max_murid:
            self.murid.append(murid)
            return True
        return False
    def rata_rata(self):
        value = 0
        for murid in self.murid:
            value += murid.get_peringkat()
        
        return value / len(self.murid)

s1= murid("iqbal", 16, 98)

course = pelajaran("math", 6)

print(course.rata_rata)