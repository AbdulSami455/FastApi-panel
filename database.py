import mysql.connector

# Connection to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sami@1234",
    database="database",
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()


conn.commit()