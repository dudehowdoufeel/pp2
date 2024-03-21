import os

pathie = "C:/Users/ASUS/Desktop/pp"

def create():
    for i in range(65, 91):  # ASCII codes from A to Z
        with open(f"{chr(i)}.txt", 'w') as file:
            file.write(chr(i))

os.mkdir(pathie)

for i in range(1,27):
    file = open(f"{pathie}{i}.txt", "w")
    file.close()