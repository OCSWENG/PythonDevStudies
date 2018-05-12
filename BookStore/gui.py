from tkinter import *
import backend

# DATABASE ACTIONS
def viewCMD():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def seekCMD():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)

def addCMD():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

def removeCMD():
    backend.delete(selected_tuple[0])

def updateCMD():
    backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())

# GUI ACTIONS
def buildLabels():
    title=Label(window,text="Title")
    author=Label(window,text="Author")
    year=Label(window,text="Year")
    isbn=Label(window,text="ISBN")
    
    title.grid(row=0,column=0)
    author.grid(row=0,column=2)
    year.grid(row=1,column=0)
    isbn.grid(row=1,column=2)

def buildEntries ():
    global title_text=StringVar()
    title=Entry(window,textvariable=title_text)
    global author_text=StringVar()
    author=Entry(window,textvariable=author_text)
    global year_text=StringVar()
    year=Entry(window,textvariable=year_text)
    global isbn_text=StringVar()
    isbn=Entry(window,textvariable=isbn_text)
    
    title.grid(row=0,column=1)
    author.grid(row=0,column=3)
    year.grid(row=1,column=1)
    isbn.grid(row=1,column=3)

def buildButtons ():
    size=12 # width=size
    viewAll=Button(window,text="View all", size,command=viewCMD)
    searchEntry=Button(window,text="Search", size,command=seekCMD)
    addEntry=Button(window,text="Add", size,command=addCMD)
    updateSelected=Button(window,text="Update", size,command=updateCMD)
    deleteSelected=Button(window,text="Delete", size,command=removeCMD)
    close=Button(window,text="Close", size,command=window.destroy)
    
    viewAll.grid(row=2,column=3)
    searchEntry.grid(row=3,column=3)
    addEntry.grid(row=4,column=3)
    updateSelected.grid(row=5,column=3)
    deleteSelected.grid(row=6,column=3)    
    close.grid(row=7,column=3)
    
def get_selected_row(event):
	try:
		global selected_tuple
		index=list1.curselection()[0]
		selected_tuple=list1.get(index)
		e1.delete(0,END)
		e1.insert(END,selected_tuple[1])
		e2.delete(0,END)
		e2.insert(END,selected_tuple[2])
		e3.delete(0,END)
		e3.insert(END,selected_tuple[3])
		e4.delete(0,END)
		e4.insert(END,selected_tuple[4])
	except IndexError:
		pass
# Window
global window = Tk()
window.wm_title("UC Book Store")
# Widgets

buildLabels()
buildEntries()

global list1=Listbox(window, height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

global sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

buildButtons()
window.mainloop()
