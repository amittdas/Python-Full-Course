# Decorator is a function that takes a function, then it creates a new function called Wrapper(); then it returns the new (wrapper) function

def decorator(func):
    def wrapper():
        print("Hey! I am about to execute a function...")
        func()
        print("I have executed this function...")
    return wrapper

def say_hello():
    print("Hello !")

f = decorator(say_hello)
f()

# This method is not really in use, we have a better way to write decorators