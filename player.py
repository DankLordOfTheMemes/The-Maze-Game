from entity import *
from graphics import Line, Rectangle, Point

class Player:
    
    def __init__(self, point, color, collision = False, lives = 1):
        try:
            if (collision == None or isinstance(collision, bool)) and isinstance(lives, int) and lives > 0 and isinstance(point, Point):
                self.__collision = collision
                self.__entities = {"points": Entity(point, color)}
                self.__lives = lives
                self.__points = 0
            else:
                raise TypeError
        except TypeError:
            print("The values of either collision, entity, color and lives must be type bool(), Entity(), Str() and Int(), respectively! Also lives must be greater than zero (0) and the internal object of entity must be type Line()!")
    
    def set_Collision(self, collision):
        try:
            if isinstance(collision, bool):
                self.__collision = collision
            else:
                raise TypeError
        except:
            print("The entered value for collision is not of type bool!")
    
    def set_Lives(self, lives):
        try:
            if isinstance(lives, int) and lives >= 0:
                self.__lives = lives
            else:
                raise TypeError
        except TypeError:
            print("Remember! The value for lives must be of type Int() and greater than zero (0)!")

    def set_Points(self, points):
        self.__points = points
    
    def get_Collision(self):
        return self.__collision
    
    def get_Entities(self):
        return self.__entities
    
    def get_Points(self):
        return self.__entities["points"]
    
    def get_Lines(self):
        return self.__entities["lines"]
    
    def get_Lives(self):
        return self.__lives
    
    def get_Points(self):
        return self.__points
    
    def add_Point(self, point, color):
        l_tmp = None
        if "lines" not in self.__entities.keys():
            self.__entities["lines"] = []
            l_tmp = Line(self.__entities["points"].get_Entity(), point)           
        else:
            l_tmp = Line(self.__entities["lines"][len(self.__entities["lines"])-1].get_Entity().getP2(), point)             

        return self.__entities["lines"].append(Entity(l_tmp, color))
    
    def add_Line(self, line, color):
        if "lines" not in self.__entities.keys():
            self.__entities["lines"] = []                        
        return self.__entities["lines"].append(Entity(line, color))
    
    def remove_Line(self, entity):
        self.__entities["lines"].remove(entity)
        return True
    
    def is_Alive(self):
        return self.__lives > 0

    def undraw_Player(self):

        self.__entities["points"].get_Entity().undraw()
        
        for entity in self.__entities["lines"]:
            entity.get_Entity().undraw()

    def reset_Player(self):
        l_Points = self.__points
        self.__collision = False
        self.__entities.clear()
        self.__lives = 1
        self.__points = 0
        return l_Points

    def __is_Counter_Clockwise(self, point_A, point_B, point_C):
        return (point_C.getY()-point_A.getY())*(point_B.getX()-point_A.getX()) > (point_B.getY() - point_A.getY())*(point_C.getX()-point_A.getX())

    def __is_Within(self, point, rectangle):
        if rectangle.getP1().getX() < rectangle.getP2().getX():
            if rectangle.getP1().getY() < rectangle.getP2().getY():
                return point.getX() >= rectangle.getP1().getX() and point.getX() <= rectangle.getP2().getX() and point.getY() >= rectangle.getP1().getY() and point.getY() <= rectangle.getP2().getY()
            else:
                return point.getX() >= rectangle.getP1().getX() and point.getX() <= rectangle.getP2().getX() and point.getY() <= rectangle.getP1().getY() and point.getY() >= rectangle.getP2().getY()
        else:
            if rectangle.getP1().getY() < rectangle.getP2().getY():
                return point.getX() <= rectangle.getP1().getX() and point.getX() >= rectangle.getP2().getX() and point.getY() >= rectangle.getP1().getY() and point.getY() <= rectangle.getP2().getY()
            else:
                return point.getX() <= rectangle.getP1().getX() and point.getX() >= rectangle.getP2().getX() and point.getY() <= rectangle.getP1().getY() and point.getY() >= rectangle.getP2().getY()
    
    def is_Collide(self, obj):
        if self.__collision == True and isinstance(obj, Line):
            return self.__is_Counter_Clockwise(obj.getP1(), self.__entities["lines"][len(self.__entities["lines"])-1].get_Entity().getP1(), self.__entities["lines"][len(self.__entities["lines"])-1].get_Entity().getP2()) != self.__is_Counter_Clockwise(obj.getP2(), self.__entities["lines"][len(self.__entities["lines"])-1].get_Entity().getP1(), self.__entities["lines"][len(self.__entities["lines"])-1].get_Entity().getP2()) and self.__is_Counter_Clockwise(obj.getP1(), obj.getP2(), self.__entities["lines"][len(self.__entities["lines"])-1].get_Entity().getP1()) != self.__is_Counter_Clockwise(obj.getP1(), obj.getP2(), self.__entities["lines"][len(self.__entities["lines"])-1].get_Entity().getP2())
        elif self.__collision and isinstance(obj, Rectangle):
            return self.__is_Within(self.__entities["lines"][len(self.__entities)-1].get_Entity().getP2(),obj)
        return False

def is_Within_Start(point, bound):
    return point.getX() <= bound.get_Entity().getP1().getX()

def is_Within_End(point, bound):
    return point.getX() >= bound.get_Entity().getP1().getX()
