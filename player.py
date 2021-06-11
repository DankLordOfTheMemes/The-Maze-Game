from entity import *
from graphics import Line, Rectangle, Point

class Player:
    
    def __init__(self, entity, collision = False, lives = 1):
        try:
            if (collision == None or isinstance(collision, bool)) and isinstance(entity, Entity) and isinstance(lives, int) and lives > 0 and isinstance(entity.getEntity(), Line):
                self.__collision = collision
                self.__entities = [entity]
                self.__lives = lives
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
            if isinstance(lives, int) and lives > 0:
                self.__lives = lives
            else:
                raise TypeError
        except TypeError:
            print("Remember! The value for lives must be of type Int() and greater than zero (0)!")

    def get_Collision(self):
        return self.__collision
    
    def get_Entities(self):
        return self.__entities
    
    def get_Lives(self):
        return self.__lives
    
    def add_Point(self, point, color):
        try:
            if isinstance(point, Point):
                l_tmp = Line(self.__entities[len(self.__entities)-1].getP2(), point)
                self.__entities.append(Entity(l_tmp, color))
            else:
                raise TypeError
        except:
            print("The given values for point and color are not of type Point() and Str()!")

    def remove_Entity(self, entity):
        self.__entities.remove(entity)
    
    def reset_Player(self):
        self.__collision = False
        self.__lives = 1
        self.__entities.clear()

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
        if self.__collision and isinstance(obj, Line):
            return self.__is_Counter_Clockwise(obj.getP1(), self.__entitities[len(self.__entities)-1)].get_Entity().getP1(), self.__entitities[len(self.__entities)-1)].get_Entity().getP2()) != self.__is_Counter_Clockwise(obj.getP2(), self.__entitities[len(self.__entities)-1)].get_Entity().getP1(), self.__entitities[len(self.__entities)-1)].get_Entity().getP2()) and self.__is_Counter_Clockwise(obj.getP1(), obj.getP2(), self.__entitities[len(self.__entities)-1)].get_Entity().getP1()) != self.__is_Counter_Clockwise(obj.getP1(), obj.getP2(), self.__entitities[len(self.__entities)-1)].get_Entity().getP2())
        elif self.__collision and isinstance(obj, Rectangle):
            return self.__is_Within(self.__entities[len(self.__entities)-1].getEntity().getP2(),obj)
        return False
    