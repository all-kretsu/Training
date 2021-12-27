# home lesson


# exercise 01 Restaurant classes
class Restaurant:
    def __init__(self, rest_name, cuisine_type):
        # rest mean - restaurant
        self.rest_name = rest_name
        self.cuisine_type = cuisine_type
        self.new_guest = None
        self.guests = None

    def describe_rest(self):
        print(f'Restaurant {self.rest_name} have {self.cuisine_type}.')

    def open_rest(self):
        print(f'Restaurant {self.rest_name} is open.')

    def set_number_served(self, guests):
        self.guests = guests
        print(f'Number of served persons: {guests}.')

    def increment_number_served(self, new_guests):
        self.new_guest = new_guests
        self.guests += self.new_guest
        print(f'Number of served persons: {self.guests}.')


chinese_rest = Restaurant('Red Dragon', 'chinese cuisine')
italian_rest = Restaurant('Napoli', 'italian cuisine')
mexican_rest = Restaurant('Amigos', 'mexican cuisine')
chinese_rest.describe_rest()
chinese_rest.open_rest()
italian_rest.describe_rest()
italian_rest.open_rest()
chinese_rest.set_number_served(5)
chinese_rest.increment_number_served(8)
