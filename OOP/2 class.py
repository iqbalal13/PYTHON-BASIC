class mobil:
    def  __init__(self, jeep: str, sedan: str, pickup: str):
        self.jeep = jeep
        self.sedan = sedan
        self.pickup = pickup

    def mobil_sedan(self):
        return self.sedan

    def mobil_jeep(self):
        return self.jeep
    
    def mobil_pickup(self):
        return self.pickup
    
    def ganti_sedan(self,sedan):
     self.sedan = sedan
    
    def ganti_pickup(self,pickup):
     self.pickup = pickup
    
    def ganti_jeep(self,jeep):
     self.jeep = jeep

class motor:
    def  __init__(self, bebek: str, balap: str, trail: str):
        self.bebek = bebek
        self.balap = balap
        self.trail = trail
    
    def motor_bebek(self):
        return self.bebek

    def motor_balap(self):
        return self.balap
    
    def motor_trail(self):
        return self.trail
    
    def ganti_bebek(self,bebek):
     self.bebek = bebek
    
    def ganti_balap(self,balap):
     self.balap = balap

    def ganti_trailp(self,trail):
     self.trail = trail

motor1 = motor("mio", "ninja", "brandong")
motor1.ganti_bebek("mio j")
print(motor1.bebek)

