from tkinter import *
import math


class Calculator:
    def __init__(self):
        root = Tk()
        root.title('Smart Calculator')
        root.config(bg='black')
        root.geometry('680x486+100+100')
        self.root = root

        self.entryField = Entry(root, font=('arial', 20, 'bold'), bg='gray', fg='white', bd=10, relief=SUNKEN, width=40)
        self.entryField.grid(row=0, column=0, columnspan=8)

        button_text_list = ["C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ",
                            "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
                            "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
                            "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
                            "0", ".", "%", "=", "log₁₀", "(", ")", "x!"]

        row_value = 1
        column_value = 0
        for i in button_text_list:

            button = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text=i, bg='gray', fg='white',
                            font=('arial', 18, 'bold'), command=lambda button=i: self.click(button))
            button.grid(row=row_value, column=column_value, pady=1)
            column_value += 1
            if column_value > 7:
                row_value += 1
                column_value = 0

    def click(self, value):
        ex = self.entryField.get()
        answer = ''

        try:

            if value == 'C':
                ex = ex[0:len(ex) - 1]
                self.entryField.delete(0, END)
                self.entryField.insert(0, ex)
                return

            elif value == 'CE':
                self.entryField.delete(0, END)

            elif value == '√':
                answer = math.sqrt(eval(ex))

            elif value == 'π':
                answer = math.pi

            elif value == 'cosθ':
                answer = math.cos(math.radians(eval(ex)))

            elif value == 'tanθ':
                answer = math.tan(math.radians(eval(ex)))

            elif value == 'sinθ':
                answer = math.sin(math.radians(eval(ex)))

            elif value == '2π':
                answer = 2 * math.pi

            elif value == 'cosh':
                answer = math.cosh(eval(ex))

            elif value == 'tanh':
                answer = math.tanh(eval(ex))

            elif value == 'sinh':
                answer = math.sinh(eval(ex))

            elif value == chr(8731):
                answer = eval(ex) ** (1 / 3)

            elif value == 'x\u02b8':  # 7**2
                self.entryField.insert(END, '**')
                return

            elif value == 'x\u00B3':
                answer = eval(ex) ** 3

            elif value == 'x\u00B2':
                answer = eval(ex) ** 2

            elif value == 'ln':
                answer = math.log2(eval(ex))

            elif value == 'deg':
                answer = math.degrees(eval(ex))

            elif value == "rad":
                answer = math.radians(eval(ex))

            elif value == 'e':
                answer = math.e

            elif value == 'log₁₀':
                answer = math.log10(eval(ex))

            elif value == 'x!':
                answer = math.factorial(ex)

            elif value == chr(247):
                self.entryField.insert(END, "/")
                return

            elif value == '=':
                answer = eval(ex)

            else:
                self.entryField.insert(END, value)
                return

            self.entryField.delete(0, END)
            self.entryField.insert(0, answer)

        except SyntaxError:
            pass

    def start(self):
        self.root.mainloop()


calculator = Calculator()

calculator.start()
