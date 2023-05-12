class Parent(): 
        
    # Parent's show method
    def display(self):
        print("ayah dan ibu")
    
    
# Inherited or Sub class (Note Parent in bracket) 
class Child(Parent): 
        
    # Child's show method
    def shows(self):
        print("anak2")
    
# Inherited or Sub class (Note Child in bracket) 
class GrandChild(Child): 
          
    # Child's show method
    def show(self):
        print("cucu")         
    
# Driver code 
g =GrandChild()   
g.shows()
g.display()
g.show()