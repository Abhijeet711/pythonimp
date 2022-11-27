import os
import glob

dir_name = ""

list_of_files = filter(os.path.isfile, glob.glob(dir_name + "*"))

max_file = max(list_of_files, key = lambda x: os.stat(x).st_size)

print("Max Sized File: ", max_file)
print("Max File size in bytes: ", os.stat(max_file).st_size)
