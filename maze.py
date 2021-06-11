from random import randint, random
from graphics import *
from button import *

'''
    Maze Class
'''
class Maze:
    def __init__(self, window):
        '''
            Constructor of the Maze class! It only needs the window in which it will be drawn.
            The original value of the width of the halls of the maze is 40.
        '''
        self.__win = window #The window in which the maze will be drawn
        self.__maze_Walls = [] #The list that will contain the walls
        self.__bounds = [] #The bounds that the maze will have. (Like out of bounds in other games)
        self.__buttons = []
        self.__maze_Hall_WIDTH = 40 #Width of the maze halls
        self.__color = None #Color of the maze walls

    
    '''
        Generate maze function with the aid of http://www.grantjenks.com/docs/freegames/maze.html
        Of course, had to edit this function in my own way to make it to properly generate the maze
        with the use of graphics.py
    '''
    def generate_Maze(self):
        '''
            Function to generate the maze and draw it. This type of maze is diagonal not horizonal as the other ones in books.
            This function does not choose the color of the maze or the width of the walls!

            Void
        '''
        self.__win.setBackground("white")
        for x in range(0,self.__win.getWidth(),self.__maze_Hall_WIDTH):
            for y in range(100,self.__win.getHeight(),self.__maze_Hall_WIDTH):
                #Right-Left, Left-Right
                if random() > 0.5:
                    l = Line(Point(x,y), Point(x+self.__maze_Hall_WIDTH,y+self.__maze_Hall_WIDTH))
                    l.setFill(self.__color) #Set the color of the maze wall line
                    l.draw(self.__win) #Generate new maze wall line
                    self.__maze_Walls.append(l) #Add new wall to list
                else:
                    l = Line(Point(x,y+self.__maze_Hall_WIDTH), Point(x+self.__maze_Hall_WIDTH,y))
                    l.setFill(self.__color)
                    l.draw(self.__win)
                    self.__maze_Walls.append(l)
        
        button_Area = Rectangle(Point(0,0), Point(self.__win.getWidth(), 100))
        button_Area.setFill("gray")
        button_Area.draw(self.__win)
        self.__bounds.append(button_Area)
        '''
        Draw the vertical line that will simbolyze the starting bounds
        '''
        start = Line(Point(self.__maze_Hall_WIDTH/2,100),Point(self.__maze_Hall_WIDTH/2,self.__win.getHeight()))
        start.setFill(color_rgb(184,15,10))
        start.draw(self.__win)
        self.__bounds.append(start)

        clear_Lines_Button = Button(self.__win, Point(self.__win.getWidth()*(0.20), self.__win.getHeight()*0.07),90,20,"Reset Lines")
        clear_Lines_Button.activate()
        self.__buttons.append(clear_Lines_Button)

        to_Menu_Button = Button(self.__win, Point(self.__win.getWidth()*(0.80), self.__win.getHeight()*0.07),90,20,"Quit Menu")
        to_Menu_Button.activate()
        self.__buttons.append(to_Menu_Button)



    
    '''
        Function to pick one of the three mazes colors. This color is set to be picked
        at random. To give some flavour to the generated maze.
    '''
    def set_Maze_COLOR(self):
        '''
            This function chooses, to some extent, at random, the color of the walls of the maze.
            The three possible colors are:
            1. RGB(11,102,35)
            2. RGB(253,106,2)
            3. Black

            Returns the color of the maze.
        '''
        r = randint(1,3)
        if r == 1:
            self.__color = color_rgb(11,102,35)
        elif r ==2:
            self.__color = color_rgb(253,106,2)
        else:
            self.__color = "black"
    
    '''
        This is the get function of the color of the maze
    '''
    def get_Maze_Color(self):
        '''
            Function that returns the current maze color of walls
        '''
        return self.__color
    
    '''
        This function will add walls to the maze one by one.
    '''
    def add_Maze_WALLS(self, wall):
        '''
            Function that adds walls to the maze. The walls are of type Line
        '''
        if isinstance(wall,Line) == False:
            raise TypeError("The given valie of 'wall' is of not type Line as in graphics.Line!")            
        self.__maze_Walls.append(wall)
    
    '''
        Get function of the list of walls of the maze.
    '''
    def get_Maze_WALLS(self):
        '''
            This function will return the list of walls in the maze. (Lines, that is...)
        '''
        return self.__maze_Walls
    
    '''
        Function that will add the bounds of the maze one by one. By bounds we mean the out of limits area of the maze. (This is only cosmethic!)
    '''
    def add_Maze_Bounds(self, bounds):
        '''
            Function that will add the bounds of the maze by a parameter that will be of type Line as in graphics.Line
        '''
        if isinstance(bounds,Line) == False:
            raise TypeError("The valie of bounds is of not type Line!")
        self.__bounds.append(bounds)
    
    '''
        Get method of the list of bounds in the maze!
    '''
    def get_Maze_Bounds(self):
        '''
            Function that will return a list of the bounds of the maze!
        '''
        return self.__bounds
    
    '''
        Get of the width of the halls of the maze. Original value is at 40.
    '''
    def get_Maze_Hall_WIDTH(self):
        '''
            Function that will return the value of the width of the halls of the maze.
        '''
        return self.__maze_Hall_WIDTH
    '''
        Get the buttons of the maze.
    '''
    def get_Maze_Buttons(self):
        '''
            Function that will return the buttons of the maze.
        '''
        return self.__buttons
    '''
        Function to change the width of the halls of the maze by an amount.
    '''
    def change_Maze_WIDTH(self, current_Level, modifier=5):
        '''
            Function to change (substract) the width of the halls of the maze by a certain modifier amount.
            The width of the halls must be greater than the modifer in order for this to work.
            It needs the current level of the maze in order to work as well for it will decide when the method will work.
            Example:
            If the current level is 5 and the modifier is 5, then the width will change by 5 because 5 mod 5 = 0. Also when level is 0,
            this will not work for its believed as start of game.
        '''
        if current_Level%5 == 0 and current_Level != 0 and modifier < self.__maze_Hall_WIDTH:
            self.__maze_Hall_WIDTH = int(self.__maze_Hall_WIDTH - modifier)
    
    '''
        Function to undraw the maze from screen.
    '''
    def undraw_Maze(self):
        '''
            This function undraws the maze walls and bounds (lines) from screen.
        '''
        for i in self.__bounds:
            i.undraw()
        for i in self.__maze_Walls:
            i.undraw()
        for i in self.__buttons:
            i.undraw()
    
    '''
        Function to destroy the data of the maze (Since the variables are lists!)
    '''
    def destroy_Maze(self):
        '''
            This function will delete the data of the maze.
        '''
        self.__bounds.clear()
        self.__maze_Walls.clear()
    '''
        Function will reset the width of the halls of the maze to 40
    '''
    def reset_Atribute(self):
        '''
            Function will reset the width of the halls of the maze to 40.
        '''
        self.__maze_Hall_WIDTH = 40

if __name__ == "__main__":
    window = GraphWin("Maze Test", 300, 300)
    window.setCoords(0,0,300,300)
    maze = Maze(window)
    maze.set_Maze_COLOR()
    maze.generate_Maze()
    window.getMouse()
    maze.undraw_Maze()
    maze.destroy_Maze()
    window.close()
