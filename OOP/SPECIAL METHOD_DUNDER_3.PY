class String:
      
    # magic method to initiate object
    def __init__(self, string):
        self.string = string
    
    def __add__(self, other):
        return self.string + other
          
# Driver Code
if __name__ == '__main__':
      
    # object creation
    string1 = String('H')
  
    # print object location
    print(string1 + " World")