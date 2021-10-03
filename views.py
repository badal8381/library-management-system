from tkinter.constants import FALSE, TRUE
import PySimpleGUI as sg
from library_data.MySQL import BookDB, DeleteBookDB, studentDB, returnBookDB

#This function registers book
def BookRegister():
    """
    Book Registration Page
    """

    # Define the window's contents
    layout = [[sg.Text("Add New Book!", font=('roboto', 30), )],
              [sg.Text("Book ID: ", size=(11, 1), font=('roboto', 15)),
               sg.Input(size=(40, 2), key='-BOOKID-')],
              [sg.Text("Book Name: ", size=(11, 1), font=('roboto', 15)),
               sg.Input(size=(40, 2), key='-BOOKNAME-')],
              [sg.Text("Author Name: ", size=(11, 1), font=('roboto', 15)),
               sg.Input(size=(40, 2), key='-AUTHORNAME-')],
              [sg.Text("Available: ", size=(11, 1), font=('roboto', 15)),
               sg.Radio('Yes', group_id='bool', key='-TRUE-'), sg.Radio('No', group_id='bool', key='-FALSE-')],
              [sg.Text(key="-OUTPUT-", size=(20, 1), font=('roboto', 11))],
              [sg.Button('Register', size=(18, 1), font=('roboto', 14)), sg.Button('Quit', size=(18, 1), font=('roboto', 14))]]

    # Create the window
    window = sg.Window('Library Management System',
                       layout, location=(450, 150))

    # Display and interact with the Window using an Event Loop
    while True:
        event, values = window.read()
        book_id = values['-BOOKID-']
        book_name = values['-BOOKNAME-']
        author_name = values['-AUTHORNAME-']
        available = False
        if values['-TRUE-']:
            available = True
        elif values['-FALSE-']:
            available = False

        # See if user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break
        # Output a message to the window
        BookDB(book_id, book_name, author_name, available)
        window['-OUTPUT-'].update("Book Added Successfully..")

    # Finish up by removing from the screen
    window.close()


def DeleteBook():
    # Define the window's contents
    layout = [[sg.Text("Delete a Book!", justification='center',  size=(18, 1), font=('roboto', 30))],
              [sg.Text("Book ID: ", size=(8, 1), font=('roboto', 15)),
               sg.Input(size=(40, 2), key='-BOOKID-')],
              [sg.Text(auto_size_text=True, size=(20, 1),
                       font=('roboto', 11), key="-OUTPUT-")],
              [sg.Button('Delete', size=(18, 1), font=('roboto', 14)), sg.Button('Quit', size=(18, 1), font=('roboto', 14))]]


    # Create the window
    window = sg.Window('Library Management System',
                       layout, location=(450, 150))

    # Display and interact with the Window using an Event Loop
    while True:
        event, values = window.read()
        # See if user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break

        if event == 'Delete':
            DeleteBookDB(values['-BOOKID-'])
        window['-OUTPUT-'].update("Book Deleted...")

    # Finish up by removing from the screen
    window.close()


def returnBook():
    # Define the window's contents
    layout = [[sg.Text("Return a Book!", justification='center',  size=(18, 1), font=('roboto', 30))],
              [sg.Text("Roll No: ", size=(12, 1), font=('roboto', 15)),
               sg.Input(size=(40, 2), key='-ROLLNO-')],
              [sg.Text("Book ID: ", size=(12, 1), font=('roboto', 15)),
               sg.Input(size=(40, 2), key='-BOOKID-')],
              [sg.Text("Student Name: ", size=(12, 1), font=('roboto', 15)),
               sg.Input(size=(40, 2), key='-NAME-')],
              [sg.Text("Class: ", size=(12, 1), font=('roboto', 15)),
               sg.Input(size=(40, 2), key='-CLASS-')],
              [sg.Text(auto_size_text=True, size=(40, 1),
                       font=('roboto', 11), key="-OUTPUT-")],
              [sg.Button('Return Book', size=(18, 1), font=('roboto', 14)), sg.Button('Quit', size=(18, 1), font=('roboto', 14))]]


    # Create the window
    window = sg.Window('Library Management System',
                       layout, location=(450, 150))

    # Display and interact with the Window using an Event Loop
    while True:
        event, values = window.read()
        student_name = values['-NAME-']
        book_id = values['-BOOKID-']
        roll_no = values['-ROLLNO-']
        std = values['-CLASS-']
        # See if user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break

        if event == 'Return Book':
            returnBookDB(roll_no, book_id, student_name, std)
        window['-OUTPUT-'].update(f"{student_name} of class {std} Returned Book with Book ID {book_id}...")

    # Finish up by removing from the screen
    window.close()


def studentRegister():
    """
    Book Registration Page
    """

    # Define the window's contents
    layout = [[sg.Text("Register Student!", font=('roboto', 30), )],
              [sg.Text("Roll NO: ", size=(11, 1), font=('roboto', 15)),
               sg.Input(size=(40, 2), key='-ROLLNO-')],
              [sg.Text("First Name: ", size=(11, 1), font=('roboto', 15)),
               sg.Input(size=(40, 2), key='-FIRSTNAME-')],
              [sg.Text("Last Name: ", size=(11, 1), font=('roboto', 15)),
               sg.Input(size=(40, 2), key='-LASTNAME-')],
              [sg.Text("Class : ", size=(11, 1), font=('roboto', 15)),
               sg.Input(size=(40, 2), key='-CLASS-')],
              [sg.Text(key="-OUTPUT-", size=(20, 1), font=('roboto', 11))],
              [sg.Button('Register', size=(18, 1), font=('roboto', 14)), sg.Button('Quit', size=(18, 1), font=('roboto', 14))]]

    # Create the window
    window = sg.Window('Library Management System',
                       layout, location=(450, 150))

    # Display and interact with the Window using an Event Loop
    while True:
        event, values = window.read()
        roll_no = values['-ROLLNO-']
        first_name = values['-FIRSTNAME-']
        last_name = values['-LASTNAME-']
        std = values['-CLASS-']

        # See if user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break
        if event == 'Register':
            studentDB(roll_no, first_name, last_name, std)
        # Output a message to the window
        window['-OUTPUT-'].update("Registration Successful")

    # Finish up by removing from the screen
    window.close()
