print('Let\'s practice everything\n\t that we\'ve learned. About escapes with the \\ character.')

poem = """\tRoses are red,\n\tViolets are blue,\n\tSugar is sweet,\n\tAnd so are you..."""
breaker = '----------------------------'

print(f"{breaker}\n{poem}\n{breaker}")

answer = 10 - 2 + 3 - 6

print("The answer is: {}".format(answer))


def secret_formula(starting_point):
    jelly_beans = starting_point * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


starting_point = 10000
beans, jars, crates = secret_formula(starting_point)


print(
    f"""With a starting point of {starting_point}:
        we'd have {beans} jelly beans, {jars} jars and {crates} crates.""")

# different way to format the strings (using a formula)
start_point = starting_point / 10
print(
    f"Alternative way of doing this, using {start_point} as the starting point.")

formula = secret_formula(start_point)

print("We'd have {} beans, {} jars and {} crates.".format(*formula))
