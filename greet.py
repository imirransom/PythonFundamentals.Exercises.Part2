""" 
This function takes a parameter for a name and 
will then print it out
"""


def greet(name):
    print(f"Hello, {name}. Welcome to Zip Code!")

def name_input():
    input("Please provide your name: ")
    

name = name_input()


greet(name)