# 01 Using list in function

def user_list(names):
    for name in names:
        msg = f'Hello, {name.title()}!'
        print(msg)

usernames = ['Ivan', 'Hannah']
user_list(usernames)

