"""9-4
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
restaurant=Restaurant("1","中餐")
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(23)
restaurant.increment_number_served(100)
restaurant.read_number_served()"""

#9-5
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

user1=User("Tom","Alex","20")
user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.read_loginattempts()

user1.reset_login_attempts()
user1.read_loginattempts()