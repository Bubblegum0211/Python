import random
'''9-13
class Die:
    def __init__(self,sides='6'):
        self.sides=sides
    def roll_die(self):
        i = 0
        if i <= 10:
            for n in range(10):
                print(random.randint(1,int(self.sides)))
                i += 1

die=Die()
die.roll_die()
die=Die(10)
die.roll_die()'''

#9-14 9-15
lists=list(range(10))+['a','b','c','d','e']
n=1
while True:
    win_number=random.sample(lists,k=4)
    '''print(f"If your number is {win_number},you win the lottery!")'''
    my_ticket=random.choices(lists,k=4)
    if win_number != my_ticket:
        n+=1
        continue
    else:
        print(f"It takes you {n} times to win the lottery")
        break