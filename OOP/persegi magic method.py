class persegi:
    def __init__(self, sisi: int):
        self.sisi=sisi
        
    def __add__(self, garis):
        return self.sisi*garis.sisi
    
l1 = persegi(100)
l2 = persegi(100)



print(l1+l2)
        
    