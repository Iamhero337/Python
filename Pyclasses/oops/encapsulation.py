class _School:
    School_name='KHGHS'
    Location='Kankinara'
    
    def __s_details(self,name):
        print(f"The name of the student is {name}.")
        

obj=_School()
# obj.__s_details('anda')


#the first way to access the private method is to use the class name
obj._School__s_details('anda')
#the second way to access is get set method
