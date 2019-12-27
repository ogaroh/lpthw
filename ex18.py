#  functions, functions, functions 😈
'''
Functions, functions, functions... 😈
    The simplest way to explain functions is that:
    they use variables, take arguments and combine the two to help you right your own `mini-scripts`.
    You're welcome. (use the keyword `def` to `define` the function)
'''

# you can do this...
def print_two(*args): 
    arg1, arg2 = args
    print(f"---------------------------\nArg 1: {arg1}\nArg 2: {arg2}")

# or this... (the previous *args was kinda pointless)
def print_two_again(arg1, arg2):
    print(f"Arg 1: {arg1}\nArg 2: {arg2}")

# takes only one argument
def print_one(arg):
    print(f"Argument: {arg}")

# takes no argument(s)
def print_none():
    print("I got nothing 😐\n---------------------------")

# calling the functions / putting them to use
print_two("Erick", 22)
print_two_again("Ogaro", "Nairobi")
print_one("One")
print_none()