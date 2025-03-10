class Resume:
    r_name='Till 12th'
    
    def __init__(self, name, ph, email, marks, yop):
        self.name=name
        self.ph=ph
        self.email=email
        self.marks=marks
        self.yop=yop
        
    def pdisp(self):
        print('Name: ',self.name)
        print('Ph: ',self.ph)
        print('email: ',self.email)
        print('marks: ',self.marks)
        print('yop: ',self.yop)
        
class New_Resume(Resume):
    
    def __init__(self, name, ph, email, marks, yop, btech_marks, btech_yop):
        super().__init__(name, ph, email, marks, yop)
        self.btech_marks=btech_marks
        self.btech_yop=btech_yop
        
    def cdisp(self):
        super().pdisp()
        print('B.Tech Marks: ', self.btech_marks)
        print('B.Tech YOP: ',self.btech_yop)
        
ob=New_Resume('Irfan',9143247777,'iamhero337@gmail.com',61.2,2018,7.93,2024)
ob.cdisp()