filename = "sample.txt"

try:
    with open(filename, 'r') as file:
        lines = file.readlines()
        print(f"{filename} has {len(lines)} lines.")
except FileNotFoundError:
    print("File not found.")
