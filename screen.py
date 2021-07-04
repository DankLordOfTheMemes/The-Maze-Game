from graphics import *
from maze import *
from player import *
from edge_connect import *

class Screen:

    def __init__(self, window, hall_width, color_case):
        self.__window = window
        self.__hall_width = hall_width
        self.__color_case = color_case
    
    def run(self):
        
        while True:
            some_Point = None
            maze = Maze(self.__window, self.__hall_width, self.__color_case)
            maze.generate_Maze_Section()
            
            while True:
                some_Point = self.__window.getMouse()
                if is_Within_Start(some_Point, maze.get_Section_Bounds()[1]):
                    break

            player = Player(some_Point, "black", True, 100)
            #player.get_Points().get_Entity().draw(self.__window)
            
            connector = Edge_Connector()

            while player.is_Alive() == True and is_Within_End(some_Point, maze.get_Section_Bounds()[2]) == False:
                is_removed = False
                lives_Text = Text(Point(maze.get_Window().getWidth()/2, maze.get_Window().getHeight()*0.07), "{a}".format(a =player.get_Lives()))
                lives_Text.draw(self.__window)
                some_Point = self.__window.getMouse()
                player.add_Point(some_Point, "black")
                for wall in maze.get_Section_Walls():
                    if player.is_Collide(wall.get_Entity()):
                        is_removed = player.remove_Line(player.get_Lines()[len(player.get_Lines())-1])
                        print(is_removed)
                        break
                if is_removed == False:
                    player.get_Lines()[len(player.get_Lines())-1].get_Entity().draw(self.__window)
                    player.set_Lives(player.get_Lives()-1)
                    player.set_Points(player.get_Points()+100)
                lives_Text.undraw()
                if connector.is_jumping(player, maze):
                    some_tmp = connector.change_Loc(player, maze)
                    player.add_Line(Line(Point(some_tmp, player.get_Lines()[len(player.get_Lines())-1].get_Entity().getP2().getY()), Point(some_tmp + 5, player.get_Lines()[len(player.get_Lines())-1].get_Entity().getP2().getY())), "Black")
                    player.get_Lines()[len(player.get_Lines())-1].get_Entity().draw(self.__window)

    def __reset_Screen(self, player, maze):
        maze.undraw_Section()
        maze.clear_Section()
        player.undraw_Player()
        return player.reset_Player()
    


if __name__ == "__main__":
    graph = GraphWin("Screen Test", 600, 600)
    graph.setCoords(0,0,600,600)
    s = Screen(graph, 20, -1)
    s.run()
    click = graph.getMouse()