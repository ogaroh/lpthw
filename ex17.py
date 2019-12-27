from sys import argv; from os.path import exists
script, from_file, to_file  = argv; in_data = open(from_file).read()
print(f"--------------------------------\nThe input file is {len(in_data)} bytes long.\nDoes the output file exist? {exists(to_file)}")
open(to_file, 'w').write(in_data)
print("Done. Finished copying.\n--------------------------------")