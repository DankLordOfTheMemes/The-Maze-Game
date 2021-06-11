from graphics import *
from button import *

'''
    Menu Class
'''
class Menu:
    def __init__(self, window):
        '''
            Constructor of the Menu Class of the Maze Game. It only needs the window where all this will be drawn as parameter.
        '''
        self.win = window #Attribute that represents the screen that the menus will be drawn

    '''
        Set the intro of the game (The instructions), draw it and then undraw it when time comes.
    '''
    def generate_Instructions(self):
        '''
            Function to draw the instruction screen (or START in games).
        
        '''
        self.win.setBackground("black")
        intro_Tittle = Text(Point(self.win.getWidth()/2,self.win.getHeight()*0.75), "A MAZE GAME")
        intro_Tittle.setTextColor("white")
        intro_Tittle.setStyle("bold")
        intro_Tittle.setSize(24)
        intro_Text = Text(Point(self.win.getWidth()/2, self.win.getHeight()/2), "Thank you for running this program! The process is the following:\n"+
        "1. You will be able to put your first point before the red vertical line.\n"+
        "2. Now, you must create a path to the other edges of the screen.\n"+
        "3. You will gain points for playing.")
        intro_Text.setTextColor("white")
        intro_Text.setSize(14)
        intro_Tittle.draw(self.win)
        intro_Text.draw(self.win)
        promt = Button(self.win,Point(self.win.getWidth()/2,self.win.getHeight()/4),30,20,"Ok!") #Buuton from button.py (OK)
        promt.activate() #Activate button 1
        while True: #Checks wether the button is clicked
            p1 = self.win.getMouse()
            if(promt.clicked(p1) == True):
                break
        intro_Tittle.undraw()
        intro_Text.undraw()
        promt.undraw() #Undraws the button see button.py (END)
    
    '''
        Set a menu to pick game difficulty; pick such difficulty, show what was picked and, then, undraw all
    '''
    def difficulty_Menu(self):
        '''
            Function to draw the menu to choose difficulty.

            Returns values related to level and life count   
        '''
        self.win.setBackground("black")
        menu_Tittle = Text(Point(self.win.getWidth()/2,self.win.getHeight()*0.75), "Difficulty Menu")
        menu_Tittle.setTextColor("white")
        menu_Tittle.setStyle("bold")
        menu_Tittle.setSize(24)
        menu_Text = Text(Point(self.win.getWidth()/2,self.win.getHeight()/2),"Please pick one of the following options:") #Fixed from Original Project
        menu_Text.setSize(14)
        menu_Text.setTextColor("white")
        menu_Tittle.draw(self.win)
        menu_Text.draw(self.win)
        option_1 = Button(self.win, Point(self.win.getWidth()*0.35,self.win.getHeight()*0.35), 75, 20, "EASY") #Button 1 for Easy
        option_2 = Button(self.win, Point(self.win.getWidth()*0.35,self.win.getHeight()*0.30), 75, 20, "MEDIUM") #Button 2 for Medium
        option_3 = Button(self.win, Point(self.win.getWidth()*0.35, self.win.getHeight()*0.25),75, 20, "HARD") #Button 3 for Hard
        option_1.activate() #Activate the button 1
        option_2.activate() #Activate 2
        option_3.activate() #Activate 3
        text_Option_1 = Text(Point(self.win.getWidth()-self.win.getWidth()*0.35, self.win.getHeight()*0.35), "2 Sections, 32 Lives") #Explination for button 1 (5 games and 20 lives)
        text_Option_1.setFill("white")
        text_Option_2 = Text(Point(self.win.getWidth()-self.win.getWidth()*0.35, self.win.getHeight()*0.30), "4 Sections, 24 Lives") #Explination for button 2 (10 games and 15 lives)
        text_Option_2.setFill("white")
        text_Option_3 = Text(Point(self.win.getWidth()-self.win.getWidth()*0.35, self.win.getHeight()*0.25), "6 Sections, 16 Lives") #Explination for button 3 (15 games and 10 lives)
        text_Option_3.setFill("white")
        text_Option_1.draw(self.win) 
        text_Option_2.draw(self.win) 
        text_Option_3.draw(self.win) 
        while True:
            p1 = self.win.getMouse()
            if option_1.clicked(p1):
                games, lives = 2, 32
                break
            elif option_2.clicked(p1):
                games, lives = 4, 24
                break
            elif option_3.clicked(p1):
                games, lives = 6, 16
                break
        menu_Tittle.undraw()
        menu_Text.undraw()
        option_1.undraw()
        option_2.undraw()
        option_3.undraw()
        text_Option_1.undraw() #Undraw button 1
        text_Option_2.undraw() #Undraw button 2
        text_Option_3.undraw() #Undraw button 3
        return games, lives
    
    '''
        The function to tell the player how many points it has at the moment.
        Of course, the amount of numeric points that the player has in the overall game is not deleted
        for it is comulative.
    '''
    def point_Screen(self, level, current_rating):
        '''
            Function to draw the screen of points (the screen that comes after a maze is won or lost).
            Needs current level (level) and the current score of the player (current_rating)

            Return 1 or 0 to see and quit game
        '''
        self.win.setBackground("black")
        text = Text(Point(self.win.getWidth()/2, self.win.getHeight()/2),"GAINED POINTS at level {a} = {b}".format(a = level, b = current_rating))
        text.setStyle("bold")
        text.setSize(24)
        text.setTextColor("white")
        option_1 = Button(self.win, Point(self.win.getWidth()*0.35,self.win.getHeight()*0.35), 75, 20, "OK!")
        option_2 = Button(self.win, Point(self.win.getWidth()*0.35,self.win.getHeight()*0.30), 75, 20, "QUIT!")
        option_1.activate()
        option_2.activate()
        text_Option_1 = Text(Point(self.win.getWidth()-self.win.getWidth()*0.35, self.win.getHeight()*0.35), "Next Level")
        text_Option_1.setFill("white")
        text_Option_2 = Text(Point(self.win.getWidth()-self.win.getWidth()*0.35, self.win.getHeight()*0.30), "To Start")
        text_Option_2.setFill("white")
        text.draw(self.win)
        text_Option_1.draw(self.win)
        text_Option_2.draw(self.win)
        while True:
            p = self.win.getMouse()
            if option_1.clicked(p):
                answer = True
                break
            elif option_2.clicked(p):
                answer = False
                break
        text.undraw()
        text_Option_1.undraw()
        text_Option_2.undraw()
        option_1.undraw()
        option_2.undraw()
        return answer
        
if __name__ == "__main__":
    win = GraphWin("Menu Test", 600, 600)
    menu = Menu(win)
    menu.generate_Instructions()
    win.close()