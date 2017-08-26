# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 13:59:10 2017

@author: Chuanping_LASC_PC
"""

import Tkinter as tk
import numpy as np
import gobang_brain

#def callback(event):
##    print event.x_roof+event.y_roof
#    print "clicked at", event.x, event.y
#    return (event.x, event.y)

class Window:
    def __init__(self):
        self.x_num = 15
        self.y_num = 15
        self.end = False
        self.order = True
        
    def build_window(self):
        global checkerboard
        self.black_box = np.zeros((0,2),dtype=np.int16)
        self.white_box = np.zeros((0,2),dtype=np.int16)
        self.window = tk.Tk()
        self.window.geometry('1500x1000')
        self.black_win_count = 0
        self.white_win_count = 0
        self.black_win_count_var = tk.StringVar()
        self.white_win_count_var = tk.StringVar()
        self.label_black_win = tk.Label(self.window,textvariable=self.black_win_count_var).place(x= 1250,y=300)
        self.label_white_win = tk.Label(self.window,textvariable=self.white_win_count_var).place(x= 1250,y=400)
        self.black_win_count_var.set("Black_Goal: 0")
        self.white_win_count_var.set("White_Goal: 0")
        self.canvas = tk.Canvas(self.window,height=1000,width=1000,relief='sunken',bg='goldenrod2')
        self.unit = 1000/self.x_num
        unit = self.unit 
        [self.canvas.create_rectangle((i*unit,j*unit,(i+1)*unit,(j+1)*unit)) for i in range(15) for j in range(15) ]

        self.clear_butten = tk.Button(self.window,command=self.clear_broad,text='clear_broad').place(x = 1300,y= 500)

        self.canvas.bind("<Button-1>", self.callback)
        self.canvas.place(x=0,y=0)
    
    def clear_broad(self):
        global checkerboard
        checkerboard = np.zeros((15,15),dtype=np.int16)
        self.black_box = np.zeros((0,2),dtype=np.int16)
        self.white_box = np.zeros((0,2),dtype=np.int16)
        self.canvas.delete('whiteC','blackC')
        self.order = True
    
    def callback(self,event):
        global checkerboard
        self.click_x = event.x/self.unit
        self.click_y = event.y/self.unit
        if self.order:
            if checkerboard[self.click_x-1,self.click_y-1] == 0.:
                checkerboard[self.click_x-1,self.click_y-1] = 1
                self.order = False
                self.black_box = np.concatenate((self.black_box,np.array([[self.click_x,self.click_y]]))) 
                game_end = gobang_brain.gobang_brain(checkerboard).end_and_win()
                self.make_black()
        else:
            if checkerboard[self.click_x-1,self.click_y-1] == 0.:
                checkerboard[self.click_x-1,self.click_y-1] = -1
                self.order = True
                self.white_box = np.concatenate((self.white_box,np.array([[self.click_x,self.click_y]]))) 
                game_end = gobang_brain.gobang_brain(checkerboard).end_and_win()
                self.make_white()
        if game_end:
            if self.order :
                self.black_win_count += 1
                self.black_win_count_var.set("Black_Goal: {0}".format(self.black_win_count))
                self.clear_broad()
            else :
                self.white_win_count += 1
                self.white_win_count_var.set("White_Goal: {0}".format(self.white_win_count))
                self.clear_broad()             
        
        
        
    def make_white(self):
        [self.canvas.create_oval((self.white_box[white_num,0]*self.unit,
                                  self.white_box[white_num,1]*self.unit,
                                 (self.white_box[white_num,0]+1)*self.unit,
                                 (self.white_box[white_num,1]+1)*self.unit), fill='white',tags='whiteC') for white_num in range(len(self.white_box))]

    def make_black(self):
        [self.canvas.create_oval((self.black_box[black_num,0]*self.unit,
                                  self.black_box[black_num,1]*self.unit,
                                 (self.black_box[black_num,0]+1)*self.unit,
                                 (self.black_box[black_num,1]+1)*self.unit), fill='black',tags='blackC') for black_num in range(len(self.black_box))]          
    
    def run_window(self):
        self.window.mainloop()

def start_game(window_main):
    window_main.run_window()    
############################################      
if __name__ == '__main__':
    checkerboard = np.zeros((15,15),dtype=np.int16)
    window_main = Window()
    window_main.build_window()    
    start_game(window_main)