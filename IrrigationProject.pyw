'''
Author: Ales Waskow
Date: 16 April 2020
Class: BE 205
Assignment: Drip-Sprinkler Irrigation Program

Description:
GUI program which takes values of an irrigation system, 
draws the system, then generates a report which is sent 
to a .txt output file.
'''

# import statements
import ctypes
import tkinter
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import csv
from graphics import *
from math import *

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
    return beLogo

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
    y1 = y/2.5 - rh/2
    x2, y2 = x/2 + rw/2, y/2.5 + rh/2
    # need to move rectangle to center of window
    btmR = Rectangle(Point(x1, y1), Point(x2,y2)).draw(w)
    btmR.setFill(boxcolor)
    clickMouse = Text(Point(x/2, y/2.5), msg).draw(w)
    clickMouse.setFace("arial"), clickMouse.setSize(13), clickMouse.setStyle("bold")
    clickMouse.setTextColor(txtcolor)
    while True:
        p = w.getMouse()
        if p.getX() >= x1 and p.getX() <= x2:
            if p.getY() >= y1 and p.getY() <= y2:
                break
    clickMouse.undraw()
    btmR.undraw()
    return

def table(w, x, y):
    table1 = Image(Point(x/2, y/1.5), "Table1.gif")
    table1.draw(w)
    return table1

def paramprompt(w, x, y):
    # make the text
    qnot = Text(Point(x/10,y/20), "Qo (Litres/Hr)").draw(w)
    pnot = Text(Point(x/10,(y/20)+20), "Po (Pa)").draw(w)
    sectlen = Text(Point(x/10,(y/20)+40), "Section Length (m)").draw(w)
    numlat = Text(Point(x/10,(y/20)+60), "Number of Laterals").draw(w)
    orfk = Text(Point(x/10,(y/20)+80), "Orifice k Value").draw(w)
    orfx = Text(Point(x/10,(y/20)+100), "Orifice x Value").draw(w)
    diam = Text(Point(x/10,(y/20)+120), "Main Pipe Diameter (m)").draw(w)
    cval = Text(Point(x/10,(y/20)+140), "C Value").draw(w)
    qnot.setSize(12), pnot.setSize(12), sectlen.setSize(12), numlat.setSize(12), orfk.setSize(12), orfx.setSize(12), diam.setSize(12), cval.setSize(12)
    # make the entry boxes
    qnot_in = Entry(Point((x/4.5),y/20), int(x/100)).draw(w)
    pnot_in = Entry(Point(x/4.5,(y/20)+20), int(x/100)).draw(w)
    sectlen_in = Entry(Point(x/4.5,(y/20)+40), int(x/100)).draw(w)
    numlat_in = Entry(Point(x/4.5,(y/20)+60), int(x/100)).draw(w)
    orfk_in = Entry(Point(x/4.5,(y/20)+80), int(x/100)).draw(w)
    orfx_in = Entry(Point(x/4.5,(y/20)+100), int(x/100)).draw(w)
    diam_in = Entry(Point(x/4.5,(y/20)+120), int(x/100)).draw(w)
    cval_in = Entry(Point(x/4.5,(y/20)+140), int(x/100)).draw(w)
    qnot_in.setFill('white'), pnot_in.setFill('white'), sectlen_in.setFill('white'), numlat_in.setFill('white'), orfk_in.setFill('white'), orfx_in.setFill('white'), diam_in.setFill('white'), cval_in.setFill('white')
    qnot_in.setText("9600.0"), pnot_in.setText("207000.0"), sectlen_in.setText("10.0"), numlat_in.setText("13"), orfk_in.setText("0.95"), orfx_in.setText("0.55"), diam_in.setText("0.1"), cval_in.setText("130.0")
    # determine final values
    qnot_val = qnot_in.getText()
    pnot_val = pnot_in.getText()
    sectlen_val = sectlen_in.getText()
    numlat_val = numlat_in.getText()
    orfk_val = orfk_in.getText()
    orfx_val = orfx_in.getText()
    diam_val = diam_in.getText()
    cval_val = cval_in.getText()

def paramdisplay(w, x, y, qnot, pnot, sectlen, numlat, orfk, orfx, diam, cval):
    qnot = Text(Point(x/10,y/20), "qnot: " + qnot).draw(w)
    po = Text(Point(x/10,(y/20)+20), "Po (Pa): "+ pnot).draw(w)
    sectlen = Text(Point(x/10,(y/20)+40), "Section Length (m): " + sectlen).draw(w)
    numlaterals = Text(Point(x/10,(y/20)+60), "Number of Laterals: " + numlat).draw(w)
    orfkval = Text(Point(x/10,(y/20)+80), "Orifice k Value: " + orfk).draw(w)
    orfxval = Text(Point(x/10,(y/20)+100), "Orifice x Value: " + orfx).draw(w)
    maindiam = Text(Point(x/10,(y/20)+120), "Main Pipe Diameter (m): " + diam).draw(w)
    cval = Text(Point(x/10,(y/20)+140), "C Value: " + cval).draw(w)
#==========================================================
def main():
    # display 1
    w, x, y = getScsz("Drip/Sprinkler Irrigation System by Dr. Tamimi")
    logo = beLogo(w,x,y)
    line1, line2, line3 = instructions(w,x,y)
    okBox(w,x,y, "Please Click Here to Continue...", "white", "black")
    line1.undraw(), line2.undraw(), line3.undraw()
    logo.undraw()
    # display 2
    table1 = table(w,x,y)
    paramprompt(w, x, y)
    okBox(w,x,y, "Please Change Default Values as Needed and Click Here to Draw the Irrigation Sysytem", "black", "light blue")
    table1.undraw()
    # display 3
    okBox(w,x,y, "Click Here to Calculate Flow Rates into Each Lateral/Sprinkler", "black", "yellow")
    # display 4
    okBox(w,x,y, "Analysis Complete. Click to Write Results/Table to Output File", "yellow", "dark blue")
    # display 5
    okBox(w,x,y, "Results are Saved. Click Here to EXIT Program", "black", "yellow")
    w.close()

if __name__ == '__main__':
    main()
