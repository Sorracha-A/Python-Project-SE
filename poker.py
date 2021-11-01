from tkinter import *
from tkinter import messagebox

class Poker:

    def __init__(self):
        self.window=Tk()
        self.window.title("Poker game")
        self.window.geometry("1000x700")
        self.window.resizable(0, 0)

        background = PhotoImage(file='images/bg.png')
        king = PhotoImage(file='images/king.png')
        queen = PhotoImage(file='images/queen.png')

        self.window["bg"]="#90EE90"
        self.canvas = Canvas(self.window)
        self.canvas.create_image(0,0,image=background,anchor=NW)
        self.canvas.create_image(100,150,image=king,tag='king')
        self.canvas.create_image(900,150,image=queen,tag='queen')
        self.canvas.create_text(500,170,text="Poker Game",font=("Arial", 82, "bold"),fill='Yellow',tag='title')
        self.canvas.pack(fill="both",expand=True)

        self.start_button = Button(text="Start",command = self.game_start,font=("Arial", 24, "normal"),width=15,height=1,fg='green')
        self.settings_button = Button(text="Settings",command = self.game_setting,font=("Arial", 24, "normal"),width=15,height=1,fg='green')
        self.rules_button = Button(text="Rules",command = self.game_rules,font=("Arial", 24, "normal"),width=15,height=1,bg='yellow',fg='green')
        self.quit_button = Button(text="Exit",command=self.quit,font=("Arial", 24, "normal"),width=15,height=1,bg='red',fg='white')

        self.start_button.place(x=355, y=300)
        self.settings_button.place(x=355, y=375)
        self.rules_button.place(x=355, y=450)
        self.quit_button.place(x=355, y=525)
        self.window.mainloop()

    def hide_menu(self):
        self.start_button.place_forget()
        self.settings_button.place_forget()
        self.rules_button.place_forget()
        self.quit_button.place_forget()
        self.canvas.delete('title')
        self.canvas.delete('queen')
        self.canvas.delete('king')

    def game_start(self):
        self.hide_menu()

    def game_setting(self):
        self.hide_menu()

    def game_rules(self):
        self.hide_menu()

    def quit(self):
        self.window.destroy()

Poker()