# more functions

def cheese_and_crackers(cheese, crackers):
    print(f"You have {cheese} cheese and {crackers} crackers.\nLet's the party get started!!")

# direct assignment
cheese_and_crackers(40, 50)

#  or use variables
cheese_amt = 100
crackers_amt = 250
cheese_and_crackers(cheese_amt, crackers_amt)

#  or even do some math inside
cheese_and_crackers(cheese_amt + 50, crackers_amt * 10)

#  values from user input
user_cheese = int(input("How many cheese packs do you have? "))
user_crackers = int(input("How about the crackers? "))

cheese_and_crackers(user_cheese, user_crackers)