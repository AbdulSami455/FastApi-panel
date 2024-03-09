import mysql.connector

# Connection to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="usernew",
    password="yourpassword",
    database="database2",
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

conn.commit()