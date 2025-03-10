class ATM:
    B_name='SBI'
    B_loc='Mahesbathan'
    
    def __init__(self,name,pin,bal):
        self.name=name
        self.pin=pin
        self.bal=bal
        
    def display(self):
        print(self.B_loc,self.name,self.bal)
        
    def deposit(self,amt):
        self.bal=self.add(self.bal,amt)
        
        
    def withdraw(self,amt):
        if amt<self.bal:
            self.bal=self.sub(self.bal,amt)
        else:
            print("Gareeb...")
            
    @classmethod
    def details(cls):
        print(cls.B_name,cls.B_loc)
        
    @staticmethod
    def add(a, b):
        return a+b
    @staticmethod
    def sub(a, b):
        return a-b
        
ob=ATM("SKR sir", 420, 6000)
ob.display()
ob.deposit(240)
ob.display()
ob.withdraw(7000)
ob.display()
ob.withdraw(6000)
ob.display()
