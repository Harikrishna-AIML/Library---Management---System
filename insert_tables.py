# import the mysql Database into our Python Program
import mysql.connector
import pandas as pd
# Read the books csv file using Pandas
df = pd.read_csv("books.csv")
# Asking Python to connect the MySQL Server
# host = localhost it defines MySQL server running my own Computer
# user = root it is the user account provided by the MySQL server 
# password = create the password to communicate with the MySQL server
# database = new Database created by the User
connection = mysql.connector.connect(host = "localhost",
                                     user = "root",
                                     password = "*********",
                                     database = "LibraryDB")
# if Python is connect MySQL Server or not if it is connect this block is Executed!
if connection.is_connected():
    print("Connection is Successfull")
# cursor is used to Send the SQL Commands from Python to MySQL server    
cursor = connection.cursor()
# create the database called LibraryDB
cursor.execute("CREATE DATABASE if not exists LibraryDB")
# Inserting Multiple Records at a Time
sql = """
      INSERT INTO books(book_id,book_name,author,status) values(%s,%s,%s,%s)
      """
# Provides the Values to Python for inserting values into Database
values =[(1001,"Python Programming","James Smith","Available"),
        (1002,"Java Programming","Herbert Schildt","Available"),
        (1003,"Database Management Systems","Raghu Ramakrishnan","Available"),
        (1004,"SQL Fundamentals","John J. Patrick","Available"),
        (1005,"Data Structures and Algorithms","Mark Allen Weiss","Available"),
        (1006,"Machine Learning","Tom Mitchell","Available"),
        (1007,"Artificial Intelligence","Stuart Russell","Available"),
        (1008,"Computer Networks","Andrew S. Tanenbaum","Available"),
        (1009,"Operating Systems","Abraham Silberschatz","Not Available"),
        (1010,"Web Development","Jon Duckett","Available"),
        (1011,"C Programming","Dennis Ritchie","Available"),
        (1012,"C++ Programming","Bjarne Stroustrup","Available"),
        (1013,"Clean Code","Robert C. Martin","Not Available"),
        (1014,"Deep Learning","Ian Goodfellow","Available")]
# it is used for only one record insert
"""for _, row in df.iterrows():
    values = (int(row["Book_ID"]),
              row["Book_Name"],
              row["Author"],
              row["Status"])"""
# Used to Executes the SQL commands provided by the Python
cursor.executemany(sql,values)
# Save the Connection
connection.commit()
print("Values are inserted into LibraryDB Table!") 
# Telling to Python Stops Executing SQL Commands
cursor.close()
# Close the Connection Between MySQL and Python     
connection.close()
