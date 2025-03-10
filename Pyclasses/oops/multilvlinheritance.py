class c1:
    a=10
    b=20
    
    def __init__(self,p,q):
        self.p=p
        self.q=q
        
class c2(c1):
    c=30
    d=40
    
    
class c3(c2):
    e=50
    f=60
    
    def disp(self):
        print(self.a,self.b,self.c,self.d,self.f,self.p,self.q)
ob=c3(100,200)
ob.disp()