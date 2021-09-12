
def but():

    button = None

    while button == None:
        button = input('Do you want to insert friend?\nPress Y/N: ')
        button = button.lower()
        # some operations
        if button == 'y':
            friends = input('Insert friend name:\n')
            list = []
            list.append(friends)
            break
        elif button == 'n':
            print('End program.')
            break     
        else:
            button = None

but()