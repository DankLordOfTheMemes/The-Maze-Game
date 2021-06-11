from graphics import *
from player import Player
from maze import Maze
from menu import Menu

'''
    Processes Class (The class that will unite everything!)
'''
class Processes:
    def __init__(self):
        self.__window_W = 600 #Starndard width of window
        self.__window_H = 600 #Standard height of window
    
    '''
        Function to run the base Maze Game
    '''
    def run(self):
        '''
            Function to run the base Maze Game
        '''
        self.win = GraphWin("A MAZE GAME", self.__window_W, self.__window_H)
        self.win.setCoords(0,0,self.__window_W, self.__window_H)
        while True:
            menus = Menu(self.win) #Create Menu Object
            menus.generate_Instructions() #Draw the Instruction Menu on screen
            games, lives = menus.difficulty_Menu() #Draw the Difficulty Menu and return a value for games (amount of games) and lives (ammount of lives)
            maze = Maze(self.win) #Create Maze Object
            player = Player(self.win, games, lives) #Create Player Object
            for i in range(games):
                maze.set_Maze_COLOR() #Set color of Maze
                maze.change_Maze_WIDTH(i) #Set halls width of maze
                player.set_Arrow_COLOR() #Set the color of the arrow of player
                maze.generate_Maze() #Draw and create Maze
                while True:
                    point_A = self.win.getMouse() #Get first point as point_A
                    if player.is_Within_START(point_A, maze.get_Maze_Hall_WIDTH()): #Check that point is not at any other location that is not near the leftmost portion of the maze
                        break
                point_A.draw(self.win)
                player.add_user_Points(point_A) #Add point to list of player points
                while player.player_timeout() == False and player.player_win(maze.get_Maze_Hall_WIDTH()) == False: #Run while player hasnt lost or won
                    point_A = player.generate_Path(point_A,maze.get_Maze_Hall_WIDTH(), maze.get_Maze_WALLS()) #Generate path of player
                self.__undraw_Screen(maze,player) #Undraw the screen with Maze and Player class methods
                player.calculate_RatingPoints(maze.get_Maze_Hall_WIDTH()) #Calculate the current score (rating) of player
                if (player.player_timeout() == True and player.player_win(maze.get_Maze_Hall_WIDTH()) == False) or menus.point_Screen(i+1, player.get_currentRatingPoints()) == False:
                    self.__destroy_Screen(maze, player) #Delete the list variables from the Maze and Player classes
                    break #Kill game
                self.__destroy_Screen(maze, player) #Same as above
    
    '''
        Functions to undraw and destroy the screen. What it is meant is this:
        1. __undraw_Screen needs Maze and Player Objects to call on their methods to undraw the screen
        2. __destroy_Screen needs Maze and Player Objects to call on their methods to delete their related lists
    '''
    def __undraw_Screen(self, maze, player):
        '''
            Function to undraw the screen of Maze and Player Objects
        '''
        maze.undraw_Maze()
        player.undraw_Player()
    def __destroy_Screen(self, maze, player):
        '''
            Function to delete Maze and Player related lists
        '''
        maze.destroy_Maze()
        player.destroy_Player()

    '''
        Getter of __windowW
    '''
    def get_Window_WIDTH(self):
        '''
            Returns the width of the window of the game
        '''
        return self.__window_W
    
    '''
        Getter of __windowH
    '''
    def get_Window_HEIGHT(self):
        '''
            Returns the height of the window of the game
        '''
        return self.__window_H

if __name__ == "__main__":
    process = Processes()
    process.run()
    
        
