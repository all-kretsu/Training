
def but():
    button = input('You want to insert friend?\nPress Y/N: ')
    button = button.lower()

but()

while but().__class__ == str and int:
    if but() == 'y':
        from friends import add_friend
        add_friend()
    elif but() == 'y':
        print('End program.')
        break     
    else:
        but()
