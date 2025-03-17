class Bank:
    def __init__(self,name,ph):
        self.name=name
        self.phno=ph
        self.pin=2222
        self.balc=60000

    def pay(self,price):
        print(f'pay{price}rs')
        chi=input('proceed to payment(y/n): ').lower()
        if chi=='y':
            if self.balc >=price:
                pin=int(input('enter the upi pin:'))
                if pin==self.pin:
                    self.balc=price
                    return True
                else:
                    print('you enter the wrong pin')
            else:
                print('no cash')
            return False
        else:
            False
class Restaurant(Bank) :
    r_name='DADA BOUDI'
    r_loc='Bp'
    menu={
        'chicken briyani':260,
        'mutton briyani':400,
        'salad':100,
        'cold drinks':20,
        'fish finger':250,
        'chili chicken ':250,
    }
    @classmethod
    def display(cls):
        for i in Restaurant.menu:
            print(i,'\t',cls.menu[i])

class Zomato(Restaurant):
    print('Welcome to Zomato')
    def __init__(self,name,ph,add):
        self.name=name
        self.phno=ph
        self.address=add
        self.cart={}
        Bank.__init__(self,name,ph)

    def order(self):
        item=input('enter the item: ').lower()
        if item in Restaurant.menu:
            qty=int(input('enter the qty: '))
            self.cart[item]=qty*(Restaurant.menu[item])
        else:
            print('not available')

        ch=input('you want to add another item (Y/N): ').lower()
        if ch=='y':
            self.order()

    def display_cart(self):
        t=0
        for i in self.cart:
            print(i,'\t',self.cart[i])
            t+=self.cart[i]
        print('total bill: ',t)
        if self.pay(t):
            print('payment succesfull')
            print('order confirm to ',self.address) 
        else:
            print('payment failed')   

cust1=Zomato(input('enter the name'),int(input('enter the phno')),input('enter the address'))

            
        