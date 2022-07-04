import psycopg2

# Establishing the connection
conn = psycopg2.connect(
   database="postgres", user='postgres', password='1234'
)
conn.autocommit = True

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing query to show a tables
sql = '''select * from DETAILS''';

cursor.execute(sql)
rows = cursor.fetchall()
for row in rows:
    print(row)