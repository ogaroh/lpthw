# functions that actually return something


def add(a, b):
    print(f"ADDING {a} + {b}.")
    return a + b


def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}.")
    return a - b


def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}.")
    return a * b


def divide(a, b):
    print(f"DIVIDING {a} / {b}.")
    return a / b


def remainder(a, b):
    print(f"REMAINDER or MODULUS of {a} / {b}")
    return a % b


# calling the functions
print("Let's do some math here.")

age = add(11, 11)
height = subtract(200, 10)
weight = multiply(25, 3)
iq = divide(1000, 4)

print(f"AGE: {age}, HEIGHT: {weight}, HEIGHT: {height}, IQ: {iq}")

#  math (nested)
what = add(age, subtract(height, multiply(weight, divide(iq, 2)))) # doea the arithmetic 'inside-out'

print(f"That becomes {what}. Can you do it by hand? ")
