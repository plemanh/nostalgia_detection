# -*- coding: utf-8 -*-
from Tkinter import *
from tkFileDialog   import *       
import pickle
import csv

class Interface(Frame):
        
    def __init__(self, frame, **kwargs):
        Frame.__init__(self, frame, width=500, height=500, **kwargs)
        self.pack(fill=BOTH)
        self.pack_propagate(False)

if __name__ == '__main__' :
    
    frame = Tk()
    interface = Interface(frame)
    interface.mainloop()