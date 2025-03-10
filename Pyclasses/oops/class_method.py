class TestYantra:
    employees=3000
    loc='Bengaluru'
    branch='Rajajinagar'

    def __init__(self,name,age,designation):
        self.name=name
        self.age=age
        self.designation=designation

    def display(self):
        print(self.name,self.age,self.designation,self.branch)

    @classmethod
    def details(cls):
        print(cls.employees,cls.loc,cls.branch)

    @classmethod
    def mod_branch(cls,new):
        cls.branch=new

    def mod_branch(self,new):
        self.branch=new
    
    
ob=TestYantra('Dhruv sir',25,'Python-Dev')
ob.display()
ob.details()
TestYantra.details()
#TestYantra.mod_branch("Ranininagar")
#TestYantra.details()
ob.mod_branch('Kolkata')
ob.display()
ob.details()
    
