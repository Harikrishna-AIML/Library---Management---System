** LIBRARY MANAGEMENT SYSTEM **

A **Python + **MySQL based **Library Management System** designed to "manage books", "library members", "book issuing", "book returns", and borrowing history efficiently.

**This project was developed as a practical Python and Database project to understand how a real-world application can interact with a MySQL database.

**Project Overview**

- The Library Management System provides a simple command-line interface for managing the day-to-day operations of a library.

**The system allows the librarian to:**

- 01.Manage books
- 02.Manage library members
- 03.Search for books
- 04.Issue books
- 05.Return books
- 06.Track issue history
- 07.View individual member history
- 08.Delete members
- 09.View available and unavailable books
- 10.Monitor library information through a dashboard
- 11.Find Fines

***All important records are stored in a MySQL database, making the system more reliable than a simple file-based application.

**Features**

*Book Management*

- Add new books
- Search books by name
- View all available books
- View issued/unavailable books
- View total number of books
- Track book availability status

*Member Management*

- Add new members
- View all members
- Delete members
- View individual member history

*Book Transactions*

- Issue books to members
- Return issued books
- Store issue records
- Store return information
- Track borrowing history

*Library Dashboard*

The dashboard provides a quick overview of the library, including important information such as:

- Total books
- Available books
- Issued books
- Total members
- Other library statistics

**Error Handling**

The system handles common user-input errors such as:

- Invalid integer input
- Invalid Book ID
- Invalid Member ID
- Duplicate Book IDs
- Invalid database operations
- Searching for unavailable records

**Technologies Used**

Technology                Purpose

01.Python              :   Application development
02.MySQL               :   Database management
03.MySQL Connector     :   Python Connecting Python with MySQL
04.Git & GitHub        :   Version control and project hosting (To Protect the Project)
05.Pandas              :   Analysis of Data

**Database**

The project uses a MySQL database named   :   LibraryDB

**The database contains tables for managing:**

- 01.Books Table
- 02.Members Table
- 03.Issue Records Table
**Why I am Use Database Instead of Simple CSV file**

--> The database stores information permanently instead of keeping the data only while the Python program is running.while using the Database i learn How to Communicate MySQL with Python and how actually stores data in the Databases that's why i use Databases 

**My Project Structure**

Library-Management-System(04)
│
├── main.py
├── database.py
├── insert_tables.py
├── test_mysql.py
├── books.csv
├── README.md
└── .gitignore

**main.py**

- Contains the main menu and handles user interaction.

**database.py**

- Contains functions responsible for communicating with the MySQL database.

**insert_tables.py**

- Used to insert initial/sample records into the database.

**test_mysql.py**

- Used to test the MySQL connection.

**Python–MySQL Connection**

- The application connects Python to MySQL using  :  import mysql.connector

- The database connection is established before performing database operations.

**Main Menu**

- The application provides options for different library operations, such as:

1. Add Book
2. View Books
3. Search Book
4. ...
7. Available Books
8. Total No. of Books
9. Add Member
10. View Members
11. Delete Member
12. ...
13. Issue History
14. Member History
15. Library Dashboard
16. Exit

**Book Issue and Return Process**

*Issue Book*

1. Takes the Book ID.
2. Checks whether the book exists.
3. Checks whether the book is available.
4. Records the issue information.
5. Changes the book status to unavailable.

**Return Book**

1. Takes the Book ID.
2. Checks the issue record.
3. Accepts the return date.
4. Updates the issue record.
5. Changes the book status back to available.

I think This creates a realistic book borrowing workflow right.

**Library Dashboard**

- The dashboard provides a simple summary of the current library status.

like this...
====================================
        LIBRARY DASHBOARD
====================================

Total Books       : 10
Available Books   : 7
Issued Books      : 3
Total Members     : 5

====================================

**Concepts Learned**

- Through this project, I practiced and learned:

- Python functions
- Conditional statements
- Real-world Projects work flows
- Loops
- Exception handling
- User input validation
- Modular programming
- SQL queries
- MySQL database management
- Primary keys
- CRUD operations
- Python–MySQL connectivity
- Database transactions
- Working with dates
- Git and GitHub
- Project organization

**Faced Problems through this projet**

01.mysql.connector.ProgrammingError : i got this error because while i for got clossing the connection between Python and MySQL Databese. So,i Learn After every function must close the connection.
02.ValueError :Using the Exception Handling i fixed this Error

**Future Enhancements**

-*Possible future improvements in this Project*

- Login and authentication
- Fine calculation for late returns
- Automatic due-date calculation
- Advanced book search and filtering
- GUI using Tkinter or PyQt
- Web version using Flask or Django
- Advanced analytics and reports

I am Interesting 

- Artificial Intelligence & Machine Learning
- Python
- Data Analysis
- Real-world AI Projects
- Software Development

**Acknowledgement**

This project was developed as a hands-on learning project to understand how Python applications can work with relational databases and implement real-world management systems.

**Why iam Built this Project**
This project is created for educational and learning purposes.


Thank you for seeing My Project.......

