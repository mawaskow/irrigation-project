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

def paramprompt_text(w, x, y):
    # make the text
    qnot = Text(Point(x/10,y/20), "Qo (Litres/Hr)").draw(w)
    po = Text(Point(x/10,(y/20)+20), "Po (Pa)").draw(w)
    sectlen = Text(Point(x/10,(y/20)+40), "Section Length (m)").draw(w)
    numlaterals = Text(Point(x/10,(y/20)+60), "Number of Laterals").draw(w)
    orfkval = Text(Point(x/10,(y/20)+80), "Orifice k Value").draw(w)
    orfxval = Text(Point(x/10,(y/20)+100), "Orifice x Value").draw(w)
    maindiam = Text(Point(x/10,(y/20)+120), "Main Pipe Diameter (m)").draw(w)
    cval = Text(Point(x/10,(y/20)+140), "C Value").draw(w)
    qnot.setSize(12), po.setSize(12), sectlen.setSize(12), numlaterals.setSize(12), orfkval.setSize(12), orfxval.setSize(12), maindiam.setSize(12), cval.setSize(12)
    return qnot, po, sectlen, numlaterals, orfkval, orfxval, maindiam, cval

def paramprompt_boxes(w, x, y):
    # make the entry boxes
    qnot_in = Entry(Point((x/4.5),y/20), int(x/100)).draw(w)
    po_in = Entry(Point(x/4.5,(y/20)+20), int(x/100)).draw(w)
    sectlen_in = Entry(Point(x/4.5,(y/20)+40), int(x/100)).draw(w)
    numlaterals_in = Entry(Point(x/4.5,(y/20)+60), int(x/100)).draw(w)
    orfkval_in = Entry(Point(x/4.5,(y/20)+80), int(x/100)).draw(w)
    orfxval_in = Entry(Point(x/4.5,(y/20)+100), int(x/100)).draw(w)
    maindiam_in = Entry(Point(x/4.5,(y/20)+120), int(x/100)).draw(w)
    cval_in = Entry(Point(x/4.5,(y/20)+140), int(x/100)).draw(w)
    qnot_in.setFill('white'), po_in.setFill('white'), sectlen_in.setFill('white'), numlaterals_in.setFill('white'), orfkval_in.setFill('white'), orfxval_in.setFill('white'), maindiam_in.setFill('white'), cval_in.setFill('white')
    qnot_in.setText("9600.0"), po_in.setText("207000.0"), sectlen_in.setText("10.0"), numlaterals_in.setText("13"), orfkval_in.setText("0.95"), orfxval_in.setText("0.55"), maindiam_in.setText("0.1"), cval_in.setText("130.0")
    return qnot_in, po_in, sectlen_in, numlaterals_in, orfkval_in, orfxval_in, maindiam_in, cval_in

def paramprompts(qnot_in, po_in, sectlen_in, numlaterals_in, orfkval_in, orfxval_in, maindiam_in, cval_in):
    # get the final texts
    qnot_val = qnot_in.getText()
    po_val = po_in.getText()
    sectlen_val = sectlen_in.getText()
    numlaterals_val = numlaterals_in.getText()
    orfkval_val = orfkval_in.getText()
    orfxval_val = orfxval_in.getText()
    maindiam_val = maindiam_in.getText()
    cval_val = cval_in.getText()
    return qnot_val, po_val, sectlen_val, numlaterals_val, orfkval_val, orfxval_val, maindiam_val, cval_val

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
    '''
    Write a description of what happens when you run
    this file here.
    '''
    # display 1
    w, x, y = getScsz("Drip/Sprinkler Irrigation System by Dr. Tamimi")
    logo = beLogo(w,x,y)
    line1, line2, line3 = instructions(w,x,y)
    okBox(w,x,y, "Please Click Here to Continue...", "white", "black")
    line1.undraw(), line2.undraw(), line3.undraw()
    logo.undraw()
    # display 2
    table1 = table(w,x,y)
    qnot_txt, pnot_txt, sectlen_txt, numlat_txt, orfk_txt, orfx_txt, diam_txt, cval_txt = paramprompt_text(w,x,y)
    qnot_box, pnot_box, sectlen_box, numlat_box, orfk_box, orfx_box, diam_box, cval_box = paramprompt_boxes(w,x,y)
    qnot, pnot, sectlen, numlat, orfk, orfx, diam, cval = paramprompts(qnot_box, pnot_box, sectlen_box, numlat_box, orfk_box, orfx_box, diam_box, cval_box)
    okBox(w,x,y, "Please Change Default Values as Needed and Click Here to Draw the Irrigation Sysytem", "black", "light blue")
    qnot_txt.undraw(), pnot_txt.undraw(), sectlen_txt.undraw(), numlat_txt.undraw(), orfk_txt.undraw(), orfx_txt.undraw(), diam_txt.undraw(), cval_txt.undraw()
    qnot_box.undraw(), pnot_box.undraw(), sectlen_box.undraw(), numlat_box.undraw(), orfk_box.undraw(), orfx_box.undraw(), diam_box.undraw(), cval_box.undraw()
    table1.undraw()
    # display 3
    paramdisplay(w,x,y,qnot, pnot, sectlen, numlat, orfk, orfx, diam, cval)
    okBox(w,x,y, "Please Change Default Values as Needed and Click Here to Draw the Irrigation Sysytem", "black", "light blue")


if __name__ == '__main__':
    main()
