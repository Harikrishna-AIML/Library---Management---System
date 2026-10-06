import pandas as pd
from database import display_books,add_books,search_books,issue_books,count_books,return_books,available_books,notavailable_books,add_members,view_members,count_members,search_members,delete_members,issue_history,members_history,library_dashboard
# read books.csv file using Pandas 
df = pd.read_csv("books.csv")
print("==========================================")
print("Library Management System")
print("==========================================")
while(True):
    print("01.Add Book")
    print("02.Return Book")
    print("03.Issue Book")
    print("04.Display Books")
    print("05.Search Book")
    print("06.Not Available Books")
    print("07.Available Books")
    print("08.Total no.of books")
    print("09.Add Member")
    print("10.View Members")
    print("11.Search Members")
    print("12.Delete Member")
    print("13.Issue History")
    print("14.Show Member History")
    print("15.Library Dashboard")
    print("Enter 16 to Exit")
    try:
        choice = int(input("Enter your choice :"))
    except ValueError:
        print("Can you Please Enter only integer values!")    
        continue
    def exit_library():
            print("---------Exited From Library Management System------------")
            print("Thank you for visiting Library Management System")
            print("All the Best")     
    if choice == 1:
        while(True):
         try:
            book_id = int(input("Enter Book ID :"))
            break
         except ValueError:
            print("Book ID Must be an Integer Value!")
            continue
        book_name = input("Enter Book Name :")
        author = input("Enter Author Name :")
        add_books(book_id,book_name,author)
    elif choice == 2:
        while(True):
            try:
                 book_id = int(input("Enter Book ID :"))
                 break
            except ValueError:
                print("Book ID Must be an integer")  
                continue
        return_books(book_id)  
    elif choice == 3:
        while(True):
            try:
                member_id = int(input("Enter Member ID :"))
                book_id = int(input("Enter Book ID :"))
                break
            except ValueError:
                print("Book ID must be an Integer!!")
                continue     
        issue_books(member_id,book_id)
    elif choice == 4:
        display_books()  
    elif choice == 5:
        book_name = input("Enter Book Name :")
        search_books(book_name)
    elif choice == 6:
        notavailable_books()
    elif choice == 7:
        available_books() 
    elif choice == 8:
        count_books() 
    elif choice == 9:
        while(True):
         try:
            member_id = int(input("Enter the Member ID :"))
            break
         except ValueError:
            print("Member ID must be an integer")
            continue
        member_name = input("Enter Member name :")
        phone_number = input("Enter Phone number :") 
        email = input("Enter Email ID :")
        add_members(member_id,member_name,phone_number,email) 
    elif choice == 10:
        print("------Members List-------\n") 
        view_members()
        print("-----Member Count-----")
        count_members()  
    elif choice == 11:
        while(True):
            try:
                member_id = int(input("Enter Member ID :"))
                break
            except ValueError:
                print("Member ID must be an integer") 
                continue   
        search_members(member_id) 
    elif choice == 12:
        while(True):
            try:
                member_id = int(input("Enter Member ID :"))
                break
            except ValueError:
                print("Member ID must be an Integer!")
        delete_members(member_id) 
    elif choice == 13:
        issue_history()  
    elif choice == 14:
        while True:
            try:
                member_id = int(input("Enter Member ID :"))
                break
            except ValueError:
                print("Member ID must be an Integer")    
                continue    
        members_history(member_id)  
    elif choice == 15:
        library_dashboard()                           
    elif choice == 16:
        exit_library()
        break     
    else:
        print("Please Enter valid choice ")        
