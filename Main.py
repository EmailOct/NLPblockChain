from tkinter import *
import GraphCreator as gc

class MainClass(Tk):

    def __init__(self):
        Tk.__init__(self)

        self.container = Frame(self)
        self.container.pack(side="top", fill="both")

        self.frames = {}
        tkvar = 0

        frame1 = MainPage(parent=self.container, controller=self)
        frame1.grid(row=0, column=0, sticky="nsew")
        frame1.tkraise()

    def make_NamePage(self, num):
        frame2 = NamePage(parent=self.container, controller=self, num=num)
        frame2.grid(row=0, column=0, sticky="nsew")
        frame2.tkraise()

    def make_GraphPage(self, entries):
        names = []
        for entry in entries:
            names.append(entry.get())
        print(names)
        frame3 = GraphPage(parent=self.container, controller=self, names=names)
        frame3.grid(row=0, column=0, sticky="nsew")
        frame3.tkraise()


class MainPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        num_frame = Frame(self)
        num_frame.grid(row=0, column=0, padx=100, pady=100)

        Label(num_frame, text='No. of Arguments:').grid(row=0, column=0)

        tkvar = StringVar(self)
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        lis = OptionMenu(num_frame, tkvar, *nums)
        lis.grid(row=1, column=0)

        btn_frame = Frame(self)
        btn_frame.grid(row=1, column=0)
        Button(btn_frame, text='Submit', command=lambda: controller.make_NamePage(int(tkvar.get()))).pack(pady='5')


class NamePage(Frame):

    def __init__(self, parent, controller, num):
        Frame.__init__(self, parent)
        self.controller = controller

        entries = []
        names = []

        for i in range(num):
            Label(self, text="Name:").grid(row=i, column=0)
            entry = Entry(self)
            entries.append(entry)
            entry.grid(row=i, column=1, pady=5)

        Button(self, text="Submit", command=lambda: controller.make_GraphPage(entries)).grid(row=i+1, pady=4)


class GraphPage(Frame):

    def __init__(self, parent, controller, names):
        Frame.__init__(self, parent)
        self.controller = controller

        Button(self, text="Bar Graph", command=lambda: gc.create_bar_graph(names, "")).grid(row=0, column=0, pady=10)
        Button(self, text="Pie Chart", command=lambda: gc.create_pie_chart(names)).grid(row=0, column=1, pady=10)
        Button(self, text="Line Graph", command=lambda: gc.create_line_graph(names)).grid(row=1, column=0, pady=10)
        Button(self, text="Area Graph", command=lambda:gc.create_area_graph(names)).grid(row=1, column=1, pady=10)


if __name__ == "__main__":
        app = MainClass()
        app.mainloop()
