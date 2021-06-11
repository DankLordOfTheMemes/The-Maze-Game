from graphics import *

class Button:
    def __init__(self, win, center, width, height, label):
        w,h = width/2, height/2
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w,x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill("lightgray")
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()
    def clicked(self, p):
        return (self.active and self.xmin <= p.getX() <= self.xmax and self.ymin <= p.getY() <= self.ymax)
    def getLabel(self):
        return self.label.getText()
    def activate(self):
        self.label.setFill("black")
        self.rect.setWidth(2)
        self.active = True
    def deactivate(self):
        self.label.setFill("lightgray")
        self.rect.setWidth(1)
        self.active = False 

    '''
        Added function to delete buttons
    '''
    def undraw(self):
        self.rect.undraw()
        self.label.undraw()