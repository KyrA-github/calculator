import customtkinter as CTK
class App(CTK.CTk, ):
    number_click = 1
    time_i = 1
    time_s = 100
    f = 0

    def __init__(self):
        super().__init__()

        self.geometry("305x455+600+350")

        self.title("Сalculator")

        self.resizable(False, False)

        self.set = CTK.CTkEntry(self, height=70, width=295, justify="right",font=("Arial", 50))
        self.set.place(x=5, y=5)

        self.btn0 = CTK.CTkButton(self, text="0", width=145, height=70, fg_color="#483D80", hover_color="#553D81", command=self.btn0q)
        self.btn1 = CTK.CTkButton(self, text="1", width=70, height=70, fg_color="#483D80", hover_color="#553D81", command=self.btn1q)
        self.btn2 = CTK.CTkButton(self, text="2", width=70, height=70, fg_color="#483D80", hover_color="#553D81", command=self.btn2q)
        self.btn3 = CTK.CTkButton(self, text="3", width=70, height=70, fg_color="#483D80", hover_color="#553D81", command=self.btn3q)
        self.btn4 = CTK.CTkButton(self, text="4", width=70, height=70, fg_color="#483D80", hover_color="#553D81", command=self.btn4q)
        self.btn5 = CTK.CTkButton(self, text="5", width=70, height=70, fg_color="#483D80", hover_color="#553D81", command=self.btn5q)
        self.btn6 = CTK.CTkButton(self, text="6", width=70, height=70, fg_color="#483D80", hover_color="#553D81", command=self.btn6q)
        self.btn7 = CTK.CTkButton(self, text="7", width=70, height=70, fg_color="#483D80", hover_color="#553D81", command=self.btn7q)
        self.btn8 = CTK.CTkButton(self, text="8", width=70, height=70, fg_color="#483D80", hover_color="#553D81", command=self.btn8q)
        self.btn9 = CTK.CTkButton(self, text="9", width=70, height=70, fg_color="#483D80", hover_color="#553D81", command=self.btn9q)
        self.btn10 = CTK.CTkButton(self, text=".", width=70, height=70, fg_color="#483D80", hover_color="#553D81", command=self.btn10q)
        self.btn11 = CTK.CTkButton(self, text="+", width=70, height=70, fg_color="#483D80", hover_color="#553D81", command=self.btn11q)
        self.btn12 = CTK.CTkButton(self, text="-", width=70, height=70, fg_color="#483D80", hover_color="#553D81", command=self.btn12q)
        self.btn13 = CTK.CTkButton(self, text="=", width=70, height=145, fg_color="#883D80", hover_color="#783D80", command=self.schet)
        self.btn14 = CTK.CTkButton(self, text="*", width=70, height=70, fg_color="#483D80", hover_color="#553D81", command=self.btn13q)
        self.btn15 = CTK.CTkButton(self, text="C", width=70, height=70, fg_color="#483D80", hover_color="#553D81", command=self.C)
        self.btn16 = CTK.CTkButton(self, text="AC", width=70, height=70, fg_color="#483D80", hover_color="#553D81", command=self.AC)
        self.btn17 = CTK.CTkButton(self, text="/", width=70, height=70, fg_color="#483D80", hover_color="#553D81", command=self.btn14q)

        self.btn0.place(x=5, y=380)
        self.btn1.place(x=5, y=305)
        self.btn2.place(x=80, y=305)
        self.btn3.place(x=155, y=305)
        self.btn4.place(x=5, y=230)
        self.btn5.place(x=80, y=230)
        self.btn6.place(x=155, y=230)
        self.btn7.place(x=5, y=155)
        self.btn8.place(x=80, y=155)
        self.btn9.place(x=155, y=155)
        self.btn10.place(x=155, y=380)
        self.btn11.place(x=230, y=230)
        self.btn12.place(x=230, y=155)
        self.btn13.place(x=230, y=305)
        self.btn14.place(x=230, y=80)
        self.btn15.place(x=5, y=80)
        self.btn16.place(x=80, y=80)
        self.btn17.place(x=155, y=80)

    def btn0q(self):
        current_text1 = str(self.set.get())
        if current_text1 == "Erorr":
            self.set.delete(0, CTK.END)
        letter = "0"
        current_text = self.set.get()
        new_text = current_text + letter
        self.set.delete(0, CTK.END)
        self.set.insert(0, new_text)

    def btn1q(self):
        current_text1 = str(self.set.get())
        if current_text1 == "Erorr":
            self.set.delete(0, CTK.END)
        letter = "1"
        current_text = self.set.get()
        new_text = current_text + letter
        self.set.delete(0, CTK.END)
        self.set.insert(0, new_text)

    def btn2q(self):
        current_text1 = str(self.set.get())
        if current_text1 == "Erorr":
            self.set.delete(0, CTK.END)
        letter = "2"
        current_text = self.set.get()
        new_text = current_text + letter
        self.set.delete(0, CTK.END)
        self.set.insert(0, new_text)

    def btn3q(self):
        current_text1 = str(self.set.get())
        if current_text1 == "Erorr":
            self.set.delete(0, CTK.END)
        letter = "3"
        current_text = self.set.get()
        new_text = current_text + letter
        self.set.delete(0, CTK.END)
        self.set.insert(0, new_text)

    def btn4q(self):
        current_text1 = str(self.set.get())
        if current_text1 == "Erorr":
            self.set.delete(0, CTK.END)
        letter = "4"
        current_text = self.set.get()
        new_text = current_text + letter
        self.set.delete(0, CTK.END)
        self.set.insert(0, new_text)

    def btn5q(self):
        current_text1 = str(self.set.get())
        if current_text1 == "Erorr":
            self.set.delete(0, CTK.END)
        letter = "5"
        current_text = self.set.get()
        new_text = current_text + letter
        self.set.delete(0, CTK.END)
        self.set.insert(0, new_text)

    def btn6q(self):
        current_text1 = str(self.set.get())
        if current_text1 == "Erorr":
            self.set.delete(0, CTK.END)
        letter = "6"
        current_text = self.set.get()
        new_text = current_text + letter
        self.set.delete(0, CTK.END)
        self.set.insert(0, new_text)

    def btn7q(self):
        current_text1 = str(self.set.get())
        if current_text1 == "Erorr":
            self.set.delete(0, CTK.END)
        letter = "7"
        current_text = self.set.get()
        new_text = current_text + letter
        self.set.delete(0, CTK.END)
        self.set.insert(0, new_text)

    def btn8q(self):
        current_text1 = str(self.set.get())
        if current_text1 == "Erorr":
            self.set.delete(0, CTK.END)
        letter = "8"
        current_text = self.set.get()
        new_text = current_text + letter
        self.set.delete(0, CTK.END)
        self.set.insert(0, new_text)

    def btn9q(self):
        current_text1 = str(self.set.get())
        if current_text1 == "Erorr":
            self.set.delete(0, CTK.END)
        letter = "9"
        current_text = self.set.get()
        new_text = current_text + letter
        self.set.delete(0, CTK.END)
        self.set.insert(0, new_text)

    def btn10q(self):
        current_text1 = str(self.set.get())
        if current_text1 == "Erorr":
            self.set.delete(0, CTK.END)
        letter = "."
        current_text = self.set.get()
        new_text = current_text + letter
        self.set.delete(0, CTK.END)
        self.set.insert(0, new_text)

    def btn11q(self):
        current_text1 = str(self.set.get())
        if current_text1 == "Erorr":
            self.set.delete(0, CTK.END)
        letter = "+"
        current_text = self.set.get()
        new_text = current_text + letter
        self.set.delete(0, CTK.END)
        self.set.insert(0, new_text)

    def btn12q(self):
        current_text1 = str(self.set.get())
        if current_text1 == "Erorr":
            self.set.delete(0, CTK.END)
        letter = "-"
        current_text = self.set.get()
        new_text = current_text + letter
        self.set.delete(0, CTK.END)
        self.set.insert(0, new_text)

    def btn13q(self):
        current_text1 = str(self.set.get())
        if current_text1 == "Erorr":
            self.set.delete(0, CTK.END)
        letter = "*"
        current_text = self.set.get()
        new_text = current_text + letter
        self.set.delete(0, CTK.END)
        self.set.insert(0, new_text)

    def btn14q(self):
        current_text1 = str(self.set.get())
        if current_text1 == "Erorr":
            self.set.delete(0, CTK.END)
        letter = "/"
        current_text = self.set.get()
        new_text = current_text + letter
        self.set.delete(0, CTK.END)
        self.set.insert(0, new_text)

    def schet(self):
        try:
            current = self.set.get()
            if current == "":
                pass
            else:
                current_text = float(eval(self.set.get()))
                new_text = str(round(current_text, 3))
                self.set.delete(0, CTK.END)
                self.set.insert(0, new_text)
        except ZeroDivisionError:
            new_text = "Erorr"
            self.set.delete(0, CTK.END)
            self.set.insert(0, new_text)
        except SyntaxError:
            new_text = "Erorr"
            self.set.delete(0, CTK.END)
            self.set.insert(0, new_text)
        except NameError:
            new_text = "Erorr"
            self.set.delete(0, CTK.END)
            self.set.insert(0, new_text)

    def C(self):
        self.set.delete(0, CTK.END)

    def AC(self):
        current_text = self.set.get()
        new_text = current_text[:-1]
        self.set.delete(0, CTK.END)
        self.set.insert(0, new_text)
if __name__=="__main__":
    app = App()

    def finish():
        app.destroy()  # ручное закрытие окна и всего приложения
        print("Закрытие приложения")
    app.protocol("WM_DELETE_WINDOW", finish)

    app.mainloop()
