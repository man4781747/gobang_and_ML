# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 16:48:45 2017

@author: Chuanping_LASC_PC
"""

import numpy as np

class gobang_brain:
    def __init__(self,checkerboard):
        self.checkerboard = checkerboard

    def end_and_win(self):
        self.Column_check = np.zeros((5,1))+1
        self.Row_check = np.zeros((1,5))+1
        self.Right_oblique_check = np.eye(5,5)
        self.Left_oblique_check = np.array([[0,0,0,0,1],
                                            [0,0,0,1,0],
                                            [0,0,1,0,0],
                                            [0,1,0,0,0],
                                            [1,0,0,0,0]])
        game_end = False
        for i in range(len(self.checkerboard)-4):
            for j in range(len(self.checkerboard[0])):
                if abs(np.sum(self.checkerboard[i:i+5,j:j+1]*self.Column_check)) == 5:
                    game_end = True
                
        for i in range(len(self.checkerboard)):
            for j in range(len(self.checkerboard[0])-4):
#                print range(len(self.checkerboard[0])-4)
                if abs(np.sum(self.checkerboard[i:i+1,j:j+5]*self.Row_check)) == 5:
                    game_end = True                

        for i in range(len(self.checkerboard)-4):
            for j in range(len(self.checkerboard[0])-4):
                if abs(np.sum(self.checkerboard[i:i+5,j:j+5]*self.Right_oblique_check)) == 5 or abs(np.sum(self.checkerboard[i:i+5,j:j+5]*self.Left_oblique_check)) == 5:
                    game_end = True    
        return game_end 