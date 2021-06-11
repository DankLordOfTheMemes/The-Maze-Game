
class Entity:
    
    def __init__(self, obj = None, color = None):
        if (color == None or isinstance(color, str)):
            self.__entity = obj
            self.__color = color

    def set_Entity(self, obj):
        self.__entity = obj
    
    def set_Color(self, color):
        try:
            if isinstance(color, str):
                self.__color = color
            else:
                raise TypeError
        except TypeError:
            print("The entered value for color is not of type str!")
    
    def get_Entity(self):
        return self.__entity
       
    def get_Color(self):
        return self.__color
        
def is_Entities(entities):
    for entity in entities:
        if isinstance(entity, Entity):
            continue
        else:
            return False
    return True
                
        