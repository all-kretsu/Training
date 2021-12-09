# 01 Using list in function
def user_list(names):
    for name in names:
        msg = f'Hello, {name.title()}!'
        print(msg)

usernames = ['Ivan', 'Hannah']
user_list(usernames)

# 02 Change list in function
# if need to deny deleting of list elements, add [:] at the end of arg
# example 
# def print_models(unprinted_designs[:], completed_models):

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        curent_models = unprinted_designs.pop()
        print(f'\nPrint a {curent_models}')
        completed_models.append(curent_models)

def show_models():
    print('\nThe following models have been printed!')
    for model in completed_models:
        print(model)

unprinted_designs = ['robot', 'phone', 'dynosaur']
completed_models = []

print_models(unprinted_designs, completed_models)
show_models()

# 03 add random number of arguments into the function
def make_pizza(*toppings):
    for topping in toppings:
        print(f'- {topping}')

make_pizza('mushrooms', 'tomatoes', 'peppers', 'meat')

