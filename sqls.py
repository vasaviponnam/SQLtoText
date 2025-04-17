import sqlite3

connection=sqlite3.connect("student.db")

cursor=connection.cursor()

table_info="""
Create table STUDENT(name varchar(25),branch varchar(25), section varchar(25),marks int);

"""

cursor.execute(table_info)

cursor.execute('''Insert into STUDENT values('Harika','EEE','A',986)''')
cursor.execute('''Insert into STUDENT values('Vasavi','IT','A',964)''')
cursor.execute('''Insert into STUDENT values('Ravi','CSE','A',922)''')
cursor.execute('''Insert into STUDENT values('Madhu Priya','CSE','A',963)''')
cursor.execute('''Insert into STUDENT values('Sai','EEE','A',985)''')

print("Records are: ")

data=cursor.execute('''Select * from STUDENT''')

for row in data:
    print(row)

topper=cursor.execute('''SELECT name from STUDENT where marks = (Select max(marks) from STUDENT)''')

for row in topper:
    print(row)

connection.commit()
connection.close