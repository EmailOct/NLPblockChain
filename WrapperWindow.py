import tkinter as tk
from tkinter import *
import GraphCreator as gc

names = ()
entry = [0 for i in range(4)]

column_values = [0,1,2,3,4]


def get_names():
    return names


def get_entry():
    return entry


# Button Commands

def analyze_data():
    global names
    names = (get_entry()[0].get(), get_entry()[1].get(), get_entry()[2].get(), get_entry()[3].get())
    create_graph_select_window()


# Chart Select Window

def create_graph_select_window():
    chart_select_window = Tk()
    Button(chart_select_window, text="Bar Graph", command=lambda: gc.create_bar_graph(get_names(), "", column_values)).grid(row=0, column=0, pady=10)
    Button(chart_select_window, text="Pie Chart", command=lambda: gc.create_pie_chart(get_names())).grid(row=0, column=1, pady=10)
    Button(chart_select_window, text="Line Graph", command=lambda: gc.create_line_graph(get_names())).grid(row=1, column=0, pady=10)
    Button(chart_select_window, text="Chart").grid(row=1, column=1, pady=10)
    chart_select_window.mainloop()


# Root Window

def create_root_window():
    global entry
    root = Tk()
    Label(root, text="Name 1").grid(row=0, pady=4)
    entry[0] = Entry(root)
    entry[0].grid(row=0, column=1)
    Label(root, text="Name 2").grid(row=1, pady=4)
    entry[1] = Entry(root)
    entry[1].grid(row=1, column=1)
    Label(root, text="Name 3").grid(row=2, pady=4)
    entry[2] = Entry(root)
    entry[2].grid(row=2, column=1)
    Label(root, text="Name 4").grid(row=3, pady=4)
    entry[3] = Entry(root)
    entry[3].grid(row=3, column=1)
    Button(root, text="Submit", command=analyze_data).grid(row=4, pady=4)
    root.mainloop()


def main():
    create_root_window()


main()
