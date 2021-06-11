from graphics import *
from random import randint
from maze import Maze

'''
    This is the Player Class, it is organized as Setter (Or some other name that will set values; such, as add in lists) and Setter and so on
'''
class Player():
    def __init__(self, window, available_games, available_lives):
        '''
            Constructor of the class that will represent a player of the maze game. It has the following parameters:
            1. window which is the grahics window which all of this object will be drawn
            2. available_games is the number of games the player will play
            3. available_lives is the number of lives the player will have
        '''  
        self.__window = window #Window where the player will be drawn
        self.__games = available_games #The number of games the player will play
        self.__lives = available_lives #The number of lives the player will have
        self.__used_Lives = 0 #Number of lives the user has used.
        self.__rating = 0 #The score of the player (player_Points in the OG version)
        self.__user_Points = [] #The list that will have the points that the player picked when playing maze
        self.__user_Lines = [] #The list that will have the lines of the player when playing the maze
        self.__color = None #The color of the lines of the player.
    
    '''
        Setter of __games (The amount of games player will play)
    '''
    def set_game_Count(self,count):
        '''
            Set the amount of games the player will play with count parameter
        '''
        self.__games = count
    
    '''
        Getter of __games
    '''
    def get_game_Count(self):
        '''
            Returns the number of games player will play
        '''
        return self.__games
    
    '''
        Setter of __lives (Lives of player)
    '''
    def set_lives_Count(self,count):
        '''
            Sets the number of lives the player will have with count parameter
        '''
        self.__lives = count
    
    '''
        Getter of __lives
    '''
    def get_Lives_Count(self):
        '''
            Returns the number of lives the player has
        '''
        return self.__lives
    
    def set_used_Lives(self, count):
        self.__used_Lives = count
    
    def get_used_Lives(self):
        return self.__used_Lives
    
    '''
        Getter of the current score (rating) of the player in the game
    '''
    def get_currentRatingPoints(self):
        '''
            Returns the value of the current score of the player in the game
        '''
        return self.__rating
    
    '''
        Function to calculate the numeric points the player will have throughout his or her playthrough. hall_Width is the value of
        maze_Hall_WIDTH
    '''
    def calculate_RatingPoints(self, hall_Width):
        '''
            Function to calculate the points the player will have in a game. In order to work it needs a hall_Width parameter which
            is another name for maze_Hall_Width!
        '''
        if (self.__user_Points[-1].getY() <= hall_Width/4 or self.__user_Points[-1].getY() >= self.__window.getHeight()-hall_Width/4):
            self.__rating = self.__rating + 25*(len(self.__user_Lines)) + 50*(self.__lives-(len(self.__user_Lines)))
        elif self.player_timeout() == True:
            self.__rating =  self.__rating + 50 * self.__lives
        else:
            self.__rating =  self.__rating + 50*(len(self.__user_Lines)) + 100*(self.__lives-(len(self.__user_Lines)))

    '''
        Function to add one point to list of points (__user_Points) of the player.
    '''
    def add_user_Points(self, point):
        '''
            This function will add one point of type Point to the list of points of the player.
        '''
        if isinstance(point, Point) == False:
            raise TypeError("The given value of point is not of type Point!")
        self.__user_Points.append(point)
    
    '''
        Getter of __user_Points
    '''
    def get_user_Points(self):
        '''
            Function that returns a list of the points that the player has set on the maze.    
        '''
        return self.__user_Points
    
    '''
        Adds one line to the list of lines __user_Lines that the player has.
    '''
    def add_user_Lines(self, line):
        '''
            Adds one line (since parameter) of type Line to the list of lines of the player (the lines he played)
        '''
        if isinstance(line, Line) == False:
            raise TypeError("The given value of line is not of type Line!")
        self.__user_Lines.append(line)
    
    '''
        Getter of __user_Lines
    '''
    def get_user_Lines(self):
        '''
            Returns the list of lines that the player has played!
        '''
        return self.__user_Lines
    
    '''
        Function to pick one of the three possible colors to the user will sey as path. 
        This color is picked at random.
    '''
    def set_Arrow_COLOR(self):
        '''
            Function to choose, to some extent, at random, the color of the player arrow (line). The possible values are:
            1. RGB(15,82,186)
            2. RGB(54,54,54)
            3. RGB(143,0,255)

            Returns the color of arrow
        '''
        r = randint(1,3)
        if r == 1:
            self.__color = color_rgb(15,82,186)
        elif r == 2:
            self.__color = color_rgb(54,54,54)
        else:
            self.__color = color_rgb(143,0,255)
    
    '''
        Getter of the color of player arrow (line) as in __color
    '''
    def get_Arrow_COLOR(self):
        '''
            Returns the color of the player's arrow
        '''
        return self.__color
    
    '''
        Function to check if the first player's point is at the left-most point
        of the screen.
    '''
    def is_Within_START(self,point_A, hall_Width):
        '''
            Function that accepts a point and hall_Width (Width of Maze Halls) as parameter to check wether such point is at the leftmost part of the screen; hence, start!
            This is done by checking if the location of the X value of the point is less than the width of the maze halls divided by 2.

            Returns True if the first point is within start, false... otherwise.
        '''
        return (point_A.getX() <= hall_Width/2 and point_A.getY() > 100 + hall_Width/4)
    
    def is_Within_TOP(self, point_A, hall_Width):
        return (point_A.getY() > self.__window.getHeight() - hall_Width/4)
    
    def is_Within_DOWN(self, point_A, hall_Width):
        return (point_A.getY() < 100 + hall_Width/4)
    
    def is_Within_RIGHT(self, point_A, hall_Width):
        return (point_A.getX() > self.__window.getWidth() - hall_Width/4)
    
    '''
        Function to check if each of the last points that the user sets is near to the 
        point that he set as the first one, or like they say in Physics: its Origin, with
        the Point Distance Function. More so, this distance is evaluated in contrast with
        the width of the halls of the maze (hall_Width) to see that they are not reaaaally close.
    ''' 
    def is_Near(self,point_A, hall_Width):
        '''
            In contrary to popular belief, the name of this function lies for it does not check if the point is near to some other
            random point but to the first one that was plotted by the user. Hence, this function will check the distance between
            the last point the user plotted and his or her first one (Origin). This function needs a point and hall_Width
            (Width of Maze Halls) as parameters.
        
            Returns True if near, False otherwise.
        '''
        return ((point_A.getX()-self.__user_Points[0].getX())**2 + (point_A.getY()+self.__user_Points[0].getY())**2)**2 < hall_Width
    
    '''
        Function to calculate the slope of the line. This is useful to set the dirrections of
        the arrows of the lines. (UNUSED)
    '''
    def calculate_Slope(self,point_A, point_B):
        '''
            Function to obtain the Slope of a line, or two points, to be more precise. It needs two points as parameter. Returns slope value.
        '''
        return (point_B.getY()-point_A.getY())/(point_B.getX()-point_A.getX())
    
    '''
        This two functions I got them from an obscure site I found. (THANK GOD, I FOUND IT!)
        Its url is: https://bryceboe.com/2006/10/23/line-segment-intersection-algorithm/
        I knew, I needed it. Just didn't have the energy or the time to build such algorithm.
        What I needed was this: An Algorithm to check wether the line the player created didn't
        try to like 'Blitzkrieg' (https://www.history.com/topics/world-war-ii/blitzkrieg) through
        the walls of the halls of the maze so that he or she would win easily.
        I thought on creating a power-up to do that a couple of times, but scraped due to... well...
        time.
    '''
    def is_Counter_CLOCK(self,point_A, point_B,point_C):
        return (point_C.getY()-point_A.getY())*(point_B.getX()-point_A.getX()) > (point_B.getY() - point_A.getY())*(point_C.getX()-point_A.getX())

    def is_Interect(self,line, collision_walls):
        for wall in collision_walls: #Its not eficient, but had to do it: Check every wall of the maze for each line the player tried
            if (self.is_Counter_CLOCK(line.getP1(),wall.getP1(),wall.getP2()) != self.is_Counter_CLOCK(line.getP2(),wall.getP1(),wall.getP2())) and (self.is_Counter_CLOCK(line.getP1(),line.getP2(),wall.getP1()) != self.is_Counter_CLOCK(line.getP1(),line.getP2(),wall.getP2())):
                return True
        return False

    '''
        Function to generate the line, or path, the user would create to try and get to the screen edges
        and try to win the game. It needs point_A parameter, as previous point the player picked, to continue
        generating player's path, or segment, with the newly picked point_B.
    '''
    def generate_Path(self,point_A, hall_Width, collision_walls):
        '''
            Function to generate the path of the player. This function needs the previous point the player picked, the width of the halls
            of the maze (hall_Width) and the list of the walls in the maze (collision_walls).
        
            This function will return the last point the user picked.
        '''
        prompt = self.__window.getMouse() #Get player new point coordinates
        point_B = Point(prompt.getX(), prompt.getY()) #Create a new point with given coordinates
        l = Line(point_A, point_B) #Create a new line
        l.setArrow("last") #Set the arrow to direction to 'foward'. Found that this was better from using th slope function that I created. (Less complicated)
        l.setFill(self.__color) # As maze, set the color of the arrow.
        if self.is_Interect(l, collision_walls) == False and self.is_Near(point_B, hall_Width)== False: #Check if the newly created line is not near the Origin or intercecting the maze's lines.
            point_A = point_B #Set point_A to point_B
            self.__user_Points.append(point_A) #Add new point to list
            self.__user_Lines.append(l)#Add new line to list
            point_A.draw(self.__window)
            l.draw(self.__window) #Generate new line (draw)

        return point_A

    '''
        This is the same function, as the original, as finish_Check but with a proper name. It checks if the player lost all his or
        her lives. It returns True if so, False, otherwise. The reason it si not substracted is for the bounds list that the maze class has.
    '''
    def player_timeout(self):
        '''
            This function checks wether the player has any more lives (lines) to continue in the maze gameplay.

            Returns True if player lost, otherwise not.
        '''
        return self.__used_Lives == self.__lives
    
    '''
        Function to check if the player won in the generated maze.
        The player will win if his or her last point (to create a line) is out of
        starting bounds and near the edges of the up, right and down edges of the
        screen.
    '''
    def player_win(self, hall_Width):
        '''
        This function checks if the game is won. It occurs when the player reaches the rightmost, uppermost and downmost portion of the screen.
        This function needs a the value of the width of the halls of the maze.
        
        Returns True if win, false if not.
    '''
        return (self.is_Within_START(self.__user_Points[-1],hall_Width) == False) and (self.is_Within_TOP(self.__user_Points[-1], hall_Width == True) or self.is_Within_DOWN(self.__user_Points[-1], hall_Width == True) or self.is_Within_RIGHT(self.__user_Points[-1], hall_Width == True))

    '''
        Function to undraw the player (lines and points) from the screen
    '''
    def undraw_Player(self):
        '''
            Function that undraws the player from the screen (lines and points)
        '''
        for i in self.__user_Lines:
            i.undraw()
        for i in self.__user_Points:
            i.undraw()
    '''
        Function that deletes the values of the lists of lines and points the player has.
    '''
    def destroy_Player(self):
        '''
            Function that is needed to delete the lists of points and lines the player has.
        '''
        self.__user_Points.clear()
        self.__user_Lines.clear()
    '''
        Function to reset the __rating to 0
    '''
    def reset_Attributes(self):
        '''
            For player it resets the value of the current points he or she has gained througout the game
        '''
        self.__rating = 0
        self.__used_Lives = 0
    
if __name__ == "__main__":
    win = GraphWin("Player Test", 300, 300)
    win.setCoords(0,0,300,300)
    player = Player(win, 1, 5)
    player.set_Arrow_COLOR()
    print(player.get_game_Count())
    print(player.get_Lives_Count())
    print(player.get_Arrow_COLOR())
    p = win.getMouse()
    player.add_user_Points(p)
    while player.player_timeout() == False:
        p = player.generate_Path(p, 0, [])
    win.getMouse()
    player.destroy_Player()
    win.close()