#5-8
name_lists = ['admin','Jaden','Tom','Ben','Bob']
for user in name_lists:
    if user == 'admin':
        print(f"Hello admin,would you like to see a status report?")
    elif user in name_lists:
        print(f"Hello {user},thank you for logging in again.")
print("\t")

#5-9
name_lists = []
if len(name_lists) == 0:
    print("We need to find some users!")
print("\t")

#5-10
current_users = ['Admin','bob','tom','ben','jack']
new_users = ['admin','Bob','mary','Alice','bess']
for new_user in new_users:
    if new_user.lower() in [current_user.lower() for current_user in current_users]:
        print("该用户名已存在。")
    else:
        print("该用户名可使用。")
print("\t")

#5-11
nums = list(range(1,10))
for num in nums:
    if num == 1:
        print("1st")
    elif num == 2:
        print("2nd")
    elif num == 3:
        print("3rd")
    else:
        print(f"{num}th")