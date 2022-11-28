import tkinter as tk
from tkinter import *
LARGE_FONT = ("Verdana", 16)
#Controller for the pages aka the classes for each function
class back(tk.Tk):


    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        tk.Frame()
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.geometry('900x500')
        self.title("Electronics Calculator")
        self.frames = {}

        for F in (StartPage, PageOne, PageTwo,PageTwoV,PageTwoC,PageTwoR,PageThree,PageThreeS,PageThreeP,PageFour,PageFourS,PageFourP,
                  PageFive,PageSix,PageSeven,PageEight,PageNine,PageNineC,PageNineR,PageNineP,PageNineT):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

# Homepage
class StartPage(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Electronics Calculator", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Resistor Color Coding", font = 40,command=lambda: controller.show_frame(PageOne))
        button1.place(relx=0.03, rely=0.13, relwidth=0.3, relheight=0.2)

        button2 = tk.Button(self, text="Ohm's Law Calculator", font = 40,command=lambda: controller.show_frame(PageTwo))
        button2.place(relx=0.03, rely=0.35, relwidth=0.3, relheight=0.2)

        button3 = tk.Button(self, text="Conductance",font = 40,command=lambda: controller.show_frame(PageThree))
        button3.place(relx=0.03, rely=0.57, relwidth=0.3, relheight=0.2)

        button4 = tk.Button(self, text="Capacitance",font = 40,command=lambda: controller.show_frame(PageFour))
        button4.place(relx=0.35, rely=0.13, relwidth=0.3, relheight=0.2)

        button5 = tk.Button(self, text="Current Divider",font = 40,command=lambda: controller.show_frame(PageFive))
        button5.place(relx=0.35, rely=0.35, relwidth=0.3, relheight=0.2)

        button6 = tk.Button(self, text="Voltage Divider",font = 40,command=lambda: controller.show_frame(PageSix))
        button6.place(relx=0.35, rely=0.57, relwidth=0.3, relheight=0.2)

        button7 = tk.Button(self, text="KCL Calculator",font = 40,command=lambda: controller.show_frame(PageSeven))
        button7.place(relx=0.67, rely=0.13, relwidth=0.3, relheight=0.2)

        button8 = tk.Button(self, text="KVL Calculator",font = 40,command=lambda: controller.show_frame(PageEight))
        button8.place(relx=0.67, rely=0.35, relwidth=0.3, relheight=0.2)

        button9 = tk.Button(self, text="Power Consumption Calculator",font = 40,command=lambda: controller.show_frame(PageNine))
        button9.place(relx=0.67, rely=0.57, relwidth=0.3, relheight=0.2)

#Resistor Color Coding
class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Resistor Color Code Calculator", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        l1 = Label(self, text="First Band:").place(relx=0.37, rely=0.115)
        l2 = Label(self, text="Second Band:").place(relx=0.37, rely=0.175)
        l3 = Label(self, text="Third Band:").place(relx=0.37, rely=0.24)
        l4 = Label(self, text="Fourth Band:").place(relx=0.37, rely=0.30)
        choices1 = ('black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white')
        v1 = StringVar()
        popupMenu1 = OptionMenu(self, v1, *choices1)
        popupMenu1.pack()

        choices2 = ('black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white')
        v2 = StringVar()
        popupMenu2 = OptionMenu(self, v2, *choices2)
        popupMenu2.pack()

        choices3 = ('black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet')
        v3 = StringVar()
        popupMenu3 = OptionMenu(self, v3, *choices3)
        popupMenu3.pack()

        choices4 = ('gold', 'silver', 'none')
        v4 = StringVar()
        popupMenu4 = OptionMenu(self, v4, *choices4)
        popupMenu4.pack()

        error1 = 0
        first_band = []
        def firstband():
            if v1.get() == "black":
                return first_band.append('0')
            elif v1.get() == "brown":
                return first_band.append('1')
            elif v1.get() == "red":
                return first_band.append('2')
            elif v1.get() == "orange":
                return first_band.append('3')
            elif v1.get() == "yellow":
                return first_band.append('4')
            elif v1.get() == "green":
                return first_band.append('5')
            elif v1.get() == "blue":
                return first_band.append('6')
            elif v1.get() == "violet":
                return first_band.append('7')
            elif v1.get() == "grey":
                return first_band.append('8')
            elif v1.get() == "white":
                return first_band.append('9')
            else:
                pass

        second_band = []
        def secondband():
            if v2.get() == "black":
                return second_band.append('0')
            elif v2.get() == "brown":
                return second_band.append('1')
            elif v2.get() == "red":
                return second_band.append('2')
            elif v2.get() == "orange":
                return second_band.append('3')
            elif v2.get() == "yellow":
                return second_band.append('4')
            elif v2.get() == "green":
                return second_band.append('5')
            elif v2.get() == "blue":
                return second_band.append('6')
            elif v2.get() == "violet":
                return second_band.append('7')
            elif v2.get() == "grey":
                return second_band.append('8')
            elif v2.get() == "white":
                return second_band.append('9')
            else:
                pass

        third_band = []
        def thirdband():
            if v3.get() == "black":
                pass
            elif v3.get() == "brown":
                return third_band.append("0")
            elif v3.get() == "red":
                return third_band.append("00")
            elif v3.get() == "orange":
                return third_band.append("K")
            elif v3.get() == "yellow":
                return third_band.append("0K")
            elif v3.get() == "green":
                return third_band.append("00K")
            elif v3.get() == "blue":
                return third_band.append("M")
            elif v3.get() == "violet":
                return third_band.append("0M")
            else:
                pass

        forth_band = []
        def fourthband():
            if v4.get() == "gold":
                return forth_band.append("and ±5% tolerance")
            elif v4.get() == "silver":
                return forth_band.append("and ±10% tolerance")
            elif v4.get() == "None":
                return forth_band.append("and ±20% tolerance")
            else:
                pass

        def Solve():
            total.delete(0, END)
            first_band.clear()
            second_band.clear()
            third_band.clear()
            forth_band.clear()
            firstband()
            secondband()
            thirdband()
            fourthband()
            error1 = []
            if first_band and second_band and third_band and forth_band != error1:
                resistor = first_band + second_band + third_band + forth_band
                total.insert(0, resistor)
            elif third_band == error1:
                resistor = first_band + second_band + forth_band
                total.insert(0, resistor)
            else:
                error = 'Complete the Vaiables'
                total.insert(0, error)
        def reset():
            total.delete(0, END)
            first_band.clear()
            second_band.clear()
            third_band.clear()
            forth_band.clear()

            v1.set('')
            popupMenu1['menu'].delete(0,'end')
            choices5 = ('black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white')
            for choice in choices5:
                popupMenu1['menu'].add_command(label=choice, command=tk._setit(v1, choice))

            v2.set('')
            choices6= ('black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white')
            popupMenu2['menu'].delete(0, 'end')
            for choice1 in choices6:
                popupMenu2['menu'].add_command(label=choice1, command=tk._setit(v2, choice1))

            v3.set('')
            choices7 = ('black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet')
            popupMenu3['menu'].delete(0,'end')
            for choice2 in choices7:
                popupMenu3['menu'].add_command(label=choice2, command=tk._setit(v3, choice2))

            v4.set('')
            choices8 = ('gold', 'silver', 'none')
            popupMenu4['menu'].delete(0, 'end')
            for choice3 in choices8:
                popupMenu4['menu'].add_command(label=choice3, command=tk._setit(v4, choice3))

        total = Entry(self, width=35, justify=CENTER)
        total.pack()
        b1 = Button(self, text="Solve!", command=Solve).pack()
        b2 = Button(self, text="Reset", command=reset).pack()
        home = tk.Button(self, text="Home", font=40, command=lambda: controller.show_frame(StartPage))
        home.place(relx=0.8, rely=0.7, relwidth=0.1, relheight=0.1)

#Ohms Law Calculator homepage
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="What do you want to calculate?", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Voltage", font=40,command=lambda: controller.show_frame(PageTwoV))
        button1.place(relx=0.35, rely=0.13, relwidth=0.3, relheight=0.2)

        button2 = tk.Button(self, text="Current", font=40, command=lambda: controller.show_frame(PageTwoC))
        button2.place(relx=0.35, rely=0.35, relwidth=0.3, relheight=0.2)

        button3 = tk.Button(self, text="Resistance", font=40, command=lambda: controller.show_frame(PageTwoR))
        button3.place(relx=0.35, rely=0.57, relwidth=0.3, relheight=0.2)

        home = tk.Button(self, text="Home", font=40, command=lambda: controller.show_frame(StartPage))
        home.place(relx=0.8, rely=0.8, relwidth=0.1, relheight=0.1)

#Voltage Page for Ohm's Law
class PageTwoV(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Enter the Variables", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        def Voltage():
            V.delete(0, END)
            try:
                a = float(I.get())
                b = float(R.get())
                c = a*b
                c1 = round(c,4)
                V.insert(0, c1)
            except ValueError:
                error ="Invalid Input!"
                V.insert(0,error)
        l1 = Label(self, text='Enter the Current', font=24)
        l1.pack(padx=10, pady=10)
        I = Entry(self, justify=CENTER, font=28)
        I.pack()

        l2 = Label(self, text='Enter the Resistance', font=24)
        l2.pack(padx=10, pady=10)
        R = Entry(self, justify=CENTER, font=28)
        R.pack()

        l3  = Label(self, text = 'Voltage', font=24)
        l3.pack(padx=10, pady=10)
        V = Entry(self, justify=CENTER, font=28)
        V.pack()

        def reset():
            I.delete(0, END)
            R.delete(0, END)
            V.delete(0, END)

        result = Button(self, text= 'Solve!', command=Voltage, font=24)
        result.pack(padx=10, pady=10)
        btnreset = Button(self, text="Reset", command=reset, font=26)
        btnreset.pack(padx=10, pady=10)
        home = tk.Button(self, text="Home", font=40, command=lambda: controller.show_frame(StartPage))
        home.place(relx=0.8, rely=0.8, relwidth=0.1, relheight=0.1)
        previous = tk.Button(self, text="Previous", font=40, command=lambda: controller.show_frame(PageTwo))
        previous.place(relx=0.1, rely=0.8, relwidth=0.1, relheight=0.1)
#Current Page for Ohm's Law
class PageTwoC(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Enter the Variables", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        def Current():
            I.delete(0, END)
            try:
                a = float(V.get())
                b = float(R.get())
                c = a/b
                c1 = round(c,4)
                I.insert(0, c1)
            except ValueError:
                error ="Invalid Input!"
                I.insert(0,error)
            except ZeroDivisionError:
                error = "Resistance must not be 0!"
                I.insert(0, error)


        l1 = Label(self, text='Enter the Voltage',font=24)
        l1.pack(padx=10, pady=10)
        V = Entry(self, justify=CENTER, font=28)
        V.pack()

        l2 = Label(self, text='Enter the Resistance',font=24)
        l2.pack(padx=10, pady=10)
        R = Entry(self, justify=CENTER, font=28)
        R.pack()

        l3  = Label(self, text = 'Current',font=24)
        l3.pack(padx=10, pady=10)
        I = Entry(self, justify=CENTER, font=28)
        I.pack()
        def reset():
            V.delete(0, END)
            R.delete(0, END)
            I.delete(0, END)


        result = Button(self, text= 'Solve!', command=Current,font=24)
        result.pack(padx=10, pady=10)
        btnreset = Button(self, text="Reset", command=reset, font=26)
        btnreset.pack(padx=10, pady=10)
        home = tk.Button(self, text="Home", font=40, command=lambda: controller.show_frame(StartPage))
        home.place(relx=0.8, rely=0.8, relwidth=0.1, relheight=0.1)
        previous = tk.Button(self, text="Previous", font=40, command=lambda: controller.show_frame(PageTwo))
        previous.place(relx=0.1, rely=0.8, relwidth=0.1, relheight=0.1)


#Resistance Page for Ohm's Law
class PageTwoR(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Enter the Variables", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        def Resistance():
            R.delete(0,END)
            try:
                a = float(V.get())
                b = float(I.get())
                c = a/b
                c1 = round(c, 4)
                R.insert(0, c1)
            except ValueError:
                error ="Invalid Input!"
                R.insert(0,error)
            except ZeroDivisionError:
                error = "Current must not be 0!"
                R.insert(0, error)
        l1 = Label(self, text='Enter the Voltage',font=24)
        l1.pack(padx=10, pady=10)
        V = Entry(self, justify=CENTER, font=28)
        V.pack()

        l2 = Label(self, text='Enter the Current',font=24)
        l2.pack(padx=10, pady=10)
        I = Entry(self, justify=CENTER, font=28)
        I.pack()

        l3  = Label(self, text = 'Resistance',font=24)
        l3.pack(padx=10, pady=10)
        R = Entry(self, justify=CENTER, font=28)
        R.pack()

        def reset():
            V.delete(0, END)
            I.delete(0, END)
            R.delete(0, END)

        result = Button(self, text= 'Solve!', command=Resistance,font=24)
        result.pack(padx=10, pady=10)
        btnreset = Button(self, text="Reset", command=reset, font=26)
        btnreset.pack(padx=10, pady=10)
        home = tk.Button(self, text="Home", font=40, command=lambda: controller.show_frame(StartPage))
        home.place(relx=0.8, rely=0.8, relwidth=0.1, relheight=0.1)
        previous = tk.Button(self, text="Previous", font=40, command=lambda: controller.show_frame(PageTwo))
        previous.place(relx=0.1, rely=0.8, relwidth=0.1, relheight=0.1)


#Conductance Homepage
class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Conductance Calculator", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="Series", font=40, command=lambda: controller.show_frame(PageThreeS))
        button1.place(relx=0.35, rely=0.13, relwidth=0.3, relheight=0.2)
        button2 = tk.Button(self, text="Parallel", font=40, command=lambda: controller.show_frame(PageThreeP))
        button2.place(relx=0.35, rely=0.35, relwidth=0.3, relheight=0.2)
        home = tk.Button(self, text="Home", font=40, command=lambda: controller.show_frame(StartPage))
        home.place(relx=0.8, rely=0.7, relwidth=0.1, relheight=0.1)

#Series Page for Conductance
class PageThreeS(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Series Conductance", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        entries = []
        sum = StringVar()
        sum.set(0)
        def addVariable():
            entry = DoubleVar()
            entries.append(entry)
            row = len(entries)
            l1 = Label(self, text=f' Enter the Conductance {row} ', font=20)
            l1.pack()
            e1 = Entry(self, textvariable=entry, width=10, font=26, justify=CENTER)
            e1.pack()
        addVariable()
        def computeSum():
            l.delete(0,END)
            sum = 0
            try:
                for var in entries:
                    sum += var.get()
                sum1 = float(sum)
                sum2 = round(sum1, 4)
                l.insert(0, sum2)
            except:
                error = "Invalid Input!"
                l.insert(0, error)


        def resetVariables():
            l.delete(0, END)
            for var in entries:
                var.set(0.0)

        b1 = Button(self, text='Add Variable', command=addVariable, font=24)
        b1.place(relx=0.15, rely=0.125, relwidth=0.2, relheight=0.085)
        b2 = Button(self, text='Reset Variables', command=resetVariables, font=20)
        b2.place(relx=0.15, rely=0.225, relwidth=0.2, relheight=0.085)
        b3 = Button(self, text='Solve', command=computeSum, font=20)
        b3.place(relx=0.15, rely=0.325, relwidth=0.2, relheight=0.085)
        lb = Label(self, text="The total", font=20)
        lb.place(relx=0.15, rely=0.425, relwidth=0.2, relheight=0.04)
        lb2 = Label(self, text="Conductance is:", font=20)
        lb2.place(relx=0.15, rely=0.47, relwidth=0.2, relheight=0.04)
        l = Entry(self, font=24, justify=CENTER)
        l.place(relx=0.15, rely=0.525, relwidth=0.2, relheight=0.075)
        home = tk.Button(self, text="Home", font=40, command=lambda: controller.show_frame(StartPage))
        home.place(relx=0.8, rely=0.8, relwidth=0.1, relheight=0.1)
        previous = tk.Button(self, text="Previous", font=40, command=lambda: controller.show_frame(PageThree))
        previous.place(relx=0.1, rely=0.8, relwidth=0.1, relheight=0.1)

#Parallel Page for Conductance
class PageThreeP(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Parallel Conductance", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        entries = []
        sum = StringVar()
        sum.set(0)
        def addVariable():
            entry = DoubleVar()
            entries.append(entry)
            row = len(entries)
            l1 = Label(self, text=f' Enter the Conductance {row} ', font=20)
            l1.pack()
            e1 = Entry(self, textvariable=entry, width=20, font=26, justify=CENTER)
            e1.pack()
        addVariable()
        def computeSum():
            l.delete(0, END)
            sum = 0
            try:
                for var in entries:
                    sum += 1 / var.get()
                sum1 = 1 / sum
                sum1 = float(sum1)
                sum2 = round(sum1, 4)
                l.insert(0, sum2)
            except ZeroDivisionError:
                error = "Variable must not be 0!"
                l.insert(0, error)
            except:
                error = "Invalid Input!"
                l.insert(0, error)
        def resetVariables():
            l.delete(0, END)
            for var in entries:
                var.set(0.0)
        b1 = Button(self, text='Add Variable', command=addVariable,font=24)
        b1.place(relx=0.15, rely=0.125, relwidth=0.2, relheight=0.085)
        b2 = Button(self, text='Reset Variables', command=resetVariables, font=24)
        b2.place(relx=0.15, rely=0.225, relwidth=0.2, relheight=0.085)
        b3 = Button(self, text='Solve', command=computeSum, font=20)
        b3.place(relx=0.15, rely=0.325, relwidth=0.2, relheight=0.085)
        lb = Label(self, text="The total", font=20)
        lb.place(relx=0.15, rely=0.425, relwidth=0.2, relheight=0.04)
        lb2 = Label(self, text="Conductance is:", font=20)
        lb2.place(relx=0.15, rely=0.47, relwidth=0.2, relheight=0.04)
        l = Entry(self, font=24, justify=CENTER)
        l.place(relx=0.15, rely=0.525, relwidth=0.2, relheight=0.075)
        home = tk.Button(self, text="Home", font=40, command=lambda: controller.show_frame(StartPage))
        home.place(relx=0.8, rely=0.8, relwidth=0.1, relheight=0.1)
        previous = tk.Button(self, text="Previous", font=40, command=lambda: controller.show_frame(PageThree))
        previous.place(relx=0.1, rely=0.8, relwidth=0.1, relheight=0.1)

#Capacitance Homepage
class PageFour(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Capacitance Calculator", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Series", font=40, command=lambda: controller.show_frame(PageFourS))
        button1.place(relx=0.35, rely=0.13, relwidth=0.3, relheight=0.2)
        button2 = tk.Button(self, text="Parallel", font=40, command=lambda: controller.show_frame(PageFourP))
        button2.place(relx=0.35, rely=0.35, relwidth=0.3, relheight=0.2)
        home = tk.Button(self, text="Home", font=40, command=lambda: controller.show_frame(StartPage))
        home.place(relx=0.8, rely=0.8, relwidth=0.1, relheight=0.1)

#Series Page for Capacitance

class PageFourS(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Series Capacitance", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        entries = []
        sum = StringVar()
        sum.set(0)
        def addVariable():
            entry = DoubleVar()
            entries.append(entry)
            row = len(entries)
            l1 = Label(self, text=f' Enter the Capacitance {row} ', font=20)
            l1.pack()
            e1 = Entry(self, textvariable=entry, width=20,font=26, justify=CENTER)
            e1.pack()
        addVariable()
        def computeSum():
            l.delete(0, END)
            sum = 0
            try:
                for var in entries:
                    sum += 1 / var.get()
                sum1 = 1 / sum
                sum1 = float(sum1)
                sum2 = round(sum1, 4)
                l.insert(0, sum2)
            except ZeroDivisionError:
                error = "Variable must not be 0!!"
                l.insert(0, error)
            except:
                error = "Invalid Input!"
                l.insert(0, error)

        def resetVariables():
            l.delete(0, END)
            for var in entries:
                var.set(0.0)
        b1 = Button(self, text='Add Variable', command=addVariable, font=24)
        b1.place(relx=0.15, rely=0.125, relwidth=0.2, relheight=0.085)
        b2 = Button(self, text='Reset Variables', command=resetVariables,font=20)
        b2.place(relx=0.15, rely=0.225, relwidth=0.2, relheight=0.085)
        b3 = Button(self, text='Solve', command=computeSum, font=20)
        b3.place(relx=0.15, rely=0.325, relwidth=0.2, relheight=0.085)
        lb = Label(self, text="The total", font=20)
        lb.place(relx=0.15, rely=0.425, relwidth=0.2, relheight=0.04)
        lb2 = Label(self, text="Capacitance is:",font=20)
        lb2.place(relx=0.15, rely=0.47, relwidth=0.2, relheight=0.04)
        l = Entry(self, font=24, justify=CENTER)
        l.place(relx=0.15, rely=0.525, relwidth=0.2, relheight=0.075)
        home = tk.Button(self, text="Home", font=40, command=lambda: controller.show_frame(StartPage))
        home.place(relx=0.8, rely=0.8, relwidth=0.1, relheight=0.1)
        previous = tk.Button(self, text="Previous", font=40, command=lambda: controller.show_frame(PageFour))
        previous.place(relx=0.1, rely=0.8, relwidth=0.1, relheight=0.1)

#Parallel page for Capacitance
class PageFourP(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Parallel Capacitance", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        entries = []
        sum = StringVar()
        sum.set(0)
        def addVariable():
            entry = DoubleVar()
            entries.append(entry)
            row = len(entries)
            l1 = Label(self, text=f' Enter the Capacitance {row} ',font=20).pack()
            e1 = Entry(self, textvariable=entry, width=20, font=26, justify=CENTER).pack()
        addVariable()
        def computeSum():
            l.delete(0, END)
            sum = 0
            try:
                for var in entries:
                    sum += var.get()
                sum1 = float(sum)
                sum2 = round(sum1, 4)
                l.insert(0, sum2)
            except:
                error = "Invalid Input!"
                l.insert(0, error)

        def resetVariables():
            l.delete(0, END)
            for var in entries:
                var.set(0.0)
        b1 = Button(self, text='Add Variable', command=addVariable, font=24)
        b1.place(relx=0.15, rely=0.125, relwidth=0.2, relheight=0.085)
        b2 = Button(self, text='Reset Variables', command=resetVariables,font=20)
        b2.place(relx=0.15, rely=0.225, relwidth=0.2, relheight=0.085)
        b3 = Button(self, text='Solve', command=computeSum, font=20)
        b3.place(relx=0.15, rely=0.325, relwidth=0.2, relheight=0.085)
        lb = Label(self, text="The total", font=20)
        lb.place(relx=0.15, rely=0.425, relwidth=0.2, relheight=0.04)
        lb2 = Label(self, text="Capacitance is:", font=20)
        lb2.place(relx=0.15, rely=0.47, relwidth=0.2, relheight=0.04)
        l = Entry(self, font=24, justify=CENTER)
        l.place(relx=0.15, rely=0.525, relwidth=0.2, relheight=0.075)
        home = tk.Button(self, text="Home", font=40, command=lambda: controller.show_frame(StartPage))
        home.place(relx=0.8, rely=0.8, relwidth=0.1, relheight=0.1)
        previous = tk.Button(self, text="Previous", font=40, command=lambda: controller.show_frame(PageFour))
        previous.place(relx=0.1, rely=0.8, relwidth=0.1, relheight=0.1)

#Current Divider Page
class PageFive(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Current Divider", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        def CDR():
            t4.delete(0,END)
            try:
                a = float(t1.get())
                b = float(t2.get())
                c = float(t3.get())
                d = float(c * (a / (a + b)))
                d1 = round(d, 4)
                t4.insert(0, d1)
            except ZeroDivisionError:
                error= 'Resistors must not be 0!'
                t4.insert(0, error)
            except ValueError:
                error = "Invalid Input!"
                t4.insert(0, error)
        def reset():
            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)
            t4.delete(0, END)

        l1 = Label(self,text="R1", font=24)
        l1.pack(padx=10, pady=10)
        t1 = Entry(self, justify=CENTER, font=28)
        t1.pack()

        l2 = Label(self,text="R2", font=24)
        l2.pack(padx=10, pady=10)
        t2 = Entry(self, justify=CENTER, font=28)
        t2.pack()
        l3 = Label(self,text="Current", font=24)
        l3.pack(padx=10, pady=10)
        t3 = Entry(self, justify=CENTER, font=28)
        t3.pack()

        l4 = Label(self,text="Result",font=24)
        l4.pack(padx=10, pady=10)
        t4 = Entry(self, justify=CENTER, font=28)
        t4.pack()
        b1 = Button(self,text="Solve", command=CDR,font=24)
        b1.pack(padx=10, pady=10)
        btnreset = Button(self, text="Reset", command=reset, font=26)
        btnreset.pack(padx=10, pady=10)
        home = tk.Button(self, text="Home", font=40, command=lambda: controller.show_frame(StartPage))
        home.place(relx=0.8, rely=0.8, relwidth=0.1, relheight=0.1)



#Voltage Divider
class PageSix(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Voltage Divider", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        def VDR():
            try:
                t4.delete(0,END)
                a=float(t1.get())
                b=float(t2.get())
                c=float(t3.get())
                d= float(c*(b/(a+b)))
                d1 = round(d,4)
                t4.insert(0,d1)
            except ValueError:
                error= "Invalid Input!"
                t4.insert(0,error)
            except ZeroDivisionError:
                error= 'Resistors must not be 0!'
                t4.insert(0,error)
        def reset():
            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)
            t4.delete(0, END)

        l1=Label(self,text="R1", font=24)
        l1.pack(padx=10, pady=10)
        t1=Entry(self, justify=CENTER, font=28)
        t1.pack()

        l2=Label(self,text="R2", font=24)
        l2.pack(padx=10, pady=10)
        t2=Entry(self, justify=CENTER, font=28)
        t2.pack()

        l3=Label(self,text="Voltage", font=24)
        l3.pack(padx=10, pady=10)
        t3=Entry(self, justify=CENTER, font=28)
        t3.pack()

        l4=Label(self,text="Result", font=24)
        l4.pack(padx=10, pady=10)
        t4=Entry(self, justify=CENTER, font=28)
        t4.pack()

        b1=Button(self,text="Solve",command=VDR, font=24)
        b1.pack(padx=10, pady=10)
        btnreset = Button(self, text="Reset", command=reset, font=26)
        btnreset.pack(padx=10, pady=10)
        home = tk.Button(self, text="Home", font=40, command=lambda: controller.show_frame(StartPage))
        home.place(relx=0.8, rely=0.8, relwidth=0.1, relheight=0.1)

#KCL Page
class PageSeven(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="KCL Calculator (1 node only) (1 unknown)", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        entries = []  # entering
        sum = StringVar()
        sum.set(0)
        def addVariable():
            entry = DoubleVar()
            entries.append(entry)
            row = len(entries)
            l1 = Label(self, text=f' Enter the Current entering {row} ', font=20).pack()
            e1 = Entry(self, textvariable=entry, width=20, font=26, justify=CENTER)
            e1.pack()
        addVariable()

        entries2 = []  # leaving
        plus = StringVar()
        plus.set(0)
        def addVariable2():
            entry = DoubleVar()
            entries2.append(entry)
            row = len(entries2)
            l1 = Label(self, text=f'Enter the Current leaving {row}', font=20).pack()
            e1 = Entry(self, textvariable=entry, width=20, font=26, justify=CENTER)
            e1.pack()
        addVariable2()
        def addVariable3():
            result.delete(0, END)
            c = []  # enter node
            c2 = []  # leaving node
            def current():
                sum = 0
                plus = 0
                try:
                    for var in entries:
                        sum += var.get()
                    for var in entries2:
                        plus += var.get()
                    c.append(sum)
                    c2.append(plus)
                except:
                    error = "Invalid Input!"
                    result.insert(0, error)
            current()
            def kcl():
                kcl1 = c2[0] - c[0]
                kcl1 = round(kcl1, 3)
                result.insert(0, kcl1)
            kcl()
        def addVariable4():
            result.delete(0, END)
            c = []
            c2 = []
            def current():
                sum = 0
                plus = 0
                try:
                    for var in entries:
                        sum += var.get()
                    for var in entries2:
                        plus += var.get()
                    c.append(sum)
                    c2.append(plus)
                except:
                    error = "Invalid Input!"
                    result.insert(0, error)
            current()
            def kcl():
                kcl1 = -c2[0] + c[0]
                kcl1 = round(kcl1, 3)
                result.insert(0, kcl1)
            kcl()

        def resetVariables():
            lb4 = Label(self, text="The Current leaving ", font=20)
            lb4.place(relx=0.7, rely=0.28, relwidth=0.2, relheight=0.04)
            lb5 = Label(self, text=" the node is:", font=20)
            lb5.place(relx=0.7, rely=0.32, relwidth=0.2, relheight=0.04)
            result.delete(0, END)
            for var in entries:
                var.set(0.0)
            for var in entries2:
                var.set(0.0)

        b1 = Button(self, text='Add entering current', command=addVariable, font=20)
        b1.place(relx=0.1, rely=0.12, relwidth=0.18, relheight=0.075)
        b11 = Button(self, text='Add leaving current', command=addVariable2, font=20)
        b11.place(relx=0.1, rely=0.20, relwidth=0.18, relheight=0.075)
        bEx = Button(self, text='Find the unknown entering current', command=addVariable3, font=20)
        bEx.place(relx=0.05, rely=0.28, relwidth=0.30, relheight=0.075)
        bLx = Button(self, text='Find the unknown leaving current', command=addVariable4, font=20)
        bLx.place(relx=0.05, rely=0.38, relwidth=0.30, relheight=0.075)
        b2 = Button(self, text='Reset Variables', command=resetVariables, font=20)
        b2.place(relx=0.7, rely=0.12, relwidth=0.18, relheight=0.075)
        lb = Label(self, text="The unknown ", font=20)
        lb.place(relx=0.7, rely=0.28, relwidth=0.2, relheight=0.04)
        lb2 = Label(self, text=" Current is:", font=20)
        lb2.place(relx=0.7, rely=0.32, relwidth=0.2, relheight=0.04)
        result = Entry(self, font=26, justify=CENTER)
        result.place(relx=0.7, rely=0.38, relwidth=0.18, relheight=0.075)
        home = tk.Button(self, text="Home", font=40, command=lambda: controller.show_frame(StartPage))
        home.place(relx=0.8, rely=0.8, relwidth=0.1, relheight=0.1)

#KVL Page
class PageEight(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="KVL in 1 loop (Series) (Current is unknown)", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        # voltage
        entries = []
        sum = StringVar()
        sum.set(0)
        # resistance
        entries2 = []
        plus = StringVar()
        plus.set(0)
        def addVariable():
            entry = DoubleVar()
            entries.append(entry)
            row = len(entries)
            l1 = Label(self, text=f' Enter the Voltage {row} ', font=20).pack()
            e1 = Entry(self, textvariable=entry, width=20, font=26, justify=CENTER)
            e1.pack()
        addVariable()
        def addVariable2():
            entry2 = DoubleVar()
            entries2.append(entry2)
            row = len(entries2)
            l1 = Label(self, text=f' Enter the Resistance {row} ', font=20).pack()
            e1 = Entry(self, textvariable=entry2, width=20, font=26, justify=CENTER)
            e1.pack()
        def Solve():
            result.delete(0, END)
            v = []
            def voltage():
                sum = 0
                try:
                    for var in entries:
                        sum += var.get()
                    v.append(sum)
                except:
                    error = "Invalid Input!"
                    result.insert(0, error)
            voltage()
            r = []
            def resistance():
                plus = 0
                try:
                    for var in entries2:
                        plus += var.get()
                    r.append(plus)
                except:
                    error = "Invalid Input!"
                    result.insert(0, error)

            resistance()
            try:
                kvl = -v[0] / r[0]
                kvl1 = round(kvl, 4)
                result.insert(0, kvl1)
            except ZeroDivisionError:
                def voltage():
                    sum = 0
                    try:
                        for var in entries:
                            sum += var.get()
                        sum1 = round(sum, 4)
                        result.insert(0, sum1)

                    except:
                        result.delete(0,END)
                        error = "Invalid Input!"
                        result.insert(0, error)
                    lb = Label(self, text="The total", font=20)
                    lb.place(relx=0.7, rely=0.28, relwidth=0.2, relheight=0.04)
                    lb2 = Label(self, text="voltage is:", font=20)
                    lb2.place(relx=0.7, rely=0.32, relwidth=0.2, relheight=0.04)
                voltage()
        def resetVariables():
            lb4 = Label(self, text="The Current in ", font=20)
            lb4.place(relx=0.7, rely=0.28, relwidth=0.2, relheight=0.04)
            lb5 = Label(self, text=" the loop is:", font=20)
            lb5.place(relx=0.7, rely=0.32, relwidth=0.2, relheight=0.04)
            result.delete(0, END)
            for var in entries:
                var.set(0.0)
            for var in entries2:
                var.set(0.0)
        b1 = Button(self, text='Add Voltage Source', command=addVariable, font=20)
        b1.place(relx=0.1, rely=0.12, relwidth=0.18, relheight=0.075)
        b11 = Button(self, text='Add Resistors', command=addVariable2, font=20)
        b11.place(relx=0.1, rely=0.20, relwidth=0.18, relheight=0.075)
        b2 = Button(self, text='Reset Variables', command=resetVariables, font=20)
        b2.place(relx=0.7, rely=0.12, relwidth=0.18, relheight=0.075)
        b31 = Button(self, text='Solve', command=Solve, font=20)
        b31.place(relx=0.7, rely=0.20, relwidth=0.18, relheight=0.075)
        lb = Label(self, text="The Current in ", font=20)
        lb.place(relx=0.7, rely=0.28, relwidth=0.2, relheight=0.04)
        lb2 = Label(self, text=" the loop is:", font=20)
        lb2.place(relx=0.7, rely=0.32, relwidth=0.2, relheight=0.04)
        result = Entry(self, font=26, justify=CENTER)
        result.place(relx=0.7, rely=0.38, relwidth=0.18, relheight=0.075)
        home = tk.Button(self, text="Home", font=40, command=lambda: controller.show_frame(StartPage))
        home.place(relx=0.8, rely=0.8, relwidth=0.1, relheight=0.1)
#Power Consumption Calculator
class PageNine(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Power Consumption Calculator", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Cost", font=40,command=lambda: controller.show_frame(PageNineC))
        button1.place(relx=0.35, rely=0.13, relwidth=0.3, relheight=0.2)

        button2 = tk.Button(self, text="Rate", font=40, command=lambda: controller.show_frame(PageNineR))
        button2.place(relx=0.35, rely=0.35, relwidth=0.3, relheight=0.2)

        button3 = tk.Button(self, text="Power", font=40, command=lambda: controller.show_frame(PageNineP))
        button3.place(relx=0.35, rely=0.57, relwidth=0.3, relheight=0.2)

        button4 = tk.Button(self, text="Time", font=40, command=lambda: controller.show_frame(PageNineT))
        button4.place(relx=0.35, rely=0.79, relwidth=0.3, relheight=0.2)

        home = tk.Button(self, text="Home", font=40, command=lambda: controller.show_frame(StartPage))
        home.place(relx=0.8, rely=0.8, relwidth=0.1, relheight=0.1)

#Cost Page for Power Consumption Calculator
class PageNineC(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Enter the Variables", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        def Cost():
            cost.delete(0, END)
            try:
                a = float(r.get())
                b = float(p.get())
                c = float(t.get())
                d = a*b*c
                d1 = round(d,4)
                cost.insert(0, d1)
            except ValueError:
                error= 'Invalid Input'
                cost.insert(0,error)

        def reset():
            r.delete(0, END)
            p.delete(0, END)
            t.delete(0, END)
            cost.delete(0, END)

        l1 = Label(self, text="What's the rate?", font=24)
        l1.pack(padx=10, pady=10)
        r = Entry(self, justify=CENTER, font=28)
        r.pack()

        l2 = Label(self, text="What's the power reading? (kW)", font=24)
        l2.pack(padx=10, pady=10)
        p = Entry(self, justify=CENTER, font=28)
        p.pack()

        l3 = Label(self, text="What's the time? (hr) ", font=24)
        l3.pack(padx=10, pady=10)
        t = Entry(self, justify=CENTER, font=28)
        t.pack()

        l4 = Label(self, text="The cost is", font=24)
        l4.pack(padx=10, pady=10)
        cost = Entry(self, justify=CENTER, font=28)
        cost.pack()

        result = Button(self, text='Solve!', command=Cost, font=24)
        result.pack(padx=10, pady=10)
        btnreset = Button(self, text="Reset", command=reset, font=26)
        btnreset.pack(padx=10, pady=10)
        home = tk.Button(self, text="Home", font=40, command=lambda: controller.show_frame(StartPage))
        home.place(relx=0.8, rely=0.8, relwidth=0.1, relheight=0.1)
        previous = tk.Button(self, text="Previous", font=40, command=lambda: controller.show_frame(PageNine))
        previous.place(relx=0.1, rely=0.8, relwidth=0.1, relheight=0.1)

#Rate Page for Power Consumption Calculator
class PageNineR(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Enter the Variables", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        def Rate():
            rate.delete(0, END)
            try:
                a = float(c1.get())
                b = float(p.get())
                c = float(t.get())
                d = a/(b*c)
                d1= round(d,4)
                rate.insert(0, d1)
            except ValueError:
                error= 'Invalid Input'
                rate.insert(0,error)
            except ZeroDivisionError:
                error= 'Division by 0 error'
                rate.insert(0,error)
        def reset():
            c1.delete(0, END)
            p.delete(0, END)
            t.delete(0, END)
            rate.delete(0, END)

        l1 = Label(self, text="What's the cost?", font=24)
        l1.pack(padx=10, pady=10)
        c1 = Entry(self, justify=CENTER, font=28)
        c1.pack()

        l2 = Label(self, text="What's the power reading? (kW)", font=24)
        l2.pack(padx=10, pady=10)
        p = Entry(self, justify=CENTER, font=28)
        p.pack()

        l3 = Label(self, text="What's the time? (hr) ", font=24)
        l3.pack(padx=10, pady=10)
        t = Entry(self, justify=CENTER, font=28)
        t.pack()

        l4 = Label(self, text="The rate is", font=24)
        l4.pack(padx=10, pady=10)
        rate = Entry(self, justify=CENTER, font=28)
        rate.pack()

        result = Button(self, text='Solve!', command=Rate, font=24)
        result.pack()
        btnreset = Button(self, text="Reset", command=reset, font=26)
        btnreset.pack(padx=10, pady=10)
        home = tk.Button(self, text="Home", font=40, command=lambda: controller.show_frame(StartPage))
        home.place(relx=0.8, rely=0.8, relwidth=0.1, relheight=0.1)
        previous = tk.Button(self, text="Previous", font=40, command=lambda: controller.show_frame(PageNine))
        previous.place(relx=0.1, rely=0.8, relwidth=0.1, relheight=0.1)

#Power Page for Power Consumption Calculator
class PageNineP(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Enter the Variables", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        def Power():
            power.delete(0, END)
            try:
                a = float(c1.get())
                b = float(r.get())
                c = float(t.get())
                d = a/(b*c)
                d1 = round(d,4)
                power.insert(0, d1)
            except ValueError:
                error= 'Invalid Input'
                power.insert(0,error)
            except ZeroDivisionError:
                error = 'Division by 0 error'
                power.insert(0, error)
        def reset():
            c1.delete(0, END)
            r.delete(0, END)
            t.delete(0, END)
            power.delete(0, END)

        l1 = Label(self, text="What's the cost?", font=24)
        l1.pack(padx=10, pady=10)
        c1 = Entry(self, justify=CENTER, font=28)
        c1.pack()

        l2 = Label(self, text="What's the rate? ", font=24)
        l2.pack(padx=10, pady=10)
        r = Entry(self, justify=CENTER, font=28)
        r.pack()

        l3 = Label(self, text="What's the time? (hr)", font=24)
        l3.pack(padx=10, pady=10)
        t = Entry(self, justify=CENTER, font=28)
        t.pack()

        l4 = Label(self, text="The power is", font=24)
        l4.pack(padx=10, pady=10)
        power = Entry(self, justify=CENTER, font=28)
        power.pack()

        result = Button(self, text='Solve!', command=Power, font=24)
        result.pack(padx=10, pady=10)
        btnreset = Button(self, text="Reset", command=reset, font=26)
        btnreset.pack(padx=10, pady=10)
        home = tk.Button(self, text="Home", font=40, command=lambda: controller.show_frame(StartPage))
        home.place(relx=0.8, rely=0.8, relwidth=0.1, relheight=0.1)
        previous = tk.Button(self, text="Previous", font=40, command=lambda: controller.show_frame(PageNine))
        previous.place(relx=0.1, rely=0.8, relwidth=0.1, relheight=0.1)

#Time Page for Power Consumption Calculator
class PageNineT(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Enter the Variables", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        def Time():
            time.delete(0, END)
            try:
                a = float(c1.get())
                b = float(r.get())
                c = float(p.get())
                d = a/(b*c)
                d1 = round(d,4)
                time.insert(0, d1)
            except ValueError:
                error= 'Invalid Input'
                time.insert(0,error)
            except ZeroDivisionError:
                error = 'Division by 0 error'
                time.insert(0, error)
        def reset():
            c1.delete(0, END)
            r.delete(0, END)
            p.delete(0, END)
            time.delete(0, END)

        l1 = Label(self, text="What's the cost?", font=24)
        l1.pack(padx=10, pady=10)
        c1 = Entry(self, justify=CENTER, font=28)
        c1.pack()

        l2 = Label(self, text="What's the rate? ", font=24)
        l2.pack(padx=10, pady=10)
        r = Entry(self, justify=CENTER, font=28)
        r.pack()

        l3 = Label(self, text="What's the power reading? (kW)", font=24)
        l3.pack(padx=10, pady=10)
        p = Entry(self, justify=CENTER, font=28)
        p.pack()

        l4 = Label(self, text="The time is", font=24)
        l4.pack(padx=10, pady=10)
        time = Entry(self, justify=CENTER, font=28)
        time.pack()

        result = Button(self, text='Solve!', command=Time, font=24)
        result.pack(padx=10, pady=10)
        btnreset = Button(self, text="Reset", command=reset, font=26)
        btnreset.pack(padx=10, pady=10)
        home = tk.Button(self, text="Home", font=40, command=lambda: controller.show_frame(StartPage))
        home.place(relx=0.8, rely=0.8, relwidth=0.1, relheight=0.1)
        previous = tk.Button(self, text="Previous", font=40, command=lambda: controller.show_frame(PageNine))
        previous.place(relx=0.1, rely=0.8, relwidth=0.1, relheight=0.1)

app = back()
app.mainloop()
