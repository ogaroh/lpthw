# more variables anf string formatting

name = 'Erick Ogaro'
age = 21
height = 190 # centimetres
weight = 76 # kilograms
eyes = 'brown'
teeth = 'White'
hair = 'black'

print(f"My name is {name}.")
print(f"I'm {height} centimetres tall.")
print(f"I'm {weight} kilograms heavy.")
print("Actually that's not really heavy.")
print(f"I have {eyes} eyes and {hair} hair.")
print(f"My teeth are usually {teeth}, depending on the coffee.")

# this liine is tricky, try to get it right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight}, I'll get {total}.")