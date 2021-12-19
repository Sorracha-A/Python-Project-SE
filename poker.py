# Sorracha Aiemmeesri 64011628 (Software Engineering) KMITL
# Poker Game Project (GUI)
# Using Tkinter
# Requirement: Pillow (pip install Pillow)



try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
    from abc import ABC,abstractmethod
    from tkinter import messagebox
    import PIL.Image
    import PIL.ImageTk
    import random

except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2
    from abc import ABC,abstractmethod
    import PIL.Image
    import PIL.ImageTk
    import random


""" Root application has attribute name,bg,size and abstractmethod """
class root_window(ABC):
    def __init__(self):
        self.window= tk.Tk()
        self.window.title("Poker game")
        self.background = tk.PhotoImage(file='images/bg.png')
        self.canvas = tk.Canvas(self.window)
        self.window.geometry("1000x700")
        self.window.resizable(0, 0)
        self.canvas.create_image(0,0,image=self.background,anchor=tk.NW)
        self.window["bg"] = "#90EE90"
        self.canvas.pack(fill="both",expand=True)
    @abstractmethod
    def quit(self):
        pass
    @abstractmethod
    def backtomenu(self):
        pass

""" main menu that can access to any part of the game (subclassing root window)"""
class Main_menu(root_window):

    def __init__(self):
        super().__init__()
        self.king = tk.PhotoImage(file='images/king.png')
        self.queen = tk.PhotoImage(file='images/queen.png')
        self.canvas.create_image(100,150,image=self.king,tag='king')
        self.canvas.create_image(900,150,image=self.queen,tag='queen')
        self.canvas.create_text(500,170,text="Poker Game",font=("Arial", 82, "bold"),fill='Yellow',tag='title')


        self.start_button = tk.Button(text="Start", command = self.game_start,font=("Arial", 24, "normal"),width=15,height=1,fg='green')
        self.rules_button = tk.Button(text="Rules", command = self.game_rules,font=("Arial", 24, "normal"),width=15,height=1,bg='yellow',fg='green')
        self.quit_button = tk.Button(text="Exit", command=self.quit,font=("Arial", 24, "normal"),width=15,height=1,bg='red',fg='white')

        self.start_button.place(x=355, y=375)
        self.rules_button.place(x=355, y=450)
        self.quit_button.place(x=355, y=525)
        self.window.mainloop()

    def game_start(self):
        self.window.destroy()
        gameplay()

    def game_rules(self):
        self.window.destroy()
        rules()

    def quit(self):
        self.window.destroy()

    def backtomenu(self):
        pass

""" Rules screen (subclassing root window)"""
class rules(root_window):
    def __init__(self):
        super().__init__()
        self.rules = tk.PhotoImage(file='images/rules.png')
        self.canvas.create_image(350, 350, image=self.rules, tag='rules')
        self.quit_button = tk.Button(text="Exit", command=self.quit, font=("Arial", 24, "normal"), width=15, height=1,
                                     bg='red', fg='white')
        self.backtomenu_button = tk.Button(text="Go to main menu", command=self.backtomenu, font=("Arial", 24, "normal"), width=15, height=1,
                                     bg='blue', fg='white')
        self.quit_button.place(x=660, y=380)
        self.backtomenu_button.place(x=660, y=320)
        self.window.mainloop()

    def quit(self):
        self.window.destroy()

    def backtomenu(self):
        self.window.destroy()
        Main_menu()

""" gameplay (subclassing root window) """
class gameplay(root_window):
    def __init__(self):
        super().__init__()
        self.window.geometry("1170x700")

        self.card_p1_x_origin = 50
        self.card_p1_y_origin = 50

        self.card_p2_x_origin = self.card_p1_x_origin
        self.card_p2_y_origin = self.card_p1_y_origin + 300

        """ list coordinates of the card picture (x,y)"""
        self.card_p1_x = []
        self.card_p1_y = []
        self.card_p2_x = []
        self.card_p2_y = []

        """ loop for coordinates """
        for i in range(5):
            self.card_p1_x.append(self.card_p1_x_origin + (200 * i))
            self.card_p1_y.append(self.card_p1_y_origin)
            self.card_p2_x.append(self.card_p2_x_origin + (200 * i))
            self.card_p2_y.append(self.card_p2_y_origin)

        """ loop for coordinates """
        self.p = PokerGame()  # initializing main deck
        self.p1 = Player(self.p.deck) # initializing player 1 hand (draw from main deck)
        self.p2 = Player(self.p.deck) # initializing player 2 hand (draw from main deck)

        """ Button Layout Design """


        self.btnMatchStart = tk.Button(self.window, width=10, height=3, text="Match!!", command=self.matchStart,background='crimson',foreground='White')


        self.button_card_change = tk.Button(self.window, width=20, height=3, text="Change first two card",command= self.card0Change)


        self.button_last_card_change = tk.Button(self.window, width=15, height=3, text="Change last card",command= self.card4Change)


        self.retry_button = tk.Button(text="Retry", command=self.retry, font=("Arial", 16, "normal"),state='disabled', width=5, height=1,bg='yellow',fg='black')

        self.quit_button = tk.Button(text="Exit", command=self.quit, font=("Arial", 16, "normal"), width=5, height=1,
                                     bg='red', fg='white')
        self.backtomenu_button = tk.Button(text="Go to main menu", command=self.backtomenu, font=("Arial", 16, "normal"), width=15, height=1,
                                     bg='blue', fg='white')

        """ Some useful label """

        self.labelPlayer1Score = tk.Label(self.window, width=10, height=3, text="Score", relief='solid')
        self.labelPlayer1Score.place(x=1050, y=140)

        self.labelPlayer2Score = tk.Label(self.window, width=10, height=3, text="Score", relief='solid')
        self.labelPlayer2Score.place(x=1050, y=430)

        self.winner_laberl = tk.Label(self.window, width=50, height=3, text="Match Result", relief='solid')
        self.winner_laberl.place(x=230, y=640)


        """ Button placing """

        self.btnMatchStart.place(x=1050, y=270)
        self.button_card_change.place(x = 30, y = 640)
        self.button_last_card_change.place(x = 1000, y = 640)

        self.retry_button.place(x=630,y=650)
        self.quit_button.place(x=920, y=650)
        self.backtomenu_button.place(x=720, y=650)

        """ initializing list of the image,image lebel of the card of players """
        self.card_p1_photoImage = []
        self.card_p2_photoImage = []


        self.card_p1_photoImage_label = []
        self.card_p2_photoImage_label = []

        """ placing cards on the table """
        for i in range(5):
            self.card_p1_photoImage.append(PIL.ImageTk.PhotoImage(self.p1.hand[i].img_B)) # append the image of the back of the i card into the photoImage list
            self.card_p1_photoImage_label.append( tk.Label(self.window, image=self.card_p1_photoImage[i])) # append the image label of the i card to the photoImage label list
            self.card_p1_photoImage_label[i].place(x=self.card_p1_x[i], y=self.card_p1_y[i]) # placing the lebel i from photoImage label list at the position i of list card_p1_x and card_p1_y
            self.card_p2_photoImage.append(PIL.ImageTk.PhotoImage(self.p2.hand[i].img_F))# append the image of the front of the i card into the photoImage list
            self.card_p2_photoImage_label.append(tk.Label(self.window, image=self.card_p2_photoImage[i]))
            self.card_p2_photoImage_label[i].place(x=self.card_p2_x[i], y=self.card_p2_y[i])

        self.window.mainloop()

    def quit(self):
        self.window.destroy()

    """ back to menu """
    def backtomenu(self):
        self.window.destroy()
        Main_menu()

    """ revealing opponent card """
    def matchStart(self):
        for i in range(5):
            self.card_p1_photoImage[i] = PIL.ImageTk.PhotoImage(self.p1.hand[i].img_F) # replacing the image list that used to be the back of the card to be front
            self.card_p1_photoImage_label[i].config(image=self.card_p1_photoImage[i])  # changing the image from label list using the front image from previous line
            self.window.update() #update window (it will replace what we have placed with the current list)
        self.labelPlayer1Score.config(text=ranktoString(self.p1.hand))
        self.labelPlayer2Score.config(text=ranktoString(self.p2.hand))

        """ define who is winning """
        if (isRank(self.p1.hand) == isRank(self.p2.hand)):
            self.winner_laberl.config(text="DRAW")


        elif (isRank(self.p1.hand) < isRank(self.p2.hand)):
            self.winner_laberl.config(text="WIN")


        elif (isRank(self.p1.hand) > isRank(self.p2.hand)):
            self.winner_laberl.config(text="LOSE")

        """ disable some buttons """
        self.button_card_change.config(state='disabled')
        self.button_last_card_change.config(state='disabled')
        self.retry_button.config(state='normal')

    """ retry game """
    def retry(self):
        self.window.destroy()
        gameplay()

    """ change first two card """
    def card0Change(self):

        self.button_card_change.config(text="Changed")
        self.p2.changeSelectedCard(0, self.p.deck) #replace card no 0 in hand with the card popped from the deck list
        self.card_p2_photoImage[0] = PIL.ImageTk.PhotoImage(self.p2.hand[0].img_F)
        self.card_p2_photoImage_label[0].config(image=self.card_p2_photoImage[0])
        ##
        self.p2.changeSelectedCard(1, self.p.deck)
        self.card_p2_photoImage[1] = PIL.ImageTk.PhotoImage(self.p2.hand[1].img_F)
        self.card_p2_photoImage_label[1].config(image=self.card_p2_photoImage[1])

        self.window.update()

    """ change the last card """
    def card4Change(self):
        self.button_last_card_change.config(text="Changed")
        self.p2.changeSelectedCard(4, self.p.deck) #replace card no 4 in hand with the card popped from the deck list
        self.card_p2_photoImage[4] = PIL.ImageTk.PhotoImage(self.p2.hand[4].img_F)
        self.card_p2_photoImage_label[4].config(image=self.card_p2_photoImage[4])
        self.window.update()

""" Initialize Poker Cards """
class PokerGame:

    """ creating a deck """
    def __init__(self):
        self.deck = []

        self.deck.append(Card("Spade", 1, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/S01.png')))
        self.deck.append(Card("Spade", 2, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/S02.png')))
        self.deck.append(Card("Spade", 3, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/S03.png')))
        self.deck.append(Card("Spade", 4, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/S04.png')))
        self.deck.append(Card("Spade", 5, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/S05.png')))
        self.deck.append(Card("Spade", 6, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/S06.png')))
        self.deck.append(Card("Spade", 7, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/S07.png')))
        self.deck.append(Card("Spade", 8, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/S08.png')))
        self.deck.append(Card("Spade", 9, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/S09.png')))
        self.deck.append(Card("Spade", 10, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/S10.png')))
        self.deck.append(Card("Spade", 11, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/S11.png')))
        self.deck.append(Card("Spade", 12, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/S12.png')))
        self.deck.append(Card("Spade", 13, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/S13.png')))

        self.deck.append(Card("Heart", 1, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/H01.png')))
        self.deck.append(Card("Heart", 2, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/H02.png')))
        self.deck.append(Card("Heart", 3, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/H03.png')))
        self.deck.append(Card("Heart", 4, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/H04.png')))
        self.deck.append(Card("Heart", 5, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/H05.png')))
        self.deck.append(Card("Heart", 6, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/H06.png')))
        self.deck.append(Card("Heart", 7, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/H07.png')))
        self.deck.append(Card("Heart", 8, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/H08.png')))
        self.deck.append(Card("Heart", 9, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/H09.png')))
        self.deck.append(Card("Heart", 10, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/H10.png')))
        self.deck.append(Card("Heart", 11, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/H11.png')))
        self.deck.append(Card("Heart", 12, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/H12.png')))
        self.deck.append(Card("Heart", 13, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/H13.png')))

        self.deck.append(Card("Club", 1, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/C01.png')))
        self.deck.append(Card("Club", 2, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/C02.png')))
        self.deck.append(Card("Club", 3, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/C03.png')))
        self.deck.append(Card("Club", 4, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/C04.png')))
        self.deck.append(Card("Club", 5, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/C05.png')))
        self.deck.append(Card("Club", 6, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/C06.png')))
        self.deck.append(Card("Club", 7, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/C07.png')))
        self.deck.append(Card("Club", 8, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/C08.png')))
        self.deck.append(Card("Club", 9, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/C09.png')))
        self.deck.append(Card("Club", 10, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/C10.png')))
        self.deck.append(Card("Club", 11, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/C11.png')))
        self.deck.append(Card("Club", 12, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/C12.png')))
        self.deck.append(Card("Club", 13, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/C13.png')))

        self.deck.append(Card("Diamond", 1, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/D01.png')))
        self.deck.append(Card("Diamond", 2, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/D02.png')))
        self.deck.append(Card("Diamond", 3, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/D03.png')))
        self.deck.append(Card("Diamond", 4, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/D04.png')))
        self.deck.append(Card("Diamond", 5, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/D05.png')))
        self.deck.append(Card("Diamond", 6, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/D06.png')))
        self.deck.append(Card("Diamond", 7, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/D07.png')))
        self.deck.append(Card("Diamond", 8, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/D08.png')))
        self.deck.append(Card("Diamond", 9, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/D09.png')))
        self.deck.append(Card("Diamond", 10, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/D10.png')))
        self.deck.append(Card("Diamond", 11, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/D11.png')))
        self.deck.append(Card("Diamond", 12, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/D12.png')))
        self.deck.append(Card("Diamond", 13, PIL.Image.open('card_images/0.png'), PIL.Image.open('card_images/D13.png')))

        random.shuffle(self.deck)

""" Define Card """
class Card:

    def __init__(self, suit, num, img_B, img_F):
        self.suit = suit
        self.num = num
        self.img_B = img_B
        self.img_F = img_F

""" Initialize Player's Card (Hand) """
""" use to draw the card from the deck , pass by refference"""
class Player():

    def __init__(self, deck):

        self.hand = []

        for i in range(5):
            self.hand.append(deck.pop())

    def changeSelectedCard(self, card_position_number, deck):
        try:
            self.hand[card_position_number] = deck.pop()
        except:
            messagebox.showwarning("NO CARD LEFT", "There's no card in the deck left! please press 'Match'")




""" Define Hand Rank Value """


def isRank(hand):
    if (isStraightFlush(hand) != False):
        return 800 + isStraightFlush(hand)

    elif (is4ofCard(hand) != False):
        return 700 + is4ofCard(hand)

    elif (isFullHouse(hand) != False):
        return 600 + isFullHouse(hand)

    elif (isFlush(hand) != False):
        return 500 + isFlush(hand)

    elif (isStraight(hand) != False):
        return 400 + isStraight(hand)

    elif (is3ofCard(hand) != False):
        return 300 + is3ofCard(hand)

    elif (is2Pair(hand) != False):
        return 200 + is2Pair(hand)

    elif (is1Pair(hand) != False):
        return 100 + is1Pair(hand)

    else:
        return isTop(hand)

""" convert from rank value to string """
def ranktoString(hand):
    rank = isRank(hand)

    if (rank >= 800):
        return "Straight Flush"

    elif (rank >= 700):
        return "4 of Card"

    elif (rank >= 600):
        return "Full House"

    elif (rank >= 500):
        return "Flush"

    elif (rank >= 400):
        return "Straight"

    elif (rank >= 300):
        return "3 of Card"

    elif (rank >= 200):
        return "Two Pairs"

    elif (rank >= 100):
        return "One Pair"

    else:
        return "Top"

""" Define Hand Rank """


def isStraightFlush(hand):
    if (isFlush(hand) != False and isStraight(hand) != False):
        return isStraight(hand)  # return the pts equal to ้highest card in str8

    else:
        return False

""" check if the hand is fourcard """
def is4ofCard(hand):
    cardnumlist = []

    for card in hand:
        cardnumlist.append(card.num)

    for i in range(1, 14):
        if (cardnumlist.count(i) == 4):
            if (i == 1):    #if it's 4 aces get 14 pts
                return 14
            else:
                return i    #else return value equal to the card num

    return False

""" check if the hand is full house """
def isFullHouse(hand):
    if (is3ofCard(hand) != False and is2Pair(hand) != False):
        return is3ofCard(hand)  # return the pts equal to the card that has 3 of a kind

    else:
        return False

""" check if the hand is flush """
def isFlush(hand):
    if (hand[0].suit == hand[1].suit == hand[2].suit == hand[3].suit == hand[4].suit):
        return isTop(hand) # return value to the highest number of card

    else:
        return False

""" check if the hand is straight """
def isStraight(hand):
    cardnumlist = []

    for card in hand:
        cardnumlist.append(card.num)

    cardnumlist.sort()

    if (cardnumlist[0] + 1 == cardnumlist[1] and
        cardnumlist[1] + 1 == cardnumlist[2] and
        cardnumlist[2] + 1 == cardnumlist[3] and
        cardnumlist[3] + 1 == cardnumlist[4]):
        return cardnumlist[4]  # get the pts equal to the biggest card in the hand

    elif (cardnumlist[0] == 1 and
          cardnumlist[1] == 10 and
          cardnumlist[2] == 11 and
          cardnumlist[3] == 12 and
          cardnumlist[4] == 13): # if it is royal straight 10 J Q K A (14 pts)
        return 14

    else:
        return False

""" check if the hand is 3 of a kind """
def is3ofCard(hand):
    cardnumlist = []

    for card in hand:
        cardnumlist.append(card.num)

    cardnumlist.sort()

    for i in range(1, 14):  # check whether there's atleast three card with the same number.
        if (cardnumlist.count(i) >= 3):
            if (i == 1):
                return 14 # if it's the ACE get 14 pts
            else:
                return i # return the pts equal to the card that has 3 of a kind

    return False

""" check if the hand is 2 pairs """
def is2Pair(hand):
    cardnumlist = []
    pairs_num = 0

    for card in hand:
        cardnumlist.append(card.num)

    cardnumlist.sort()

    for i in range(1, 14):  # check whether there's more atleast two card with the same number.
        if (cardnumlist.count(i) >= 2):
            pairs_num = pairs_num + 1   # yes ==> number of paird +1

        if (pairs_num == 2):
            if (is1Pair(hand) == 14): # if one of the pair is ACES
                return 14
            else:
                return i    # return the score equal to the highest pair card number

    return False

""" check if the hand is 1 pair """
def is1Pair(hand):
    cardnumlist = []

    for card in hand:
        cardnumlist.append(card.num)

    cardnumlist.sort()

    for i in range(1, 14):
        if (cardnumlist.count(i) >= 2):
            if (i == 1):
                return 14
            else:
                return i

    return False

""" check if the hand is high card """
def isTop(hand):
    cardnumlist = []

    for card in hand:
        cardnumlist.append(card.num)

    cardnumlist.sort()

    if (cardnumlist[0] == 1):
        return 14 #if there is an ace
    else:
        return cardnumlist[4] # return value to the highest number of card




Main_menu()