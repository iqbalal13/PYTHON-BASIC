class vehicle():
    def __init__(self, motor: str, mobil: str, sepeda: str):
        self.motor = motor
        self.mobil =  mobil
        self.sepeda =  sepeda
        self.bbm = 30.000
    
    def bbm_mobil(self):
        return self.bbm*100
    
    def bbm_motor(self):
        return self.bbm*50
    
    def bbm_sepeda(self):
        return self.bbm*2

class transportasi(vehicle):
    def __init__(self, kereta: str, bus: int, angkot: str):
        super().__init__(kereta, bus, angkot)
        self.bbm = 100.000

    def bunyi(self):
        print("ting")


kendaraan1 = vehicle("ferrari", "yamaha r1", "brompton")   
kendaraan2 = transportasi("gajahmada", "transjakarta", "29") 

print(kendaraan2.bunyi())