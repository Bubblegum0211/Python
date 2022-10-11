'''5-3 通过
Alien_color = "green"
if Alien_color == "green":
    print("You get 5 points.")

# 未通过
Alien_color = "green"
if Alien_color == "red":
    print("You get 5 points.")

#5-4 if版本
Alien_color = "green"
if Alien_color == "green":
    print("You get 5 points.")
else:
    print("You get 10 points.")

# else版本
Alien_color = "green"
if Alien_color == "red":
    print("You get 10 points.")
else:
    print("You get 5 points.")

#5-5 绿色外星人
Alien_color = "green"
if Alien_color == "green":
    print("You get 5 points.")
elif Alien_color == "yellow":
    print("You get 10 points.")
elif Alien_color == "red":
    print("You get 15 points.")

# 黄色外星人
Alien_color = "green"
if Alien_color == "yellow":
    print("You get 5 points.")
elif Alien_color == "yellow":
    print("You get 10 points.")
elif Alien_color == "red":
    print("You get 15 points.")

# 红色外星人
Alien_color = "red"
if Alien_color == "green":
    print("You get 5 points.")
elif Alien_color == "yellow":
    print("You get 10 points.")
elif Alien_color == "red":
    print("You get 15 points.")
'''

'''
#5-6
age = int(input())
if age < 2:
    print("这个人是婴儿。")
elif 2 <= age < 4:
    print("这个人是幼儿。")
elif 4 <= age < 13:
    print("这个人是儿童。")
elif 13 <= age < 20:
    print("这个人是青少年。")
elif 20 <= age < 65:
    print("这个人是成年人。")
elif age >= 65:
    print("这个人是老年人。")
'''

#5-7
favorite_fruits = ['watermelons','apples','bananas','grapes','pears']
if 'bananas' in favorite_fruits:
    if 'apples' in favorite_fruits:
        if 'watermelons' in favorite_fruits:
            if 'pears' in favorite_fruits:
                if 'grapes' in favorite_fruits:
                    print("You really like bananas!")