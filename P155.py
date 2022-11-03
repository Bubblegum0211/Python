"""9-6
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
    def describe_restaurant(self):
        print(f"Restaurant'name is {self.restaurant_name}")
        print(f"Restaurant'type is {self.cuisine_type}")
    def open_restaurant(self):
        print("正在营业")
    def set_number_served(self,number_served):
        self.number_served=number_served
    def read_number_served(self):
        print(f"{self.number_served}")
    def increment_number_served(self,number_served):
        self.number_served+=number_served

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors=['a','b','c','d']
    def read_flavors(self):
        print(f"{self.flavors}")

icecream=IceCreamStand('蜜雪冰城','冰淇淋')
icecream.read_flavors()"""

#9-8
class User:
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.login_attempts=0
    def describe_user(self):
        print(f"first_name:{self.first_name},last_name:{self.last_name},age:{self.age}")
    def greet_user(self):
        print(f"Hello,{self.first_name}{self.last_name}!")
    def increment_login_attempts(self):
        self.login_attempts+=1
    def reset_login_attempts(self):
        self.login_attempts=0
    def read_loginattempts(self):
        print(f"{self.login_attempts}")

class Admin(User):
    def __init__(self,first_name,last_name,age):
        super().__init__(first_name,last_name,age)
        self.privileges=Privileges()

class Privileges:
    def __init__(self):
        self.privileges=["can add post","can delete post","can ban user"]
    def show_privileges(self):
        print(f"{self.privileges}")

admin=Admin('Tom','Alex','20')
admin.privileges.show_privileges()