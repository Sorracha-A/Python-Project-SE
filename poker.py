from tkinter import *
from tkinter import messagebox

class Poker:

    def __init__(self):
        self.window=Tk()
        self.window.title("Poker game")
        self.window.geometry("1000x700")
        self.window["bg"]="#90EE90"
        self.window.resizable(0,0)

        game_title =Label(text="Poker Game",font=("Arial", 82, "bold"),bg='#90EE90',fg='Blue')
        game_title.place(x=220, y=70)

        self.start_button = Button(text="Start",command = self.game_start,font=("Arial", 24, "normal"),width=15,height=1,fg='green')
        self.settings_button = Button(text="Settings",command = self.game_setting,font=("Arial", 24, "normal"),width=15,height=1,fg='green')
        self.rules_button = Button(text="Rules",command = self.game_rules,font=("Arial", 24, "normal"),width=15,height=1,bg='yellow',fg='green')
        self.quit_button = Button(text="Exit",command=self.quit,font=("Arial", 24, "normal"),width=15,height=1,bg='red',fg='white')

        self.start_button.place(x=375, y=300)
        self.settings_button.place(x=375, y=375)
        self.rules_button.place(x=375, y=450)
        self.quit_button.place(x=375, y=525)
        self.window.mainloop()

    def hide_menu(self):
        self.start_button.place_forget()
        self.settings_button.place_forget()
        self.rules_button.place_forget()
        self.quit_button.place_forget()

    def game_start(self):
        self.hide_menu()

    def game_setting(self):
        self.hide_menu()

    def game_rules(self):
        self.hide_menu()

    def quit(self):
        self.window.destroy()

Poker()

    ##ทำพื้นหลัง และก็ เปลี่ยน title เกมให้เป็นรูปสวยๆ แล้วค่อยเริ่มทำระบบเกม