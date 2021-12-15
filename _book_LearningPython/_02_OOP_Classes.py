# learning classes
# fundamental examples

# creating Dog class 
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sit(self):
        print(f'{self.name} sit down.')
    
    def roll_over(self):
        print(f'{self.name} rolled over.')

my_dog = Dog('willie', 6)

print(f'My dogs name is {my_dog.name}, he is {my_dog.age} years old')

# creating class of cars
class Car():
    def __init__(self, name, year):
        self.name = name
        self.year = year
    def speed(self):
        print(f'The name of car is {self.name}, the speed of it is {self.speed}')
     



        
        
