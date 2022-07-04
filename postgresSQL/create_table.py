import psycopg2

#Establishing the connection
conn = psycopg2.connect(
   database="postgres", user='postgres', password='1234'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Doping table if already exists.
cursor.execute("DROP TABLE IF EXISTS testing_table")

#Creating table as per requirement
sql ='''CREATE TABLE testing_table(
        FIRST_NAME CHAR(20) NOT NULL,
        LAST_NAME CHAR(20),
        AGE INT
      )'''
      
cursor.execute(sql)
print("Table created successfully........")
conn.commit()
#Closing the connection
conn.close()