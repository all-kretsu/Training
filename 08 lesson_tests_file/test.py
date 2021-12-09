# test file for use new knowns
# file is script for use in cooking 
import json
import os

from input_list import input_list as in_list

# empty lists
ingredients = []
quantity = []
dish = []

# function for calling commands
def command_func(args):
    print('\nInsert the command: ')
    # adding to ingredients
    if args == 'i':
        while len(ingredients) != 3:
            in_list('\nInsert ingredients: ')
            ingredients.append(in_list)
    # adding to quantity
    elif args == 'q':
        in_list('\nInsert quantity: ')
        quantity.append(in_list)
    # export to byte
    elif args == 'ex':
        os.mkdir('cooking')
        with open('ingredints.txt', 'w', encoding= 'utf-8') as f:
            json.dump(f('\n Ingredients: {}'.format(ingredients)),
                        '\n Quantity: {}'.format(quantity), f)

command_func('i')
