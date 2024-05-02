#Function that returns all records based on a pattern (example of pattern: part of name, surname, phone number)

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


def update(surname, mode, new_name):
    cur.execute("""UPDATE PhoneBook
    SET {} = '{}'
    WHERE surname = '{}'
    """.format(mode,new_name,surname))

def delete(surname):
    cur.execute("""DELETE FROM PhoneBook
    WHERE surname='{}'
    """.format(surname))

def search_records(pattern):
    cur.execute("""SELECT * FROM PhoneBook
                   WHERE surname LIKE %s OR name LIKE %s OR number LIKE %s""",
                   (f'%{pattern}%', f'%{pattern}%', f'%{pattern}%'))
    records = cur.fetchall()
    return records


#insert
mode="enter"
while True:
    print("Type 'enter' if you want to add more data and type 'stop' to break")
    mode=input()
    if mode=="stop":
        break
    new=[]
    print("enter surname:")
    new.append(input())
    print("enter name:")
    new.append(input())
    print("enter number:")
    new.append(input())
    new=tuple(new)
    cur.execute("""INSERT INTO PhoneBook (surname, name ,number) VALUES
    {};
    """.format(new))


#insert from csv

while True:
    print("Want to insert data from csv file? yes/no:")
    mode=input()
    if mode=="no":
        break
    elif mode=="yes":
        filename = r'C:\Users\ASUS\Desktop\pp2\lab10\phonebook\book.cvs'
        with open(filename, "r") as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            for row in csvreader:
                cur.execute("INSERT INTO PhoneBook VALUES (%s,%s,%s)", row)
        print("Data inserted successfully from CSV file.")
        break  
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

#update

while True:
    print("Type 'update' to update some data or 'stop' to break")
    mode=input()
    if mode=="stop":
        break
    cur.execute("""SELECT * FROM PhoneBook""")
    print(cur.fetchall())
    print("Enter surname")
    changes=input()
    print("What you want to change? name/number")
    mode=input()
    print("Enter new name/number")
    new_value=input()
    update(changes, mode, new_value)

#delete
while True:
    print("Want to delete some data? yes/no")
    mode=input()
    if mode=="no":
        break
    cur.execute("""SELECT * FROM PhoneBook""")
    print(cur.fetchall())
    print("Enter surname")
    row_to_delete=input()
    delete(row_to_delete)

#search
while True:
    print("Want to find something? yes/no")
    mode = input()
    if mode.lower() == "no":
        break
    pattern = input("Enter search pattern: ")
    matched_records = search_records(pattern)
    print("Matched records:")
    for record in matched_records:
        print(record)


conn.commit()
cur.close()
conn.close()