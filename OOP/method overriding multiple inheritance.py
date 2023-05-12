class ayah():
          
    # Parent's show method
    def show(self):
        print("ayah")
          
# Defining Parent class 2
class ibu():
          
    # Parent's show method
    def display(self):
        print("ibu")
          
          
# Defining child class
class anak(ayah, ibu):
          
    # Child's show method
    def shows(self):
        print("anak2 dari ayah dan ibu")
     
        
# Driver's code
obj =anak()
  
obj.show()
obj.shows()
obj.display()