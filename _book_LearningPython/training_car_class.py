# training file
# about classes

class Car():
    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        long_name = f'{self.year} {self.manufacturer} {self.model}'
        return long_name.title()

    def read_odometer(self):
        print(f'This car has {self.odometer} kilometers on it.')
    
    def update_odometer(self, mileage):
        self.odometer = mileage
        if mileage >= :
            
            
        

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(60)
my_new_car.read_odometer()

