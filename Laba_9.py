from tkinter import *
import tkinter.messagebox as mb
import sqlite3


class Registr:

    def CreateNewUser(self, username, password, password_again):
        if username == '' or password == '' or password_again == '':
            msg = 'Заполните все поля'
            mb.showerror("Ошибка", msg)
        else:
            try:
                f = open('Users.txt', 'r+')
                text = f.read().split()
                for i in text:
                    if username == i.split(':')[0]:
                        msg = 'Имя пользователя уже существует'
                        mb.showerror("Ошибка", msg)
                        return
                else:
                    if password != password_again:
                        msg = 'Пароли не совпадают'
                        mb.showerror("Ошибка", msg)
                        return
                    else:
                        f.write(username + ':' + password + '\n')
                        self.window_Reg.destroy()
                        root = Tk()
                        game = GameField(root, matrix)
                        game.create_game_field()

                        root.mainloop()
                    return
            except:
                f = open('Users.txt', 'w')
                if password != password_again:
                    msg = 'Пароли не совпадают'
                    mb.showerror("Ошибка", msg)
                    return
                else:
                    f.write(username + ':' + password + '\n')
                    self.window_Reg.destroy()
                    root = Tk()
                    game = GameField(root, matrix)
                    game.create_game_field()

                    root.mainloop()
                return


    def __init__(self):
        try:
            window_Entry.destroy()
        except:
            pass
        self.window_Reg = Tk()
        self.window_Reg.title('Регистрация')
        self.window_Reg.geometry('300x300')
        self.window_Reg.eval('tk::PlaceWindow . center')
        username_label = Label(self.window_Reg, text='Имя пользователя', )
        username_entry = Entry(self.window_Reg)
        password_label = Label(self.window_Reg, text='Пароль')
        password_entry = Entry(self.window_Reg)
        password_label_confirm = Label(self.window_Reg, text='Повторите пароль')
        password_entry_confirm = Entry(self.window_Reg)
        send_btn = Button(self.window_Reg, text='Зарегистрироваться', command=lambda:
        self.CreateNewUser(username_entry.get(), password_entry.get(), password_entry_confirm.get(), ))
        username_label.pack(padx=10, pady=8)
        username_entry.pack(padx=10, pady=8)
        password_label.pack(padx=10, pady=8)
        password_entry.pack(padx=10, pady=8)
        password_label_confirm.pack(padx=10, pady=8)
        password_entry_confirm.pack(padx=10, pady=8)
        send_btn.pack(padx=10, pady=8)

        self.window_Reg.mainloop()


class Login_in:

    def CheckExist(self, username, password):
        if username == '' or password == '':
            msg = 'Заполните все поля'
            mb.showerror("Ошибка", msg)
        else:
            try:
                f = open('Users.txt', 'r')
                text = f.read().split()
                for i in text:
                    if i.split(':')[0] == username:
                        if password == i.split(':')[1]:
                            self.window_Login.destroy()
                            root = Tk()
                            game = GameField(root, matrix)
                            game.create_game_field()
                            root.mainloop()
                            return
                        else:
                            msg = 'Пароль не совпадает'
                            mb.showerror("Ошибка", msg)
                            return
                    msg = 'Такой пользователь не зарегестрирован'
                    mb.showerror("Ошибка", msg)
                    return
            except:
                msg = 'Еще ни один пользователь не зарегестрирован'
                mb.showerror("Ошибка", msg)
                self.window_Login.destroy()
                Registr()


    def __init__(self):
        window_Entry.destroy()
        self.window_Login = Tk()
        self.window_Login.title('Вход')
        self.window_Login.geometry('300x250')
        self.window_Login.eval('tk::PlaceWindow . center')
        username_label = Label(self.window_Login, text='Имя пользователя', )
        username_entry = Entry(self.window_Login)
        password_label = Label(self.window_Login, text='Пароль')
        password_entry = Entry(self.window_Login)
        send_btn = Button(self.window_Login, text='Войти', command=lambda:
        self.CheckExist(username_entry.get(), password_entry.get()))

        username_label.pack(padx=10, pady=8)
        username_entry.pack(padx=10, pady=8)
        password_label.pack(padx=10, pady=8)
        password_entry.pack(padx=10, pady=8)
        send_btn.pack(padx=10, pady=8)

        self.window_Login.mainloop()


class GameField:
    def __init__(self, root, matrix):
        self.root = root
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.buttons = []

    def create_game_field(self):
        for r in range(self.rows):
            row_buttons = []
            for c in range(self.cols):
                button = Button(self.root, width=10, height=5, relief=RAISED)
                button.grid(row=r, column=c)
                button.config(command=lambda row=r, col=c: self.button_click(row, col))
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def button_click(self, row, col):
        pass


matrix = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

window_Entry = Tk()
window_Entry.title('Lab 9')
window_Entry.geometry('250x250')
window_Entry.eval('tk::PlaceWindow . center')
loginin = Button(window_Entry, text='Вход', command=Login_in)
reg = Button(window_Entry, text='Регистрация', command=Registr)
loginin.pack(padx=10, pady=8)
reg.pack(padx=10, pady=8)

window_Entry.mainloop()
