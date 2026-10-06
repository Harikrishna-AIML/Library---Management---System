import mysql.connector
connection = mysql.connector.connect(host = "localhost",
                                     user = "root",
                                     password = "Hari@9505",
                                     database = "LibraryDB")
if connection.is_connected():
    print("Connection is Successfull!")
cursor = connection.cursor()
# create issue_records table
cursor.execute("CREATE TABLE issue_records(record_id INT PRIMARY KEY auto_increment,member_id INT,book_id INT,issue_date DATE,return_date DATE)")
print("Record Table Is created successfully!")
cursor.close()
connection.close()