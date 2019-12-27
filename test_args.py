from sys import argv

script_name, first_name, last_name = argv

yob = int(input("When were you born? "))
age = 2020 - yob

print("Your full name is ", first_name, last_name, " and you're approximately ", int(age), " years old.")