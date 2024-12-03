import sqlite3

## connect to sqllite
connection = sqlite3.connect("student.db")

## create a cursor object to insert record, create table
cursor = connection.cursor()

## create table
table_info = """
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT);
"""

cursor.execute(table_info)

## Insert records
cursor.execute('''Insert Into STUDENT values('Krish', 'Data Science', 'A', 90)''')
cursor.execute('''Insert Into STUDENT values('Sudhanshu','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Dhruv', 'Data Science', 'A', 86)''')
cursor.execute('''Insert Into STUDENT values('Hitesh', 'DEVOPS', 'A', 50)''')
cursor.execute('''Insert Into STUDENT values('Sunny', 'DEVOPS', 'A', 35)''')

## Display all the records
print("The inserted records are :")
data = cursor.execute('''Select * from STUDENT''')

for row in data:
    print(row)

## commit your changes in the database
connection.commit()
connection.close()