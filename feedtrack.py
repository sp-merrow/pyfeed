import sqlite3
import tkinter as tk

db = sqlite3.connect("feed_data.db")

dbCur = db.cursor()

mainWindow = tk.Tk()
mainWindow.title("PyFeed")

def confirmTable(tableName):
    #dbCur.execute(f"CREATE TABLE IF NOT EXISTS {tableName};")
    print(tableName)

def newTable():
    newName = tk.StringVar()
    inputWin = tk.Toplevel(mainWindow)
    inputWin.title('New Table')
    tk.Label(inputWin, text='Enter new animal table name:').pack()
    tk.Entry(inputWin, textvariable=newName).pack()
    enterButton = tk.Button(inputWin, text='Submit', command=confirmTable(newName.get())).pack()

label = tk.Label(text="PyFeed").pack()
cTableButton = tk.Button(mainWindow, text='Create New Animal Table', command=newTable)
cTableButton.pack()

tk.mainloop()
