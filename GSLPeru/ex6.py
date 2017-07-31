# SOLUTIONS Ex. 6


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


class Starbucks(Restaurant):
    """Define a type of restaurant: Starbucks"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize Restaurant attributes"""
        super().__init__(restaurant_name, cuisine_type)
        self.drinks = ['cappuccino', 'coffee', 'macchiato']

    def display_drinks(self):
        print("Menu:")
        for drink in self.drinks:
            print(drink)

san_francisco_loc = Starbucks("San Francisco Starbucks", "Cafe")
san_francisco_loc.describe_restaurant()
san_francisco_loc.display_drinks()
