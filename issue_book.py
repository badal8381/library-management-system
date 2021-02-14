import PySimpleGUI as sg
from library_data.MySQL import IssueBookDB


def IssueBook():
    """
    Book Registration Page
    """

    # Define the window's contents
    layout = [[sg.Text("Issue a book!", justification='center',  size=(18, 1), font=('roboto', 30))],
              [sg.Text("Roll No: ", size=(8, 1), font=('roboto', 15)),
               sg.Input(size=(40, 2), key='-ROLLNO-')],
              [sg.Text("Book ID: ", size=(8, 1), font=('roboto', 15)),
               sg.Input(size=(40, 2), key='-BOOKID-')],
              [sg.Text(auto_size_text=True, size=(20, 1),
                       font=('roboto', 11), key="-OUTPUT-")],
              [sg.Button('Issue', size=(18, 1), font=('roboto', 14)), sg.Button('Quit', size=(18, 1), font=('roboto', 14))]]

    # Create the window
    window = sg.Window('Library Management System',
                       layout, location=(450, 150))

    # Display and interact with the Window using an Event Loop
    while True:
        event, values = window.read()
        roll_no = values['-ROLLNO-']
        book_id = values['-BOOKID-']
        # See if user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break
        # Output a message to the window
        IssueBookDB(roll_no, book_id)
        window['-OUTPUT-'].update("Book Issued..")

    # Finish up by removing from the screen
    window.close()


