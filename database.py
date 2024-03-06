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

# Your SQL queries go here

# Commit the changes and close the connection
conn.commit()
conn.close()
