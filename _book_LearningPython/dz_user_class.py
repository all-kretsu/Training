# home lesson


# exercise 02 User class
class Users:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login = None

    def describe_user(self):
        print(f'The user name is {self.first_name} {self.last_name}!')

    def greet_user(self):
        print(f'Hello {self.first_name} {self.last_name}!')

    login_attempts = 0

    def increment_login_attempts(self):
        if True:
            self.login_attempts += 1
            print(f'Current login attempts: {self.login_attempts}')

    def reset_login_attempts(self):
        if True:
            self.login_attempts = 0
            print('Current number of login attempts has been reset.')
            print(f'Login attempts: {self.login_attempts}')


user_1 = Users('Alex', 'Cretu')
user_2 = Users('Jane', 'Cretu')

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.reset_login_attempts()
