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
        self.__Maze_Sections = []
    
    def run(self):
        win = GraphWin("The Maze", self.__window_W, self.__window_H)
        win.setCoords(0,0, self.__window_W, self.__window_H)
        while True:
            menus = Menu(win)
            menus.generate_Instructions()
            sections, lives = menus.difficulty_Menu()
            for i in range(sections):
                maze_Section = Maze(win)
                self.__Maze_Sections.append(maze_Section)
            player =  Player(win, lives)
            player