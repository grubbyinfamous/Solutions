'''
Things to do:
Write a class named Person with attributes for a person's name, address, and telephone number
Write a class named Customer that is a subclass of the Person class
The Customer should have a data attribute for a customer number, and a boolean data attribute of whether or not they want to be on a mailing list
'''
import random

#This is where I will write the person class, with setters and getters
class Person:
    #name, address, and tel_phone should all be strings
    def __init__(self, name, address, tel_phone):
        self.name = name
        self.address = address
        self.tel_phone = tel_phone

    def get_Name(self):
        return self.name
    
    def get_Address(self):
        return self.address
    
    def get_Tel_Phone(self):
        return self.tel_phone
    
    def set_Name(self, name):
        self.name = name

    def set_Address(self, address):
        self.address = address

    def set_Tel_Phone(self, tel_phone):
        self.tel_phone = tel_phone

#This is where I will write the Customer class, with setters and getters
#Customer number will be an integer and isMailing is a boolean
class Customer(Person):
    def __init__(self, name, address, tel_phone, customer_number, isMailing):
        super().__init__(name, address,tel_phone)
        self.customer_number = customer_number
        self.isMailing = isMailing

    def get_customer_number(self):
        return self.customer_number
    
    def get_isMailing(self):
        return self.isMailing
    
    def set_Customer_Number(self,customer_number):
        self.customer_number = customer_number

    def set_isMailing(self, isMailing):
        self.isMailing = isMailing

    #This will display whether or not the customer is on the mailing list
    def areTheyMailing(self):
        if self.isMailing == True:
            return f"{self.get_Name()} is on the mailing list"
        
        else:
            return f"{self.get_Name()} is not on the mailing list"
        
if __name__ == '__main__':
    user_Name = ""
    user_Address = ""
    user_Tel_Phone = ""
    user_Customer_Number = ""
    user_IsMailing = ""

    print("Welcome to First Credit Union Program! We thank you for joining this program, and all you need to do is give us your information")
    user_Name = input("Please enter your name: ")
    user_Address = input("Please enter your address: ")
    user_Tel_Phone = input("Please enter your telephone number: ")
    #I believe that the user should be given a customer number since I am assuming they are new to the bank
    user_Customer_Number = random.randint(1, 999999)

    #This loop will ensure that the user enters a Y or N for the isMailing
    while True:
        user_IsMailing = input("Would you like to enter our mailing list? Y/N ")

        if user_IsMailing.upper() == "Y":
            customer = Customer(user_Name, user_Address, user_Tel_Phone, user_Customer_Number, True)
            break
        elif user_IsMailing.upper() == "N":
            customer = Customer(user_Name, user_Address, user_Tel_Phone, user_Customer_Number, False)
            break
        else:
            print("Please type Y or N")

    #Here is where I will show the user's information
    print("Here is your information:")
    print(f"{customer.get_Name()} is your name.")
    print(f"{customer.get_Address()} is your address")
    print(f"{customer.get_Tel_Phone()} is your phone number")
    print(f"{customer.get_customer_number()} is your customer number")
    print(customer.areTheyMailing())
            
