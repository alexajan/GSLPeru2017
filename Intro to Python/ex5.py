# SOLUTIONS Ex. 5


class Restaurant():
    """Create a listing of a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Add description of the restaurant."""
        print("Name: " + self.restaurant_name.title())
        print("Cuisine: " + self.cuisine_type)

    def open_restaurant(self):
        """Tell customers that the restaurant is open."""
        print("The restaurant is open!")

my_restaurant = Restaurant("Ceviche", "Peruvian seafood")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
