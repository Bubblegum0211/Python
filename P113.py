'''7-8
sandwich_orders=['1','2','3']
finished_sandwiches=[]
for sandwich in sandwich_orders:
    finished_sandwiches.append(sandwich)
    print(f"I made {sandwich} sandwich.")
'''

'''7-9
print("Sorry,c is over.")
sandwich_orders=['a','b','c','c','c']
while 'c' in sandwich_orders:
    sandwich_orders.remove('c')
print(sandwich_orders)
'''

#7-10
active = True
places = []
while active:
    ask=input("If you could visit one place in the world,where would you go?")
    places.append(ask)
    tuichu=input("是否退出程序？(yes/no)")
    if tuichu == 'yes':
        active =False
for place in places:
    print(f"{place}")