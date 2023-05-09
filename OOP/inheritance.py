class animal:
    def __init__(self, jenis: str, kelamin: str):
        self.jenis = jenis
        self.kelamin = kelamin
    
    def kalimat(self):
       print(f"ini adalah {self.jenis} dan jenis kelaminnya adalah {self.kelamin}")
    
class kucing(animal):
    def bunyi(self):
        print("meow")

class anjingg(animal):
    def bunyi(self):
        print("guk guk")


animal2 = kucing("kucing anggora", "laki-laki")
animal2.bunyi()
