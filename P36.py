#3-4
lists = ['jack','mary','tom']
print(f"Welcome,{lists[0].title()}.")
print(f"Welcome,{lists[1].title()}.")
print(f"Welcome,{lists[2].title()}.")
print(len(lists))
print("\t")

#3-5
print(f"Sorry,{lists[2].title()} can't come here.")
lists[2] = 'ben'
print(f"Welcome,{lists[0].title()}.")
print(f"Welcome,{lists[1].title()}.")
print(f"Welcome,{lists[2].title()}.")
print(len(lists))
print("\t")

#3-6
print("I found a bigger table.")
lists.insert(0,'bill')
lists.insert(2,'bob')
lists.append('mark')
print(f"Welcome,{lists[0].title()}.")
print(f"Welcome,{lists[1].title()}.")
print(f"Welcome,{lists[2].title()}.")
print(f"Welcome,{lists[3].title()}.")
print(f"Welcome,{lists[4].title()}.")
print(f"Welcome,{lists[5].title()}.")
print(len(lists))
print("\t")

#3-7
print("Sorry,I can only invite two people to come here")
one = lists.pop(0)
print(f"Sorry,{one.title()}.")
two = lists.pop(0)
print(f"Sorry,{two.title()}.")
three = lists.pop(0)
print(f"Sorry,{three.title()}.")
four = lists.pop(0)
print(f"Sorry,{four.title()}.")
print(f"Welcome,{lists[0].title()},you can come here.")
print(f"Welcome,{lists[1].title()},you can come here.")
del lists[0]
del lists[0]
print(lists)
print(len(lists))