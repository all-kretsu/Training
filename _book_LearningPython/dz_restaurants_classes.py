# home lesson


# exercise 01 Restaurant classes
class Restaurant:
    def __init__(self, rest_name, cuisine_type):
        # rest mean - restaurant
        self.rest_name = rest_name
        self.cuisine_type = cuisine_type

    def describe_rest(self):
        print(f'Restaurant {self.rest_name} have {self.cuisine_type}.')

    def open_rest(self):
        print(f'Restaurant {self.rest_name} is open.')


chinese_rest = Restaurant('Red Dragon', 'chinese cuisine')
italian_rest = Restaurant('Napoli', 'italian cuisine')
mexican_rest = Restaurant('Amigos', 'mexican cuisine')

# print(chinese_rest.rest_name)
chinese_rest.describe_rest()
chinese_rest.open_rest()

italian_rest.describe_rest()
italian_rest.open_rest()


# exercise 02 User class
class Users:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f'The user name is {self.first_name} {self.last_name}!')

    def greet_user(self):
        print(f'Hello {self.first_name} {self.last_name}!')


user_1 = Users('Alex', 'Cretu')
user_2 = Users('Jane', 'Cretu')

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()
