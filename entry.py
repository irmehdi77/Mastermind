from random import randint
from tkinter import Tk, Label, END, Listbox, Menu
from tkinter.ttk import Button, Entry


player_color = {}
computer_color = {}
s = {}  # s = state
T = 'true'
F = 'false'
boolian = True
m_try = 5
base_try = m_try


def finish_program(event=None):
    '''This function closes the program'''
    exit()


class entf:
    '''This class is responsible for focusing on inputs'''

    def ent2f(event=None):
        ent2.focus()
        ent2.select_range(0, END)

    def ent3f(event=None):
        ent3.focus()
        ent3.select_range(0, END)

    def ent4f(event=None):
        ent4.focus()
        ent4.select_range(0, END)

    def ent1f(event=None):
        ent1.focus()
        ent1.select_range(0, END)


def max_try(event=None):
    '''This function counts your attempts and if it reaches the maximum, you lose'''
    global m_try
    m_try -= 1
    if m_try == 2:
        lbl_try.config(fg='red')
    lbl_try.config(text=f'Remaining attempts : {m_try}')

    if m_try == 0:
        lst_box.insert(END, 'Your attempt has exceeded the limit.')
        lst_box.insert(END, "I'm sorry but you lost")
        lst_box.insert(END, '\n')
        btn.config(text='Refresh', command=refresh_trys)
    else:
        player_input()


def refresh_trys():
    '''This function refreshes the game after winning or losing'''
    global boolian, m_try
    m_try = 5
    lbl_try.config(text=f'Remaining attempts : {m_try}', fg='green')
    btn.config(text='Check', command=max_try)
    boolian = True
    ent1.delete(0, END)
    ent2.delete(0, END)
    ent3.delete(0, END)
    ent4.delete(0, END)


def player_input(event=None):
    '''This function takes user inputs and then stores them'''
    entf.ent1f()
    in1 = ent1.get()
    in2 = ent2.get()
    in3 = ent3.get()
    in4 = ent4.get()
    player_color.update({1: in1, 2: in2, 3: in3, 4: in4})
    if boolian:
        computer_select()
    game()


def computer_select():
    '''In this function, the computer selects the colors'''
    for i in range(1, 5):
        random_color = randint(0, 6)
        if random_color == 0:
            computer_color.update({i: 'nothing'})
        elif random_color == 1:
            computer_color.update({i: 'red'})
        elif random_color == 2:
            computer_color.update({i: 'green'})
        elif random_color == 3:
            computer_color.update({i: 'blue'})
        elif random_color == 4:
            computer_color.update({i: 'yellow'})
        elif random_color == 5:
            computer_color.update({i: 'white'})
        elif random_color == 6:
            computer_color.update({i: 'black'})
        global boolian
        boolian = False
    print(computer_color)

def game():
    '''In this function, the input of the user and the computer are compared and the result is told to the user'''
    for C in range(1, 5):
        if player_color.get(C) == computer_color.get(C):
            lst_box.insert(END, f'The color of position {C} is correct')
            s.update({C: 'true'})
        else:
            lst_box.insert(END, f'The color of position {C} is wrong')
            s.update({C: 'false'})
    lst_box.insert(END, '\n')
    lst_box.insert(END, f'Colors chosen by you : {ent1.get()}, {ent2.get()}, {ent3.get()}, {ent4.get()}')
    lst_box.insert(END, '\n')
    win_or_lose()


def win_or_lose():
    '''In this function, it is determined whether the user is a winner or a loser'''
    if s.get(1) == T and s.get(2) == T and s.get(3) == T and s.get(4) == T:
        global boolian
        boolian = True
        cc = computer_color
        lst_box.insert(END, 'You are Winner!')
        lst_box.insert(END, f'You succeeded in {base_try-m_try} attempts')
        lst_box.insert(END, f'Colors : {cc.get(1)}, {cc.get(2)}, {cc.get(3)}, {cc.get(4)}')
        lst_box.insert(END, '\n')
        ent1.delete(0, END)
        ent2.delete(0, END)
        ent3.delete(0, END)
        ent4.delete(0, END)
        ent1.focus()


def view_mode():
    windowe.destroy()
    from mastermind import window
    window()


def d_windowe():
    global ent1, ent2, ent3, ent4
    global lst_box, btn, windowe, lbl_try

    windowe = Tk()

    windowe.title('mastermind (Entry view)')
    windowe.geometry('425x391+450+200')
    windowe.resizable(0, 0)

    lbl1 = Label(windowe, text='The color of the first position : ')
    lbl1.place(x=10, y=10)

    lbl2 = Label(windowe, text='The color of the Second position : ')
    lbl2.place(x=10, y=50)

    lbl3 = Label(windowe, text='The color of the third position : ')
    lbl3.place(x=10, y=90)

    lbl4 = Label(windowe, text='The color of the fourth position : ')
    lbl4.place(x=10, y=130)

    ent1 = Entry(windowe, width=30)
    ent1.place(x=210, y=13)
    ent1.focus()

    ent2 = Entry(windowe, width=30)
    ent2.place(x=210, y=53)

    ent3 = Entry(windowe, width=30)
    ent3.place(x=210, y=93)

    ent4 = Entry(windowe, width=30)
    ent4.place(x=210, y=133)

    ent1.bind('<Return>', entf.ent2f)
    ent1.bind('<Up>', entf.ent4f)
    ent1.bind('<Down>', entf.ent2f)

    ent2.bind('<Return>', entf.ent3f)
    ent2.bind('<Up>', entf.ent1f)
    ent2.bind('<Down>', entf.ent3f)

    ent3.bind('<Return>', entf.ent4f)
    ent3.bind('<Up>', entf.ent2f)
    ent3.bind('<Down>', entf.ent4f)

    ent4.bind('<Return>', max_try)
    ent4.bind('<Up>', entf.ent3f)
    ent4.bind('<Down>', entf.ent1f)

    windowe.bind('<Escape>', finish_program)

    btn = Button(windowe, text='Check', width=15, command=max_try)
    btn.place(x=250, y=170)

    lst_box = Listbox(windowe, width=70, height=11)
    lst_box.place(x=0, y=210)

    lbl_try = Label(windowe,text=f'Remaining attempts : {m_try}', fg='green')
    lbl_try.place(x=25, y=170)

    menubar = Menu(windowe)
    menubar.add_command(label='Change view mode', command=view_mode)
    windowe.config(menu=menubar)

    windowe.mainloop()
