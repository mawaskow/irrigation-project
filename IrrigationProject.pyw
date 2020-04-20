'''
Author: Ales Waskow
Date: 16 April 2020
Class: BE 205
Assignment: Drip-Sprinkler Irrigation Program

Description:
GUI program which generates a .txt output file
'''

# import statements
import tkinter
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import csv
from graphics import *

# function definitions

def getScsz(text):
    scsz=[]
    root = tkinter.Tk()
    scsz.append(root.winfo_screenwidth())
    scsz.append(root.winfo_screenheight())
    #root.destroy() ### generates error
    w = GraphWin(text, scsz[0], scsz[1])
    return w, scsz[0], scsz[1]

def beLogo(w, x, y):
    # "C:\\Users\\MAWaskow\\Documents\\School\\S20\\BE205\\GraphicsProjs\\BE.gif"
    beLogo = Image(Point(x/2, 60), "BE.gif")
    beLogo.draw(w)
    return

def instructions(w,x,y):
    line1 =Text(Point(x/2,200), "This program uses default input values and draws the irrigation system based on the Default Values.").draw(w)
    line2 =Text(Point(x/2, 200+30), "The User can change the default values to new values and click a box to redraw the Irrigation ststem for the new entries.").draw(w)
    line3 = Text(Point(x/2, 200+60), "The Number of Laterals can be any number.").draw(w)
    sizeT = 12
    line1.setSize(sizeT), line2.setSize(sizeT), line3.setSize(sizeT)
    return line1, line2, line3

def okBox(w,x,y, msg, txtcolor, boxcolor):
    rw, rh = x/2, 60
    x1 = x/2 - rw/2
    y1 = y/1.2 - rh/2
    x2, y2 = x/2 + rw/2, y/1.2 + rh/2
    # need to move rectangle to center of window
    btmR = Rectangle(Point(x1, y1), Point(x2,y2)).draw(w)
    btmR.setFill(boxcolor)
    clickMouse = Text(Point(x/2, y/1.2), msg).draw(w)
    clickMouse.setFace("arial"), clickMouse.setSize(14), clickMouse.setStyle("bold")
    clickMouse.setTextColor(txtcolor)
    while True:
        p = w.getMouse()
        if p.getX() >= x1 and p.getX() <= x2:
            if p.getY() >= y1 and p.getY() <= y2:
                break
    clickMouse.undraw()
    btmR.undraw()
    return

#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    w, x, y = getScsz("Drip/Sprinkler Irrigation System by Dr. Tamimi")
    beLogo(w,x,y)
    line1, line2, line3, line4, line5, line6, line7, line8, line9 = instructions(w,x,y)
    okBox(w,x,y, "Please Click Here to Continue", "dark blue", "pink")
    line1.undraw(), line2.undraw(), line3.undraw(), line4.undraw(), line5.undraw(), line6.undraw(), line7.undraw(), line8.undraw(), line9.undraw()


if __name__ == '__main__':
    main()
