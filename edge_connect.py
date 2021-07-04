from player import *
from maze import *
from random import randint

class Edge_Connector:
    
    def __init__(self, jumps_number = 3):
        self.__randDF = None
        self.__jumps = jumps_number
    
    def get_RandDF(self):
        return self.__randDF
    
    def get_Jumps(self):
        return self.__jumps
    
    def set_Jumps(self, jumps_number):
        try:
            if jumps_number > -1:
                self.jumps = jumps_number
            else:
                raise ValueError
        except ValueError:
            print("The given value for jumps_number is less than 0. It cant be that!")
    
    def change_Loc(self, player, maze):
        self.__randDF = randint(2,4)
        if player.get_Lines()[len(player.get_Lines())-1].get_Entity().getP2().getX()*self.__randDF <= maze.get_Window().getWidth():
            self.__jumps = self.__jumps - 1
            return player.get_Lines()[len(player.get_Lines())-1].get_Entity().getP2().getX()*self.__randDF
        else:
            return self.change_Loc(player,maze)
    
    def is_jumping(self, player, maze):
        if self.__jumps > 0 and (player.get_Lines()[len(player.get_Lines())-1].get_Entity().getP2().getY() >= maze.get_Window().getHeight()-maze.get_Hall_Width()/2 or player.get_Lines()[len(player.get_Lines())-1].get_Entity().getP2().getY() <= maze.get_Hall_Width()/2):
            return True
        return False
    

    

