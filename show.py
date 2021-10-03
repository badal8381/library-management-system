import PySimpleGUI as sg
from library_data.MySQL import studentQuery, bookQuery, studentWithBookQuery
import tkinter as tk
from tkinter import ttk


# This function shows All the Books names
def ShowBook():
    root = tk.Tk()
    root.title("Books")
    root.geometry("500x200")

    table = ttk.Treeview()
    table['show'] = 'headings'

    #defining number of columns
    table["columns"] = ("BookID", "BookName", "AuthorName", "Availability")

    #Assign the width, minwidth and anchor to the respective columns
    table.column("BookID", width=50, minwidth=50, anchor = tk.CENTER)
    table.column("BookName", width=200, minwidth=100, anchor = tk.CENTER)
    table.column("AuthorName", width=150, minwidth=70, anchor = tk.CENTER)
    table.column("Availability", width=100, minwidth=70, anchor = tk.CENTER)


    #Assign the heading names to the respective columns
    table.heading("BookID", text = "Book ID", anchor = tk.CENTER)
    table.heading("BookName", text = "Book Name", anchor = tk.CENTER)
    table.heading("AuthorName", text = "Author Name", anchor = tk.CENTER)
    table.heading("Availability", text = "Availability", anchor = tk.CENTER)

    i = 0
    for row in bookQuery():
        table.insert('', i, text = "", values = (row[0], row[1], row[2], row[3]))
        i = i + 1

    table.pack()
    root.mainloop()


def showStudents():
    print("---------------------------Student Details-----------------------------")
    print("(Roll NO, " + "First Name, "+"Last Name, "+"Class)")
    for row in studentQuery():
        print(row)
    # Define the window's contents
    layout = [[sg.Text("Check The Console for Details", justification='center',  size=(25, 1), font=('roboto', 30))],
              [sg.Button('Quit', size=(50, 2), font=('roboto', 14))]]


    # Create the window
    window = sg.Window('Library Management System',
                       layout, location=(390, 200))

    # Display and interact with the Window using an Event Loop
    while True:
        event, values = window.read()
        # See if user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break

    # Finish up by removing from the screen
    window.close()


def showStudentsWithBooks():
    print("--------------------------Student With Books------------------------------")
    print("(Roll NO, " + "First Name, "+"Last Name, "+"Class, "+"Book ID, "+"Book Name, "+"Author Name)")
    for row in studentWithBookQuery():
        print(row)
    # Define the window's contents
    layout = [[sg.Text("Check The Console for Details", justification='center',  size=(25, 1), font=('roboto', 30))],
              [sg.Button('Quit', size=(50, 2), font=('roboto', 14))]]


    # Create the window
    window = sg.Window('Library Management System',
                       layout, location=(390, 200))

    # Display and interact with the Window using an Event Loop
    while True:
        event, values = window.read()
        # See if user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break

    # Finish up by removing from the screen
    window.close()


def showBook():
    print("---------------------------Book Details-----------------------------")
    print("(Book ID, " + "Book Name, "+"Author Name, "+"Availability)")
    for row in bookQuery():
        print(row)
    # Define the window's contents
    layout = [[sg.Text("Check The Console for Details", justification='center',  size=(25, 1), font=('roboto', 30))],
              [sg.Button('Quit', size=(50, 2), font=('roboto', 14))]]


    # Create the window
    window = sg.Window('Library Management System',
                       layout, location=(390, 200))

    # Display and interact with the Window using an Event Loop
    while True:
        event, values = window.read()
        # See if user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break

    # Finish up by removing from the screen
    window.close()
