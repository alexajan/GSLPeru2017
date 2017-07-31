# VARIABLES AND DATA TYPES

# Print "Hello, World!"

print("Hello, world!")
message = "Hello, world!"
print(message)
message = "Hola, mundo!"
print(message)

# Understanding errors

# Error: print mesage

# Strings

print("It's a string")
print('This is also a string')

first_name = 'alexa'
last_name = 'jan'
print(len(last_name))
first_name = first_name.upper()
first_name = first_name.title()
first_name = first_name.lower()
print("Hello " + first_name + " " + last_name)

msg = "bienvenidos"
print(msg[::2])

# Numbers

print(3 + 3 / 2 - 1 * 0)
print(3 ** 2)

# LISTS

# Accessing elements

menu = ["pizza", "spaghetti", "burger"]
print(menu[1].title())
print(menu)

# Adding items

menu.append("salad")
menu.insert(0, "soup")
print(menu)

# Deleting items
del menu[1]
menu.remove("soup")
popped = menu.pop()
print(menu)
print(popped)

# Sorting items
menu.sort(reverse=False)
print(menu)
# Error: print(menu[10])

# Working with lists
appliances = ["magic toaster", "rainbow oven", "unicorn fridge"]
for appliance in appliances:
    print("I am a " + appliance)

num_list = []
for index in range(1, 5):
    num_list.append(index)
    print(num_list)
print(sum(num_list))
print(max(num_list))

# Tuples
tuple_ex = (999, 1000)
# Error: tuple_ex[0] = 0
for num in tuple_ex:
    print("My favorite number is " + str(num))

# Ex. 1 With a for loop, make a list of multiples of 3 from 3 to 30 and print the list and the numbers in the list.
import ex1

# IF STATEMENTS

age = 16
name = "John"
if age == 16 and name.lower() == "john":
    print(name.title() + " is " + str(age))

if age == 16 or name.lower() == "steven":
    print(name.title() + " is " + str(age))

if "h" in name:
    print("h is in the name!")

appliances = ['magic_toaster', 'rainbow_oven', 'unicorn_fridge']
for appliance in appliances:
    if appliance == "magic_toaster":
        print(appliance.upper())
    elif appliance != "rainbow_oven":
        print(appliance.title())
    else:
        print(appliance)

# DICTIONARIES

# Creating them
my_car = {'color': 'turquoise', 'brand': 'bmw'}
print(my_car['color'])

my_car['year'] = 2017
my_car['color'] = 'gold'
print(my_car)
del my_car['year']
print(my_car)

# Looping through the key-value pairs
car_dealership = {'rolls-royce': 2012, 'honda': 2002, 'mercedes': 2017}
car_database = []
for key, value in car_dealership.items():
    car_database.append(key + ": " + str(value))

print(car_database)

# Ex. 2 Create a glossary. Think of 5 programming terms, like tuple and print, and store them as keys in your glossary
# with their meanings as values. Then, print each word and meaning in a neatly formatted output. You can use the
# newline character "\n" to insert a blank line between each word-meaning pair.
import ex2

# USER INPUT AND WHILE LOOPS

# User input
height = input("How tall are you in inches? ")
if int(height) >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

# Modulo
user_num = input("Enter a number, and I'll tell you if it's even or odd: ")
if int(user_num) % 2 == 0:
    print("\nThe number " + str(user_num) + " is even.")
else:
    print("\nThe number " + str(user_num) + " is odd.")

# While loops
index = 1
while index <= 5:
    print(index)
    index += 1

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("Added " + city.title() + " to your travel log!")

# Ex. 3 Make a list called pizza_orders and fill it with the names of various pizzas. Then make an empty dictionary
# called finished_pizzas. Loop through the list of pizza orders and print a message for each order. As each pizza is
# made, move it to the dictionary of finished pizzas. After all sandwiches have been made, print a message listing each
# sandwich made.
import ex3

# FUNCTIONS


def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()

# Arguments


def greet_custom_user(username):
    """Display a custom greeting."""
    print("Hello, " + username.title() + "!")

greet_custom_user('alexa')


def describe_pet(pet_name, animal_type='zebra'):
    """Display info about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='henry')
describe_pet('carl', 'giraffe')
describe_pet('giraffe', 'carl')
describe_pet(animal_type='giraffe', pet_name='carl')

# Return values


def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
        return full_name.title()
    else:
        full_name = first_name + ' ' + last_name
        return full_name.title()

politician_1 = get_formatted_name('michelle', 'bachelet')
politician_2 = get_formatted_name('pEdro', 'kucZynsKi', 'paBlo')
print(politician_1)
print(politician_2)

# Passing an arbitrary number of arguments

def make_sandwiches(size, *condiments):
    """Print the list of condiments that have been requested."""
    print("\nMaking a " + str(size) + "-inch sandwich with the following condiments:")
    for condiment in condiments:
        print("- "  + condiment)

make_sandwiches(16, 'salami', 'lettuce', 'cheese')

# Ex. 4 Make a list of king's names. Pass the list to a function called show_kings(), which prints the name of each
# king in the list. Next, write a function called make_great() that modifies the list of kings by adding 'the Great'
# to each king's name. Call show_kings() to see that the list has actually been modified.
import ex4

# CLASSES

# Creating a class


class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        # self is a reference to the instance
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is sitting.")

    def roll_over(self):
        """Simulate a dog rolling over"""
        print(self.name.title() + " rolled over!")

my_dog = Dog("Buddy", 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()

# Ex. 5 Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant
#_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, and
# a method called open_restaurant() that prints a message indicating that the restaurant is open. Then, make an
# instance called restaurant from your class. Print the two attributes individually, and then call both methods.
import ex5

# Inheritance


class Husky(Dog):
    """Creating a type of dog with similar attributes"""
    def __init__(self, name, age):
        """Initialize attributes of the parent class."""
        super().__init__(name, age)
        self.eye_color = 'jade'

    def describe_husky(self):
        """Talk about the husky."""
        print("This is my beautiful husky named " + self.name.title() + " who is " + str(self.age) +
              " years old and has " + self.eye_color + " eyes.")

my_husky = Husky('Alaskan princess', 2)
my_husky.describe_husky()
my_husky.eye_color = 'aqua'
my_husky.describe_husky()

# Ex. 6 Starbucks is a type of restaurant. Write a class called Starbucks that inherits from the Restaurant class that
# you wrote earlier. Add an attribute called drinks that stores a list of types of drinks. Write a method that displays
# these flavors. Create an instance of Starbucks, call this method, and call describe_restaurant.
import ex6










