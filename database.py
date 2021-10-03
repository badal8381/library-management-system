import mysql.connector

# Connection to the database
mydb = mysql.connector.connect(
    host="localhost",
    database="library",
    user = "root",
    password="Badal@8381962255")



# Creating tables into the library database
# Student, Book and issue book tables are being created

def create_db():

    mycursor = mydb.cursor()

    sql = "CREATE TABLE book(book_id INT PRIMARY KEY NOT NULL, book_name VARCHAR(50) NOT NULL, author_name VARCHAR(50) NOT NULL, avail BOOLEAN)"
    sql1 = "CREATE TABLE students(roll_no INT PRIMARY KEY NOT NULL, first_name VARCHAR(50) NOT NULL, last_name VARCHAR(50), std INT NOT NULL)"
    sql2 = "CREATE TABLE issue_book(roll_no INT NOT NULL, book_id INT NOT NULL, FOREIGN KEY (roll_no) REFERENCES students(roll_no), FOREIGN KEY (book_id) REFERENCES book(book_id))"

    mycursor.execute(sql)
    mycursor.execute(sql1)
    mycursor.execute(sql2)
    print(mycursor.rowcount, "Tables Created")
    mydb.commit()


create_db()
