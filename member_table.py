import mysql.connector
connection = mysql.connector.connect(host = "localhost",
                                     user = "root",
                                     password = "*********",
                                     database = "LibraryDB")
if connection.is_connected():
    print("Database is connected Successfully!!")
cursor = connection.cursor()
# Create a Members Table
cursor.execute("CREATE table members(member_id int primary key,member_name varchar(100),phone_number varchar(100),email varchar(100))")
print("Members table is created in Library database")
sql = """
      INSERT into members(member_id,member_name,phone_number,email) values(%s,%s,%s,%s)
      """
values = [(201,"Hari","720xxxx256","hari@36.gmail.com"),
          (202,"Mahesh","950xxxx605","mahi@1786.gmail.com"),
          (203,"Sunny","620xxxx986","sunny@8629.gmail.com"),
          (204,"Swetha","927xxxx342","cute@1786.gmail.com"),
          (205,"Shive","9120xxxx546","shiva@143.gmail.com"),
          (206,"Venkey","798xxxx535","venkey@7989.gmail.com")]
# cursor.executemany() is used to execute the multiple values
cursor.executemany(sql,values)
connection.commit()
print("Records are inserted Successfully!!")
cursor.close()
connection.close()
