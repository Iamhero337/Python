

#########Constructor Chaining & Method Chaining#########

class Match:
    name='ICC'
    team='IND'
    opt='NZ'
    
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def pdisp(self):
        print(self.a,self.b)
        
class Final(Match):
    year=2025
    time=2.30
    result='WON'
    
    def __init__(self, a, b, c, d):#Constructor Chaining
        super().__init__(a, b)
        self.c=c
        self.d=d
        
    def cdisp(self): #method chaining
        super().pdisp()
        print(self.c, self.d)
        
ob=Final(10,20,30,40)
print(ob.name,ob.team,ob.year,ob.result)

ob.cdisp()