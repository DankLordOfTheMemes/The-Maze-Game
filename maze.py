from random import random, randint
from graphics import *
from button import *
from entity import *

class Maze:
    
    def __init__(self, window, hall_Width, color_case = None):
        self.__window = window
        self.__hall_Width = hall_Width
        self.__cc = color_case
        self.__section = {}

        self.__colors = {0:color_rgb(255,0,0), 1:color_rgb(255,128,0), 2: color_rgb(255,255,0), 3: color_rgb(128,255,0), 4: color_rgb(0,255,255), 5:color_rgb(0,128,255), 6:color_rgb(0,0,255), 7:color_rgb(127,0,255), 8:color_rgb(255,0,255), 9:color_rgb(255,0,127), 10: color_rgb(128,128,128)}
        
    
    def set_Window(self, window):
        try:
            if isinstance(window, GraphWin):
                self.__window = window
            else:
                raise TypeError
        except TypeError:
            print("The given window object is not of type GraphWin!")
    
    def set_Hall_Width(self, hall_Width):
        self.__hall_Width = hall_Width
    
    def set_Section(self, section):
        try:
            if isinstance(section, dict) and is_Entities(section):
                self.__section = section
            else:
                raise TypeError
        except TypeError:
            print("The given section variable is not valid! It must be both a dictionary element which contains only entities elements!")
    
    def set_CC(self, cc):
        self.__cc = cc
    
    def generate_CC(self):
        self.__cc = randint(-1, len(self.__colors)-1)

    def get_Window(self):
        return self.__window
    
    def get_Hall_Width(self):
        return self.__hall_Width
    
    def get_Section(self):
        return self.__section
    
    def get_Section_Walls(self):
        if "walls" in self.__section.keys():
            return self.__section["walls"]
        return IndexError("There are no walls in the maze!")

    def get_Section_Bounds(self):
        if "bounds" in self.__section.keys():
            return self.__section["bounds"]
        return IndexError("There are no bounds in the maze!")

    def get_Section_Buttons(self):
        if "buttons" in self.__section.keys():
            return self.__section["buttons"]
        return IndexError("There are no buttons in the maze!")
    
    def get_CC(self):
        return self.__cc

    def get_Colors(self):
        return self.__colors

    def generate_Maze_Section(self):
        if "walls" not in self.__section.keys():
            self.__section["walls"] = []

        for x in range(0, self.__window.getWidth(), self.__hall_Width):
            for y in range(int(self.__window.getHeight()/6), self.__window.getHeight(), self.__hall_Width):
                if self.__cc == -1:
                    color = self.__colors[randint(0, len(self.__colors)-1)]
                else:
                    color = self.__colors[self.__cc]
                
                if random() > 0.5:
                    wall = Line(Point(x,y), Point(x+self.__hall_Width,y+self.__hall_Width))
                else:
                    wall = Line(Point(x,y+self.__hall_Width), Point(x+self.__hall_Width,y))

                wall.setFill(color)
                wall.draw(self.__window)
                self.__section["walls"].append(Entity(wall, color))
        
        if "bounds" not in self.__section.keys():
            self.__section["bounds"] = []
        
        button_Area = Rectangle(Point(0,0), Point(self.__window.getWidth(), int(self.__window.getHeight()/6)))
        button_Area.setFill(color_rgb(220,220,220))
        button_Area.draw(self.__window)
        self.__section["bounds"].append(Entity(button_Area, color_rgb(220,220,220)))

        start_Area = Line(Point(self.__hall_Width/2, int(self.__window.getHeight()/6)), Point(self.__hall_Width/2, self.__window.getHeight()))
        start_Area.setFill(color_rgb(184,15,10))
        start_Area.draw(self.__window)
        self.__section["bounds"].append(Entity(start_Area, color_rgb(184,15,10)))
        
        end_Area = Line(Point(self.__window.getWidth()-self.__hall_Width/2, int(self.__window.getHeight()/6)), Point(self.__window.getWidth()-self.__hall_Width/2, self.__window.getHeight()))
        end_Area.setFill(color_rgb(153,153,0))
        end_Area.draw(self.__window)
        self.__section["bounds"].append(Entity(end_Area, color_rgb(153,153,0)))
        
        if "buttons" not in self.__section.keys():
            self.__section["buttons"] = []
        
        clear_Button = Button(self.__window, Point(self.__window.getWidth()*(0.20), self.__window.getHeight()*0.07),90,20,"Reset Lines")
        clear_Button.activate()
        self.__section["buttons"].append(clear_Button)

        Menu_Button = Button(self.__window, Point(self.__window.getWidth()*(0.80), self.__window.getHeight()*0.07),90,20,"Quit Menu")
        Menu_Button.activate()
        self.__section["buttons"].append(Menu_Button)

    def undraw_Section(self):
        for entity in self.__section["walls"]:
            entity.get_Entity().undraw()
        
        for entity in self.__section["bounds"]:
            entity.get_Entity().undraw()

        for entity in self.__section["buttons"]:
            entity.undraw()
    
    def clear_Section(self):
        self.__section.clear()

if "__main__" == __name__:
    window = GraphWin("Test Maze Section", 600, 600)
    window.setCoords(0,0,600,600)
    m_section = Maze(window, 20,-1)
    m_section.generate_Maze_Section()
    s = window.getMouse()

