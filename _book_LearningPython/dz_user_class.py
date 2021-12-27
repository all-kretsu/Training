# home lesson


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
