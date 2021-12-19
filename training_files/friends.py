

def friends_num():
    friends_number = None
    while True:
        try:
            friends_number = int(input('How many friends will be in your birthday?'))
            break
        except ValueError:
            print('Enter int please!')

def add_friend():
    for friends in range (1):
        friends = input('Insert friend name:\n')
        friend_list = []
        friend_list.append(friends)

add_friend()