class Bank:
    B_name='SBI'
    B_ifsc='SBIN001883'
    B_add='Sec-V'
    B_pincode=700091

    def __init__(self,name,ac,pin):
        self.name=name
        self.ac=ac
        self.pin=pin
        
    def display(self):
        print(self.B_name,self.B_ifsc,self.name,self.ac,self.pin)
    
    def mod_pin(self,new):
        self.pin=new

ob=Bank('Aman',6969696969696, 8888)
ob1=Bank('Chaman',79797979797, 9999)
#ob.diplay()
# Bank.display(ob)
# ob1.display()

print('Before modification:')
Bank.display(ob)
#ob1.display()
print('After modification: ')
ob.mod_pin(1563)
ob.display()