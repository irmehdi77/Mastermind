from tkinter import Tk, Radiobutton, Label, LabelFrame, Menu, messagebox
from tkinter import BOTH, StringVar
from tkinter.ttk import Button


hp1 = 'A color is chosen for each situation\n'
hp2 = 'Then you choose a color(among the colors)for each situation.\n'
hp3 = 'Finally, it is clear whether your guess is correct or not and\n'
hp4 = ' the game continues.\n'
hp_good_luck = 'Good luck!\n\n'
hp_colors = 'colors: {red, green, blue, yellow, white, black, nothing}'
how_play = hp1 + hp2 + hp3 + hp4 + hp_good_luck + hp_colors


def select_view_mode():
    '''This will call your requested shell function'''
    value_of_rbtns = rbtn_variable.get()

    if value_of_rbtns == 'RB':
        window.destroy()
        from radiobutton import d_windowr
        d_windowr()

    elif value_of_rbtns == 'E':
        window.destroy()
        from entry import d_windowe
        d_windowe()


def show_info():
    messagebox.showinfo('Information', 'Made by Mehdi Taheri.')


def how_to_play():
    messagebox.showinfo('How to play?', how_play)


def window():
    global rbtn_variable, window

    window = Tk()

    window.title('Mastermind Game')
    window.geometry('300x290+520+150')
    window.resizable(0, 0)
    window.config(bg='ivory4')

    RadioButtons = [('RadioButtons', 'RB', 40),
                    ('Entry', 'E', 180)]
    rbtn_variable = StringVar()
    rbtn_variable.set('RB')

    lbl = Label(window,
                text='Welcome to Mastermind',
                font=('tahoma', 19),
                fg='maroon2',
                bg='gold',
                height=2)
    lbl.pack(fill=BOTH)

    lframe = LabelFrame(window, bg='ivory4')
    lframe.pack(fill=BOTH, expand=True)

    Label(lframe,
          text='Choose a mode to play : ',
          font=('tahoma', 11, 'italic'),
          bg='ivory4',
          fg='blue4').place(x=5, y=30)

    for text, Type, x in RadioButtons:
        rbtn = Radiobutton(lframe,
                    text=text,
                    font=('tahoma 10 italic'),
                    fg='blue4',
                    bg='ivory4',
                    value=Type,
                    variable=rbtn_variable)
        rbtn.place(x=x, y=90)

    Button(lframe,
               text='Chose',
               command=select_view_mode).place(x=110, y=160)

    menubar = Menu(window)

    menubar.add_command(label='How to play', command=how_to_play)
    menubar.add_command(label='Info', command=show_info)

    window.config(menu=menubar)

    window.mainloop()


window()
