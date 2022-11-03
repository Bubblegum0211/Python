"""9-1
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print(f"Restaurant'name is {self.restaurant_name}")
        print(f"Restaurant'type is {self.cuisine_type}")
    def open_restaurant(self):
        print("正在营业")
my_restaurant=Restaurant("1","中餐")
print(f"{my_restaurant.restaurant_name}")
print(f"{my_restaurant.cuisine_type}")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

9-2
my_restaurant1=Restaurant("1","中餐")
my_restaurant2=Restaurant("2","西餐")
my_restaurant3=Restaurant("3","法餐")
my_restaurant1.describe_restaurant()
my_restaurant2.describe_restaurant()
my_restaurant3.describe_restaurant()"""

#9-3
class User:
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    def describe_user(self):
        print(f"first_name:{self.first_name},last_name:{self.last_name},age:{self.age}")
    def greet_user(self):
        print(f"Hello,{self.first_name}{self.last_name}!")

user1=User("Tom","Alex","20")
user2=User("Bob","Alex","22")
user3=User("Ben","Alex","19")
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()