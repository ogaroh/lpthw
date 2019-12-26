from sys import argv

script_name, user = argv

input_prompt = ">>> "

print(f"Hi {user}, I'm the {script_name} Python Script. ")
print("I'd like to ask you a few questions.")

# interaction with the user
print(f"Do you like computers, {user}? ")
likes = input(input_prompt)

print(f"Where do you live, {user}? ")
lives = input(input_prompt)

print("And what computer do you have? 👀")
computer_type = input(input_prompt)

print(f"""
Alrightie then, {user}. You said {likes} about liking computers.
You live in {lives}, not sure where that is. 🤔
And that you have a {computer_type} computer. Nice!
""")
