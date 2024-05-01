#Implement procedure to deleting data from tables by username or phone

import csv
import psycopg2

conn = psycopg2.connect(
    host='localhost', 
    dbname='phonebook', 
    user='postgres', 
    password='tokaw25155'
)

cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS PhoneBook")

cur.execute("""CREATE TABLE IF NOT EXISTS PhoneBook (
    surname VARCHAR(255),
    name VARCHAR(255),
    number VARCHAR(20)
);
""")

def update(surname, mode, new_value):
    cur.execute("""
    UPDATE PhoneBook
    SET {} = %s
    WHERE surname = %s
    """.format(mode), (new_value, surname))

def delete_by_username(surname):
    cur.execute("""
    DELETE FROM PhoneBook
    WHERE surname = %s
    """, (surname,))

def delete_by_phone(number):
    cur.execute("""
    DELETE FROM PhoneBook
    WHERE number = %s
    """, (number,))

# insert
while True:
    print("Type 'enter' if you want to add more data and type 'stop' to break")
    mode = input()
    if mode == "stop":
        break
    new_data = []
    print("Enter surname:")
    new_data.append(input())
    print("Enter name:")
    new_data.append(input())
    print("Enter number:")
    new_data.append(input())
    cur.execute("""
    INSERT INTO PhoneBook (surname, name, number)
    VALUES (%s, %s, %s)
    """, tuple(new_data))

# insert from csv
while True:
    print("Want to insert data from csv file? yes/no:")
    mode = input()
    if mode == "no":
        break
    elif mode == "yes":
        filename = r'C:\Users\ASUS\Desktop\pp2\lab10\phonebook\book.cvs'
        with open(filename, "r") as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            for row in csvreader:
                cur.execute("INSERT INTO PhoneBook VALUES (%s,%s,%s)", row)
        print("Data inserted successfully from CSV file.")
        break  
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

# update
while True:
    print("Type 'update' to update some data or 'stop' to break")
    mode = input()
    if mode == "stop":
        break
    cur.execute("""SELECT * FROM PhoneBook""")
    print(cur.fetchall())
    print("Enter surname:")
    surname = input()
    print("What do you want to change? name/number:")
    field = input()
    print("Enter new {}:".format(field))
    new_value = input()
    update(surname, field, new_value)

# delete
while True:
    print("Want to delete some data? yes/no")
    mode = input()
    if mode == "no":
        break
    print("Delete by surname or number? (surname/number):")
    delete_mode = input()
    if delete_mode == "surname":
        print("Enter surname:")
        surname = input()
        delete_by_username(surname)
    elif delete_mode == "number":
        print("Enter number:")
        number = input()
        delete_by_phone(number)
    else:
        print("Invalid input. Please enter 'surname' or 'number'.")

conn.commit()
cur.close()
conn.close()
