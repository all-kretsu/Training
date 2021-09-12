friends_list = []

def add_friend():
    friends_number = int(input('How many friends will be in your birthday?'))
    for friends in range(friends_number):
        friends = input('Insert friend name:\n')
        friends_list.append(friends)

add_friend()

print(friends_list)

press_key = input('Press Y if you want to add new friend:\nPress W if you want to see the friends lists:\n')


if press_key == 'Y':
    add_friend()
else:
    print(friends_list)
