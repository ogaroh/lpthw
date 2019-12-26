from sys import argv
 
# uses argv to get file names --> method 1 
script_name, filename = argv

# open the file specified
txt = open(filename)

print(f"here is your {filename} file.")

# prints out the contents of the file specified
print(txt.read())

# requires user to manually enter the file name --> method 2
filename_again = input("Enter your file name: \n\t>>> ")

# open the file specified
txtfile_again = open(filename_again)

# prints out the contents of the file specified
print(txtfile_again.read())