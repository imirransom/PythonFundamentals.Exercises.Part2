""" 
This function takes a parameter for a name and 
will then print it out
"""


def greet(name):
    print(f"Hello, {name}. Welcome to Zip Code!")


"""
This function will print out the name provided
"""

def name_input():
    return input("Please provide your name: ")

user_name = name_input
greet(user_name)