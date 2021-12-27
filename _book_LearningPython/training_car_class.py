# training file
# about classes

class Car:
    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer = 6

    def get_descriptive_name(self):
        long_name = f'{self.year} {self.manufacturer} {self.model}'
        return long_name.title()

    def read_odometer(self):
        print(f'This car has {self.odometer} kilometers on it.')

    def update_odometer(self, mileage):
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print('You cant roll back an odometer!')

    def increment_odometer(self, kilometers):
        self.odometer += kilometers


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(100)
my_new_car.read_odometer()
my_new_car.increment_odometer(100)
my_new_car.read_odometer()
