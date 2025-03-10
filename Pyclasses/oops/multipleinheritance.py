class p1:
    a = 10
    b=20
    def add(self):
        print("p1")
class p2:
    c=30
    def add(self):
        print("p2")
class p3:
    d=40
    def add(self):
        print("p3")
class allll(p3,p2,p1):
    pass
    # def add(self):
    #     print('alll')
ob=allll()
ob.add()
