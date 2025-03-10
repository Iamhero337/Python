class Temp:
    
    def __init__(self,temp=20):
        self.tmep=temp
    
    def inc_temp(self):
        self.tmep+=1
        print('Current temp is: ',self.temp)
        
    def dec_temp(self):
        self.temp-=1
        print('Current temp is: ',self.temp)
        
    def set_temp(self, new):
        self.temp=new
        print('Current tem is: ',sefl.temp)
        
class Bright:
    
    def __init__(self,bright=0):
        self.bright=bright
        
    def turn_on(self):
        self.bright=100
        print('Light is turned on =_=')
    
    def turn_off(self):
        self.bright=0
        print('Light is turned off =_=')
    
    def set_brigh(self, new):
        if self.bright:
            self.bright=new
            print('Bright is set to:',self.bright)
        else:
            print('Turn on light first =_=')
            
class User(Temp,Bright):
    
    def __init__(self, temp=20, bright=0):
        Temp.__init__(self,temp)
        Bright.__init__(self,bright)
        
    def status(self):
        print(f'Current status of Temp is:{self.temp}')
        print(f'Current status of Brightnessis:{self.bright}')
        

ob=User()