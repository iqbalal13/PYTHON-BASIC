class triangle:
    def __init__(self, alas: int, tinggi: int):
        self.alas=alas
        self.tinggis=tinggi
        self.r_luas = alas*tinggi/2

    def luas(self):
        return f"luas segitiga: {self.r_luas}"

s1 = triangle(20, 30)
print(s1.luas())