import os

pathie = "C:/Users/ASUS/Desktop/pp2"

dir = [d for d in os.listdir(pathie) if os.path.isdir(os.path.join(pathie, d))]

files = [f for f in os.listdir(pathie) if os.path.isfile(os.path.join(pathie, f))]

all = os.listdir(pathie)

print("directories: ", dir)
print("files:", files)
print("all items:", all)


'''
dirs = os.listdir(pathie)
for dir in dirs:
print(dir)
print("isdir", os.path.isdir(pathie))
print("isfile", os.path.isfile(pathie))
print("---")
'''



'''
print(os.getcwd()) # returns current working directory


print(os.listdir()) # list everything in the current dir
'''


'''
path_to = "../builtin/"

print(os.listdir(path_to))

'''