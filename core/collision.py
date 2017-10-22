# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

class Collision:
    width = height = move_x = move_y =0
    #get widdth and hreight
    def set_width_and_height(self, x, y):
        self.width = x 
        self.height = y
    
    def get_move(self, x, y):
        self.move_x = x
        self.move_y = y
    
    def check_board(self, x, y):
        x += self.move_x
        y += self.move_y
        print (x,y)
        move_available = True
        if (x > self.width) or (x == 0):
            move_available = False 
        if (y > self.height) or (y == 0):
            move_available = False
        if (y == 0) and (x == 0):
            move_available = False
        return move_available
