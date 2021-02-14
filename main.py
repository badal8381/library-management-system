import PySimpleGUI as sg
from views import BookRegister, DeleteBook, studentRegister, returnBook
from show import showStudents, showStudentsWithBooks, showBook
from issue_book import IssueBook


def Main():
    # Define the window's contents
    layout = [[sg.Text("Library Management System!", size=(400, 2), font=('roboto', 35), justification='center',)],
              [sg.Button('Register Book', font=('roboto', 15), size=(32, 2)), sg.Button('Register Student', font=('roboto', 15), size=(32, 2))],
              [sg.Button('Issue Book to Student', font=('roboto', 15), size=(32, 2)),sg.Button('View Students with Books', font=('roboto', 15), size=(32, 2))],
              [sg.Button('View Books', font=('roboto', 15), size=(32, 2)),sg.Button('View Students', font=('roboto', 15), size=(32, 2))],
              [sg.Button('Return Book', font=('roboto', 15), size=(32, 2)), sg.Button('Delete Book', font=('roboto', 15), size=(32, 2))],
              [sg.Button('Quit', font=('roboto', 15), size=(67, 2))]]

    # Create the window
    window = sg.Window('Library Management System', layout, size=(760, 450), location=(300, 30))

    # Display and interact with the Window using an Event Loop
    while True:
        event, values = window.read()
        # See if user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break

        if event == 'Register Book':
            BookRegister()

        if event == 'Register Student':
            studentRegister()

        if event == 'Delete Book':
            DeleteBook()

        if event == 'Issue Book to Student':
            IssueBook()

        if event == 'View Students with Books':
            showStudentsWithBooks()
        
        if event == 'View Books':
            showBook()

        if event == 'View Students':
            showStudents()
        
        if event == 'Return Book':
            returnBook()

            

    # Finish up by removing from the screen
    window.close()


Main()