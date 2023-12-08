from tkinter import *
import ttkbootstrap as tb 

root = tb.Window(themename='superhero')

#root = Tk()

root.title("TTK bootstrap! Notebook Tabs!")
#root.iconbitmap()
root.geometry('500x400')

my_notebook = tb.Notebook(root,bootstyle='info')
my_notebook.pack(pady=20)

tab1 = tb.Frame(my_notebook)
tab2 =tb.Frame(my_notebook)

my_label =Label(tab1,text='My awesome Label',font=("Helvetica",18))
my_label.pack(pady=20)

my_text = Text(tab1,width=70,height=10)
my_text.pack(pady=10,padx=10)

my_button = tb.Button(tab1,text='Click me',bootstyle= "Danger outline")
my_button.pack()

my_label2=Label(tab2,text='This is Tab',font=("Helvetica",18))
my_label2.pack(pady=20)


my_notebook.add(tab1,text='Tab one')
my_notebook.add(tab2,text='Tab two')
root.mainloop()
