import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="postgres", user='postgres', password='1234'
)
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing query to show tables
sql = """SELECT table_name FROM information_schema.tables
       WHERE table_schema = 'public' """;

cursor.execute(sql)
rows = cursor.fetchall()
for row in rows:
    print(row[0])


