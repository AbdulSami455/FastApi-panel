import mysql.connector

# Connection to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="usernew",
    password="yourpassword",
    database="database1",
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

cursor.execute("SHOW TABLES;")

# Fetch all the tables
tables = cursor.fetchall()

# Print the list of tables
print("Tables in the database:")
for table in tables:
    print(table[0])

# Your SQL queries go here

# Commit the changes and close the connection
conn.commit()