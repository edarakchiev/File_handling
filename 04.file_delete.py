import os
try:
    os.remove("my_first_file.txt")
    print("File already deleted!")
except FileNotFoundError:
    print("File not found")