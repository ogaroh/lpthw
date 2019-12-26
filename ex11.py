# PS :
# this exercise combines effort from ex12 too, which means:
# i'll skip it because it's basically the same shit

name = input("What's your name? ")
age = int(input("How about your age? "))
height = float(input("How tall are you? (Centimeters) "))
weight = float(input("How much do you weigh? (Kilograms) "))

print("." * 60, "\n")
print(f"So, here's what I've gathered: \n\t* Your name is {name}.\n\t* You are {age} years old.\n\t* Your height is {height} cm and you weigh {weight} Kg.\n")
print("." * 60)