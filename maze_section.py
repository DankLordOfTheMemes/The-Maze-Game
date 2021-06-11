from random import random, randint
from graphics import *
from button import *
from entity import *

class Maze_Section:
    
    def __init__(self, window, hall_Width, color_case):
        self.__window = window
        self.__hall_Width = hall_Width
        self.__cc = color_case
        self.__section = {}

        self.__colors = {0:"Red", 1:"Orange", 2: "Yellow", 3: "Green", 4:"Cyan", 5:"Azure", 6:"Blue", 7:"Violet", 8:"Magenta", 9:"Rose", 10: "Brown"}
        
    
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
        if "walls" in self.__section.keys:
            return self.__section["walls"]
        return IndexError("There are no walls in the maze!")

    def get_Section_Bounds(self):
        if "bounds" in self.__section.keys:
            return self.__section["bounds"]
        return IndexError("There are no bounds in the maze!")

    def get_Section_Buttons(self):
        if "buttons" in self.__section.keys:
            return self.__section["buttons"]
        return IndexError("There are no buttons in the maze!")
    
    def get_CC(self):
        return self.__cc

    def get_Colors(self):
        return self.__colors
    
    def generate_Maze_Section(self):
        if "walls" not in self.__section.keys:
            self.__section["walls"] = []
        
        for x in range(0, self.__window.getWidth(), self.__hall_Width):
            for y in range(self.__control_Bounds, self.__window.getHeight(), self.__hall_Width):
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
        
        if "bounds" not in self.__section.keys:
            self.__section["bounds"] = []
        
        button_Area = Rectangle(Point(0,0), Point(self.__window.getWidth(), int(self.__window.getHeight()/6)))
        button_Area.setFill(color_rgb(220,220,220))
        button_Area.draw(self.__window)
        self.__section["bounds"].append(Entity(button_Area, color_rgb(220,220,220)))

        start_Area = Line(Point(self.__hall_Width/2, self.__control_Bounds), Point(self.__hall_Width/2, self.__window.getHeight()))
        start_Area.setFill(color_rgb(184,15,10))
        start_Area.draw(self.__window)
        self.set_Section["bounds"].append(Entity(start_Area, color_rgb(184,15,10)))
        
        if "buttons" not in self.__section.keys:
            self.__section["buttons"] = []
        
        clear_Button = Button(self.__win, Point(self.__win.getWidth()*(0.20), self.__win.getHeight()*0.07),90,20,"Reset Lines")
        clear_Button.activate()
        self.__section["buttons"].append(clear_Button)

        Menu_Button = Button(self.__win, Point(self.__win.getWidth()*(0.80), self.__win.getHeight()*0.07),90,20,"Quit Menu")
        Menu_Button.activate()
        self.__section["buttons"].append(Menu_Button)

    def undraw_Section(self):
        for key in self.__section.keys:
            for entity in self.__section[key]:
                entity.getEntity().undraw()
    
    def clear_Section(self):
        self.__section.clear()

    


