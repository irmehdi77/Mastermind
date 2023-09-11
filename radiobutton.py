from random import randint
from tkinter import Tk, Label, Radiobutton, Listbox, LabelFrame, Menu
from tkinter import StringVar, END
from tkinter.ttk import Button


player_color = {}
computer_color = {}
s = {}  # s = state
T = 'true'
F = 'false'
boolian = True
m_try = 5
base_try = m_try
chang_or_not_text_btn = False


def finish_program(event=None):
    '''This function closes the program'''
    exit()


def max_try(event=None):
    '''This function counts your attempts and if it reaches the maximum, you lose'''
    global chang_or_not_text_btn, m_try
    m_try -= 1
    if m_try == 2:
        lbl.config(fg='red4')
    lbl.config(text=f'Remaining attempts : {m_try}')

    if m_try == 0:
        lst_box.insert(END, 'Your attempt has exceeded the limit.')
        lst_box.insert(END, "I'm sorry but you lost.")
        lst_box.insert(END, '\n')
        btn.config(text='Retry', command=refresh_trys)
    else:
        if chang_or_not_text_btn:
            btn.config(text='Check', command=max_try)
        player_input()


def refresh_trys():
    '''This function refreshes the game after winning or losing'''
    global boolian, chang_or_not_text_btn, m_try
    m_try = 5
    lbl.config(text=f'Remaining attempts : {m_try}', fg='limegreen')
    chang_or_not_text_btn = True
    boolian = True
    rbtnsF_variable.set('red')
    rbtnsS_variable.set('red')
    rbtnsT_variable.set('red')
    rbtnsFourth_variable.set('red')
    btn.config(command=max_try, text='Check')


def player_input():
    '''This function takes user inputs and then stores them'''
    in1 = rbtnsF_variable.get()
    in2 = rbtnsS_variable.get()
    in3 = rbtnsT_variable.get()
    in4 = rbtnsFourth_variable.get()
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


def game():
    '''In this function, the input of the user and the computer are compared and the result is told to the user'''
    for C in range(1, 5):
        if player_color.get(C) == computer_color.get(C):
            lst_box.insert(END, f'The color of position {C} is correct.')
            s.update({C: 'true'})
        else:
            lst_box.insert(END, f'The color of position {C} is wrong.')
            s.update({C: 'false'})
    lst_box.insert(END, '\n')
    lst_box.insert(END, '\n')
    win_or_lose()


def win_or_lose():
    '''In this function, it is determined whether the user is a winner or a loser'''
    if s.get(1) == T and s.get(2) == T and s.get(3) == T and s.get(4) == T:
        global boolian
        boolian = True
        lst_box.insert(END, 'You are Winner!')
        lst_box.insert(END, f'You succeeded in {base_try-m_try} attempts.')
        lst_box.insert(END, '\n')
        btn.config(command=refresh_trys, text='Refresh')


def view_mode():
    windowr.destroy()
    from mastermind import window
    window()


def d_windowr():
    global lst_box, btn, windowr, lbl
    global rbtnsF_variable, rbtnsS_variable
    global rbtnsT_variable, rbtnsFourth_variable

    windowr = Tk()

    windowr.title('mastermind (RadioButton view)')
    windowr.geometry('733x325+350+220')
    windowr.resizable(0, 0)
    windowr.config(bg='skyblue4')
    sb4 = 'skyblue4'
    selectC = 'white smoke'

    rbtns = [('red', 'red', 55, 'brown4', sb4, selectC),
             ('green', 'green', 105, 'green2', sb4, selectC),
             ('blue', 'blue', 170, 'blue2', sb4, selectC),
             ('yellow', 'yellow', 220, 'goldenrod1', sb4, selectC),
             ('white', 'white', 285, 'ghost white', sb4, 'black'),
             ('black', 'black', 345, 'gray1', sb4, selectC),
             ('nothing', 'nothing', 405, 'gray60', sb4, selectC)]
    rbtnsF_variable = StringVar()
    rbtnsF_variable.set('red')

    rbtnsS_variable = StringVar()
    rbtnsS_variable.set('red')

    rbtnsT_variable = StringVar()
    rbtnsT_variable.set('red')

    rbtnsFourth_variable = StringVar()
    rbtnsFourth_variable.set('red')

    Label(windowr,
          text='Choose colors : ',
          font='tahoma 11 italic bold', bg=sb4).place(x=10, y=10)

    Label(windowr,
          text='First place : ',
          font='tahoma 11 italic', bg=sb4).place(x=10, y=50)

    for text, Type, x, fg, bg, sc in rbtns:
        rbtnsF = Radiobutton(windowr,
                            text=text,
                            value=Type,
                            variable=rbtnsF_variable,
                            font='tahoma 9 italic',
                            fg=fg,
                            bg=bg,
                            selectcolor=sc)
        rbtnsF.place(x=x, y=80)

    Label(windowr,
          text='Second place : ',
          font='tahoma 11 italic', bg=sb4).place(x=10, y=120)

    for text, Type, x, fg, bg, sc in rbtns:
        rbtnsS = Radiobutton(windowr,
                            text=text,
                            value=Type,
                            variable=rbtnsS_variable,
                            font='tahoma 9 italic',
                            fg=fg,
                            bg=bg,
                            selectcolor=sc)
        rbtnsS.place(x=x, y=150)

    Label(windowr,
          text='Third place : ',
          font='tahoma 11 italic', bg=sb4).place(x=10, y=190)

    for text, Type, x, fg, bg, sc in rbtns:
        rbtnsT = Radiobutton(windowr,
                            text=text,
                            value=Type,
                            variable=rbtnsT_variable,
                            font='tahoma 9 italic',
                            fg=fg,
                            bg=bg,
                            selectcolor=sc)
        rbtnsT.place(x=x, y=220)

    Label(windowr,
          text='Fourth place : ',
          font='tahoma 11 italic', bg=sb4).place(x=10, y=260)

    for text, Type, x, fg, bg, sc in rbtns:
        rbtnsFourth = Radiobutton(windowr,
                            text=text,
                            value=Type,
                            variable=rbtnsFourth_variable,
                            font='tahoma 9 italic',
                            fg=fg,
                            bg=bg,
                            selectcolor=sc)
        rbtnsFourth.place(x=x, y=290)

    frame = LabelFrame(windowr, width=232, height=323, bg=sb4)
    frame.place(x=499, y=1)

    lst_box = Listbox(frame, height=13, width=37)
    lst_box.place(x=1, y=2)

    btn = Button(frame,
                 text='Check',
                 width=10,
                 command=max_try)
    btn.place(x=80, y=250)

    lbl = Label(
        frame,
        text=f'Remaining attempts : {m_try}',
        bg=sb4,
        fg='limegreen'
        )
    lbl.place(x=50, y=285)

    menubar = Menu(windowr)
    menubar.add_command(label='Change view mode', command=view_mode)
    windowr.config(menu=menubar)

    windowr.bind('<Escape>', finish_program)
    windowr.bind('<Return>', max_try)

    windowr.mainloop()
