from sys import argv
 
# uses argv to get file names --> method 1 
script_name, filename = argv

# creates the file object so that you can read or write to it
txt = open(filename)

print(f"here is your {filename} file.")

# shows the contents of the file specified
print(txt.read())

# requires user to manually enter the file name --> method 2
filename_again = input("Enter your file name: \n\t>>> ")

# open the file specified
txtfile_again = open(filename_again)

# prints out the contents of the file specified
print(txtfile_again.read())