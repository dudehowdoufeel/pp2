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


def update(sn, mode, newv):
    cur.execute("""UPDATE PhoneBook
    SET {} = '{}'
    WHERE surname = '{}'
    """.format(mode,newv,sn))

def delete(sn):
    cur.execute("""DELETE FROM PhoneBook
    WHERE surname='{}'
    """.format(sn))

#INSERTING DATA--------------------------

mode="enter"
while True:
    print("Type 'enter' if you want to add more data and type 'stop' to break")
    mode=input()
    if mode=="stop":
        break
    mytuple=[]
    print("enter surname:")
    mytuple.append(input())
    print("enter name:")
    mytuple.append(input())
    print("enter number:")
    mytuple.append(input())
    mytuple=tuple(mytuple)
    cur.execute("""INSERT INTO PhoneBook (surname, name ,number) VALUES
    {};
    """.format(mytuple))

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

#UPDATING DATA---------
while True:
    print("Type 'update' to update some data or 'stop' to break")
    mode=input()
    if mode=="stop":
        break
    cur.execute("""SELECT * FROM PhoneBook""")
    print(cur.fetchall())
    print("Enter surname")
    idtochange=input()
    print("What you want to change? name/number")
    mode=input()
    print("Enter new name/number")
    newvalue=input()
    update(idtochange, mode, newvalue)

#DELETING DATA-----------
while True:
    print("want to delete some data? yes/no")
    mode=input()
    if mode=="no":
        break
    cur.execute("""SELECT * FROM PhoneBook""")
    print(cur.fetchall())
    print("Enter surname")
    idtodelete=input()
    delete(idtodelete)


conn.commit()
cur.close()
conn.close()