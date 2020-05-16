
class Test:
    
    def Name(self,name):
        self.name = name
        
    def Show(self):
        print("Hello : %s" % self.name)
    
    def Value(self,value):
        Ans = value * 5
        return Ans
                 
  
  
t1=Test()
t1.Name("CHE")
t1.Show()
        
t2=Test()
t2.Name("Mo")
t2.Show()

t3=Test()
print(t3.Value(5))

    
        

    

        
  
    
        



