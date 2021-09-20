import random
number = random.randint(1, 100)

print("Hi! Can u guess a number?")
print("Print 'prompt' if you want to take a prompt!")
print("You have 4 chance for guess, good luck!")

user_answer = None

#the game
def game():

    while True: # if answer != int
        try:
            user_answer = int(input("Your answer is:\n"))
            break
        except ValueError:
                print('Enter int please!')
    
    for i in reversed(range(3)):

        if user_answer != number:
            print("No, its not!")
            
            if i == (2): # prompt for game
                print("The prompt!")
                if number < 50:  
                    print ("Its more than 50!")
                else:
                    print("Its less than 50!")

            print("You have {} chance!".format(i+1))
            user_answer = input("Try again:\n")
            if i == 0:
                print("True number is: {}!".format(number))
                break
            continue
        else:
            print("Yes, its right!")
            break

game()

new_game = None
while new_game == None: #offer to play again
        new_game = input('Do you want to play again?\nPress Y/N: ')
        new_game = new_game.lower()
        # some operations
        if new_game == 'y':
            number = random.randint(1, 100)
            game()
    
        elif new_game == 'n':
            print('Ok..Good Bye!')
            break
        else:
            new_game = None


