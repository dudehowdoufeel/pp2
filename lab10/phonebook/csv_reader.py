import csv
filename = r'C:\Users\ASUS\Desktop\pp2\lab10\phonebook\book.cvs'
with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        surname, name, number = row
        print(surname, name, number)