# more files
from sys import argv
from os.path import exists
 
script, from_file, to_file  = argv

# in_file = open(from_file)
# in_data = in_file.read()

# option B
in_data = open(from_file).read() # check if it's valid

print(f"--------------------------------\nThe input file is {len(in_data)} bytes long.")

print(f"Does the output file exist? {exists(to_file)}")
input("READY... hit RETURN to continue to the copy operation, or CTRL-C to abort.\n>>>")

out_file = open(to_file, 'w')
out_file.write(in_data)

print("Done. Finished copying.\n--------------------------------")
out_file.close()

# in_file.close() # - because it's not in use