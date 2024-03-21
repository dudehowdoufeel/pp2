import os

def copy(source_path, destination_path):
    with open(source_path, 'r') as source, open(destination_path, 'w') as dest:
        dest.write(source.read())


pathie = "C:/Users/ASUS/Desktop/pp"

os.remove("2.txt")

print(os.path.exists("2.txt"))