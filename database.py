# Connecting MySQl Server to Python
import mysql.connector
from datetime import date
from datetime import datetime
# connecting MySQL to Python and provides the user Database details to Python
def get_connection():
    connection = mysql.connector.connect(host = "localhost",
                                         user = "root",
                                         password = "*********",
                                         database = "LibraryDB")
    return connection
# Display the all Books
def display_books():
    connection = get_connection()
    cursor = connection.cursor()
    # Select the all records from books Table
    cursor.execute("SELECT *from books")
    books = cursor.fetchall()
    print("----------BOOKS LIST-----------\n")
    for book in books:
        print(f"Book ID :{book[0]} | "
              f"Book Name :{book[1]} | "
              f"Author :{book[2]} | "
              f"Status :{book[3]} | ")
    cursor.close()
    connection.close()    
# Searching Particular Book        
def search_books(book_name):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "SELECT *from books where book_name = %s"
    values = (book_name,)
    cursor.execute(sql,values)
    books = cursor.fetchall()
    if not books:
        print("Books Not Available right now!!")
    else:    
        print("--------Available Books for you-------") 
        for book in books:
             print(f"Book ID :{book[0]} | "
              f"Book Name :{book[1]} | "
              f"Author :{book[2]} | "
              f"Status :{book[3]} |")
    cursor.close()
    connection.close()          
# adding books into the Books table              
def add_books(book_id,book_name,author):
    connection = get_connection()  
    cursor = connection.cursor() 
    sql = """
          INSERT INTO books(book_id,book_name,author,status)
          VALUES(%s,%s,%s,%s)
          """
    values = (book_id,book_name,author,"Available")
    cursor.execute(sql,values)
    connection.commit()
    print("Your Book is add to Database!")
    cursor.close()
    connection.close()
# Whether the Book is Issued or Not    
def issue_books(member_id,book_id):
    connection = get_connection() 
    cursor = connection.cursor() 
    sql = "select member_name from members where member_id = %s" 
    values = (member_id,)
    cursor.execute(sql,values)
    member = cursor.fetchone()
    if member is None:
        print("Member not Found!")
        cursor.close()
        connection.close()
        return
    sql = "select book_name,status from books where book_id = %s"
    values = (book_id,)
    cursor.execute(sql,values)
    book = cursor.fetchone()
    if book is None:
        print("Book Not Found!")
        cursor.close()
        connection.close()
        return
    if book[1] == "Issued":
        print("Book is already Issued!")
        cursor.close()
        connection.close()
        return
    sql = "update books set status = %s where book_id = %s"
    values = ("Issued",book_id)
    cursor.execute(sql,values)
    sql = "INSERT INTO issue_records(member_id,book_id,issue_date,return_date) values(%s,%s,%s,%s)"
    issue_date = input("Enter Issued Date (yyyy-mm-dd) :")
    values = (member_id,book_id,issue_date,None)
    cursor.execute(sql,values)  
    connection.commit()     
    print("Book is Issued Successfully!")
    print(f"Member :{member[0]}")
    print(f"Book :{book[0]}")
    print(f"Issued Date :{date.today()}")
    cursor.close()
    connection.close()
def count_books():
    connection = get_connection() 
    cursor = connection.cursor()
    sql = "select count(*) as total_books from books"
    cursor.execute(sql)  
    result = cursor.fetchone() 
    print(f"Total Books :{result[0]}")
    cursor.close()
    connection.close()    
def return_books(book_id):
    connection = get_connection() 
    cursor = connection.cursor()
    sql = "SELECT record_id,issue_date from issue_records where book_id = %s AND return_date is NULL"
    values = (book_id,) 
    cursor.execute(sql,values)
    record = cursor.fetchone()
    if record is None:
        print("This book is not currently Issued!")
        cursor.close()   
        connection.close()  
        return
    return_date = input("Enter Return Date (YYYY-MM-DD)")
    days_kept,fine = calculate_fine(record[1],return_date)
    sql = "update issue_records set return_date = %swhere record_id = %s"
    values = (return_date,record[0])
    cursor.execute(sql,values)
    sql = "update books set status = %s where book_id = %s"
    values = ("Available",book_id)
    cursor.execute(sql,values)
    connection.commit()
    print("========Return Book==========")
    print("Issue date :",record[1])
    print("Return Date:",return_date)
    print("Days Kept :",days_kept)
    if days_kept>7:
        print("Late Days :",days_kept-7)
    print("Fine :",fine)    
    print("Book Returned Successfully!")
    cursor.close()
    connection.close()  
def available_books():
    connection = get_connection()
    cursor = connection.cursor()
    sql = "select book_id,book_name,author,status from books where status = %s"
    values = ("Available",)
    cursor.execute(sql,values)
    books = cursor.fetchall()
    if not books:
        print("Books Are not Available right now")
    else:
        for book in books:
            print(f"Book ID :{book[0]}",
                  f"Book Name :{book[1]}",
                  f"Author :{book[2]}",
                  f"Status :{book[3]}")
    cursor.close()
    connection.close()        
def notavailable_books():
    connection = get_connection()
    cursor = connection.cursor() 
    sql = "select book_id,book_name,author,status from books where status = %s" 
    values = ("Not Available",)
    cursor.execute(sql,values)
    books = cursor.fetchall()
    if not books:
        print("All books are available") 
    else:
        print("-------Not Available Books are-------")
        for book in books:
            print(f"Book ID :{book[0]}",
                  f"Book Name :{book[1]}",
                  f"Author :{book[2]}",
                  f"Status :{book[3]}")
    cursor.close()
    connection.close()          
# Member Operations
def add_members(member_id,member_name,phone_number,email):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "INSERT INTO members(member_id,member_name,phone_number,email) values(%s,%s,%s,%s)"
    values = (member_id,member_name,phone_number,email)
    cursor.execute(sql,values)
    print("Member is Added Successfully!!")
    connection.commit()
    cursor.close()
    connection.close()  
def view_members():
    connection = get_connection() 
    cursor = connection.cursor() 
    cursor.execute("SELECT *from members")
    members = cursor.fetchall()
    if not members:
        print("There is No Members yet!") 
    else:
        for member in members:
            print("Your searched Member :")
            print(f"{'Member ID':<23}:{member[0]}")
            print(f"{'Member Name':<23}:{member[1]}")
            print(f"{'Phone number':<23}:{member[2]}")
            print(f"{'Email':<23}:{member[3]}")
    cursor.close()
    connection.close()
# Counting Total No.of Members In Database            
def count_members():
    connection = get_connection()
    cursor = connection.cursor() 
    sql = "select count(*) as total_members from members" 
    cursor.execute(sql)
    result = cursor.fetchone() 
    print("Total no.of Members :",result[0])
    cursor.close()
    connection.close()
# Searching Particular Member In the Database based on Member ID   
def search_members(member_id):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "select *from members where member_id = %s" 
    values = (member_id,)
    cursor.execute(sql,values) 
    member = cursor.fetchone()
    if not member:
        print("Member ID is not Available!") 
    else:
        print("Your searched Member :")
        print(f"{'Member ID':<23}:{member[0]}")
        print(f"{'Member Name':<23}:{member[1]}")
        print(f"{'Phone number':<23}:{member[2]}")
        print(f"{'Email':<23}:{member[3]}")
    cursor.close()
    connection.close()    
# Delete Members from the members Table        
def delete_members(member_id):
    connection = get_connection()
    cursor = connection.cursor()  
    sql = "DELETE from members where member_id = %s" 
    values = (member_id,)
    cursor.execute(sql,values)
    if cursor.rowcount>0:
        connection.commit()
        print("Member Deleted Successfully!")  
    else:
        print("Member ID is not available!")                                              
    cursor.close()
    connection.close()
# Issue AND Return History    
def issue_history():
    connection = get_connection() 
    cursor = connection.cursor()
    sql = "SELECT record_id,member_id,book_id,issue_date,return_date from issue_records"
    cursor.execute(sql)
    records = cursor.fetchall()
    if not records:
        print("No Issue books are found!")
    else:
        print("=========Issue and Return History=========")
        for record in records:
            print(f"{'Record ID':<23}:{record[0]}")
            print(f"{'Member ID':<23}:{record[1]}") 
            print(f"{'Book ID':<23}:{record[2]}")
            print(f"{'Issue Date':<23}:{record[3]}") 
            if record[4] is None:
                print("Return Date : Not Returned")    
            else:
                print(f"{'Return Date':<23}:{record[4]}")  
            print("===========================================")           
    cursor.close()
    connection.close()
# Calculating the Fine for book returned Late      
def calculate_fine(issue_date,return_date):
    issue_date = datetime.strptime(str(issue_date),"%Y-%m-%d")
    return_date = datetime.strptime(str(return_date),"%Y-%m-%d")
    days_kept = (return_date-issue_date).days
    allowed_days = 7
    fine_per_day = 10
    if days_kept <= allowed_days:
        fine = 0
    else:
        late_days = (days_kept)-(allowed_days)
        fine = (late_days)*(fine_per_day)
    return days_kept,fine
days,fine = calculate_fine("2026-10-01","2026-10-10")
print("Days Kept :",days)
print("Fine :",fine) 
# It is for Member History
def members_history(member_id):
    connection = get_connection()
    cursor = connection.cursor()
    # finding Member history using join operations in MySQL
    sql = """select members.member_name,books.book_name,issue_records.issue_date,issue_records.return_date 
             from issue_records join members on issue_records.member_id = members.member_id join books on
             issue_records.book_id = books.book_id where members.member_id = %s"""
    values = (member_id,)
    cursor.execute(sql,values)
    records = cursor.fetchall()
    if records is None:
        print("No History is found for this Member")
    else:
        print("=====Member History======")
        for record in records:
            print(f"{'Member name':<23}:{record[0]}")
            print(f"{'Book Name':<23}:{record[1]}")
            print(f"{'Issued Date':<23}:{record[2]}")
            if record[3] is None:
                print("Return Date : Not Returned")
            else:
                print(f"{'Return Date':<23}:{record[3]}")
            print("===================================")        
    cursor.close()
    connection.close()
def library_dashboard():
    connection = get_connection() 
    cursor = connection.cursor() 
    # Total books
    sql = "Select count(*)from books"
    cursor.execute(sql)  
    total_books = cursor.fetchone()[0]
    # Total available Books
    sql = "select count(*) from books where status = %s"
    values = ("Available",)
    cursor.execute(sql,values)
    available_book = cursor.fetchone()[0]
    # Total issued books
    sql = "select count(*) from books where status = %s"
    values = ("Issued",)
    cursor.execute(sql,values)
    total_issued = cursor.fetchone()[0]
    # Total members
    sql = "select count(*) from members"
    cursor.execute(sql)
    total_memebers = cursor.fetchone()[0]
    # Total Transactions
    sql = "select count(*) from issue_records"
    cursor.execute(sql)
    total_transactions = cursor.fetchone()[0]
    print("=========Library Dashboard==========")
    print(f"{'Total Books':<23}:{total_books}")
    print(f"{'Total Available Books':<23}:{available_book}")
    print(f"{'Total Issued Books':<23}:{total_issued}")
    print(f"{'Total Members':<23}:{total_memebers}")
    print(f"{'Total Transactions':<23}:{total_transactions}")
    print("====================================")
    cursor.close()
    connection.close()
