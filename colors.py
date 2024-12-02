#defined colors to call on grid.py and main.py
class Colors: 
    black = (26, 31, 40)
    green = (47, 230, 23)
    red = (232, 18, 18)
    orange = (226, 116, 17)
    yellow = (237, 234, 4)
    purple = (255, 87, 51)
    cyan = (21, 204, 209)
    blue = (13, 64, 216)
    white = (255, 255, 255)
    dark_blue = (44, 44, 127)
    light_blue = (59, 85, 162)
    light_grey = (120, 120, 120)

    
    #define method used to call class and not instance of class
    @classmethod
    def get_cell_colors(cls):
         #order of colors matter 
        return[cls.light_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue, cls.black]
