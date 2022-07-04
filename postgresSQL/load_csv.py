
import psycopg2
import csv

# Establishing the connection
conn = psycopg2.connect(
   database='postgres', user='postgres', password='1234'
)  
conn.autocommit = True
# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Drop if table if exists 
cursor.execute("DROP TABLE IF EXISTS DETAILS")


# creating new table 
sql = '''CREATE TABLE DETAILS(employee_id int NOT NULL,\
                                employee_name char(20),\
                                employee_email varchar(30) );'''
cursor.execute(sql)

# inset data 
with open('details.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    for row in reader:
        cursor.execute(
        "INSERT INTO DETAILS VALUES (%s, %s, %s)",
        row
    )
conn.commit()


