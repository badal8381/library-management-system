import mysql.connector

# Connection to the database
mydb = mysql.connector.connect(
    host="localhost",)
    #database="library",
    #user= "root",
    #password="Badal@8381962255")
    
# this function inserts data into Book table
def BookDB(book_id, book_name, author_name, avail):

    mycursor = mydb.cursor()

    sql = "INSERT INTO book(book_id, book_name, author_name, avail) VALUES (%s, %s, %s, %s)"
    val = (int(book_id), book_name, author_name, avail)

    mycursor.execute(sql, val)
    print(mycursor.rowcount, "Record Inserted")
    mydb.commit()

# this function inserts data into Issue Book table
def IssueBookDB(roll_no, book_id):

    mycursor = mydb.cursor()

    sql = "INSERT INTO issue_book(roll_no, book_id) VALUES (%s, %s)"
    val = (int(roll_no), int(book_id))

    mycursor.execute(sql, val)
    print(mycursor.rowcount, "Record Inserted")
    mydb.commit()

# this function inserts data into Student table
def studentDB(roll_no, first_name, last_name, std):

    mycursor = mydb.cursor()

    sql = "INSERT INTO students(roll_no, first_name, last_name, std) VALUES (%s, %s, %s, %s)"
    val = (int(roll_no), first_name, last_name, int(std))

    mycursor.execute(sql, val)
    print(mycursor.rowcount, "Record Inserted")
    mydb.commit()

# this function returns data from Book table
def bookQuery():

    mycursor = mydb.cursor()


    sql = "SELECT * FROM book"


    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    return myresult

# this function deletes data from Book table
def DeleteBookDB(id):

    mycursor = mydb.cursor()


    sql = f"DELETE FROM book where book_id = {id}"


    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "Book Deleted")

# this function delets data from Issue Book table
def returnBookDB(roll_no, book_id, student_name, std):

    mycursor = mydb.cursor()


    sql = f"delete from issue_book where roll_no = {int(roll_no)} and book_id = {int(book_id)};"


    mycursor.execute(sql)
    mydb.commit()
    print(f"{student_name} of class {std} Returned a Book with Book ID {book_id}")

# this function Returns data of students having books from Book and issue book table
def studentWithBookQuery():
    mycursor = mydb.cursor()


    sql = "select students.roll_no, students.first_name, students.last_name, students.std, issue_book.book_id, book.book_name, book.author_name FROM ((issue_book INNER JOIN students ON students.roll_no = issue_book.roll_no) INNER JOIN book ON issue_book.book_id = book.book_id)"


    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    return myresult

# this function returns data from Students table
def studentQuery():
    mycursor = mydb.cursor()


    sql = "SELECT * FROM students"


    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    return myresult

