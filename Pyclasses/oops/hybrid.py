class Bank:
    b_name='SBI'
    b_loc='kolkata'

    def _init_(self,name,ph,pin):
        self.name=name
        self.ph=ph
        self.pin=pin
        self.bal=6000

    def payment(self,price):
        print(f"pay{self.price}Rs")
        ch=input('proceed to payment(y/n):')

        if ch=='y':
            if self.bal>=price:
                upin=int(input('entered UPI pin:'))

                if upin==self.pin:
                    self.bal-=price
                    return True
                
                else:
                    print('you entered wrong pin !!!!')
                    return False
            else:
                print('Gareeb insaan ........')
                return False
            
        else:
             False


class Restaurant(Bank):
    r_name='ITC'
    r_loc="kolkata"


    menu={
        'gobi curry ':1200,
        'veg biryani':1600,
        'brownie':800,
        'chai':550,
        'ice_cream':500,
        'tacos':760,
    }

    @classmethod
    def display(cls):
        for i in cls.menu:
            print(i,'\t',cls.menu[i])

class Zomato(Restaurant):

    print('Welcome to Zomato :)')
    Restaurant.display()
    def _init_(self,name,ph,address,pin):
            # self.name=name
            # self.ph=ph
            self.address=address
            Bank._init_(self,ph,address,pin)
            self.address=address
            self.cart()

    def order(self):
        item=input('enter your item :').lower()

        if item in Restaurant.menu:
            qty=int(input("enter quantity :"))
            self.cart[item]=qty*(Restaurant.menu)
        else:
            print('entered item is unavailable')

        ch=input('you want to add  more (y/n):')
        if ch=='y':
            self.order()

        def display_cart(self):
            total=0
            for i in self.cart:
                print(i,'\t',self.cart[i])
                total+=self.cart[i]
            print('Total amount is :',total)

            if self.payment(total):
                print('Payment successfull......')

                print(f"your order will be delivered to {self.address}")
            else:
                print('Payment Failed ........try again.')