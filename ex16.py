from sys import argv

script_name, filename = argv
print(f"We are going to erase {filename}. ")
print("If you din't want that, hit CTRL-C (^C).")
print("If you want that, hit RETURN.")

input('>> ')

print("Opening file...")
target = open(filename, 'w')

print("Truncating the file. Bye!")
target.truncate()

print("Now I'm going to ask you for three lines.")
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")
print("Writing the lines above to the target file.")

target.write(f"{line1}\n{line2}\n{line3}\n") # escapes and formatters instead of multiple lines

print("And finally we close the file.")
target.close()