#!/usr/bin/python3
# http://www.java2s.com/Code/Python/GUI-Tk/2dtableofinputfields.htm

from __future__ import print_function
from cli_tables import print_table
from Tkinter import *
import sys

def initialize():
    rows_num = int(e1.get())
    cols_num = int(e2.get())
    forgetElements()
    for i in range(rows_num):
        cols = []
        for j in range(cols_num):
            e = Entry(root,relief=RIDGE)
            e.grid(row=i, column=j, sticky=NSEW)
            cols.append(e)
        rows.append(cols)
    Button(root, text='Done', command=onPress).grid(row=rows_num, column=cols_num-1)

def onPress():
    newrows = [[y.get() for y in x] for x in rows ]
    print_table(newrows)
    quit()

def forgetElements():
    e1.grid_forget()
    e2.grid_forget()
    l1.grid_forget()
    l2.grid_forget()
    b.destroy()

rows = []
root = Tk()
root.title("cli_tables")

l1 = Label(root, text="Rows")
l2 = Label(root, text="Columns")
e1 = Entry(root, relief=RIDGE)
e2 = Entry(root, relief=RIDGE)

l1.grid(row=0, column=0, sticky=W)
l2.grid(row=1, column=0, sticky=W)
e1.grid(row=0, column=1, sticky=E)
e2.grid(row=1, column=1, sticky=E)

b = Button(root, text='Done', command=initialize)
b.grid(row=2, column=1)

root.mainloop()
