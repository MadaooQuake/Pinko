# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

class Collision:
    width = height = 0
    #get widdth and hreight
    def set_width_andheight(self, x, y):
        self.width = x 
        self.height = y
    
    def check_board(self, x, y):
        print x