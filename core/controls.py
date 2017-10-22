# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import pygame
class Control:
    pressed = None
    move_x = move_y = 0
    
    def get_event(self, key_event):
        self.pressed = key_event
    
    def check_key(self):
         if self.pressed[pygame.K_UP]:
            self.move_x = 0
            self.move_y = -5
         elif self.pressed[pygame.K_DOWN]:
            self.move_x = 0
            self.move_y = 5
         elif self.pressed[pygame.K_LEFT]:
            self.move_x = -5
            self.move_y = 0
         elif self.pressed[pygame.K_RIGHT]:
            self.move_x = 5
            self.move_y = 0
         else:
            self.move_x = 0
            self.move_y = 0
        

    def get_x(self):
        return self.move_x;
  
    def get_y(self):
        return self.move_y
    
    
         