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
import math

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
    qnot_in.setText("9500.0"), pnot_in.setText("207000.0"), sectlen_in.setText("10.0"), numlat_in.setText("13"), orfk_in.setText("0.95"), orfx_in.setText("0.55"), diam_in.setText("0.1"), cval_in.setText("130.0")
    return qnot_in, pnot_in, sectlen_in, numlat_in, orfk_in, orfx_in, diam_in, cval_in

def parachange(qnot_in, pnot_in, sectlen_in, numlat_in, orfk_in, orfx_in, diam_in, cval_in):
    # determine final values
    qnot_val = qnot_in.getText()
    pnot_val = pnot_in.getText()
    sectlen_val = sectlen_in.getText()
    numlat_val = numlat_in.getText()
    orfk_val = orfk_in.getText()
    orfx_val = orfx_in.getText()
    diam_val = diam_in.getText()
    cval_val = cval_in.getText()
    # initialize dictionary
    irridict = {}
    irridict["qnot"] = float(qnot_val)
    irridict["pnot"] = float(pnot_val)
    irridict["sectlen"] = float(sectlen_val)
    irridict["numlat"] = float(numlat_val)
    irridict["orfk"] = float(orfk_val)
    irridict["orfx"] = float(orfx_val)
    irridict["diam"] = float(diam_val)
    irridict["cval"] = float(cval_val)
    return irridict

def construct_dcts(qnot, pnot, sectlen, numlat, orfk, orfx, diam, cval):
    # make dictionaries for pressure, flowrate, miniq, and hl
    pressdct = {}
    flowdct = {}
    miniqdct = {}
    hldct = {}
    # initialize known values
    pressdct[0] = pnot
    flowdct[0] = qnot
    miniqdct[0] = 0.0
    hldct[0] = (1000.0)*(9.806)*((4*sectlen**(0.54)*qnot)/(math.pi*3600000*0.85*cval*(diam**2)*((diam/4)**0.63)))**(1/0.54)
    # begin calculations
    i = 1
    while i <= numlat:
        # determine pressdct
        if flowdct[i-1] > 0:
            pressdct[i] = pressdct[i-1] - hldct[i-1]
        else:
            pressdct[i] = 0
        pressdct[i] = round(pressdct[i], 2)
        # determine minidct
        if orfk*(pressdct[i])**orfx <= flowdct[i-1]:
            miniqdct[i] = orfk*pressdct[i]**orfx
        else:
            miniqdct[i] = flowdct[i-1]
        miniqdct[i] = round(miniqdct[i], 5)
        # determine flowdct
        flowdct[i] = flowdct[i-1] - miniqdct[i]
        flowdct[i] = round(flowdct[i], 5)
        # determine hldict
        hldct[i] = (1000.0)*(9.806)*((4*sectlen**(0.54)*flowdct[i])/(math.pi*3600000*0.85*cval*(diam**2)*((diam/4)**0.63)))**(1/0.54)
        i = i + 1
    return pressdct, flowdct, miniqdct, hldct

def pipelines(w, x, y, irrigationdictionary):
    n = int(irrigationdictionary["numlat"])
    div = x/(n+3)
    mainpipetop = Line(Point(div, y*2/3), Point((n+1)*div, y*2/3)).draw(w)
    mainpipebottom = Line(Point(div, (y*2/3)+20), Point((n+1)*div, (y*2/3)+20)).draw(w)
    mainpipeend = Line(Point((n+1)*div, y*2/3), Point((n+1)*div, (y*2/3)+20)).draw(w)
    for i in range(n+1):
        Text(Point((i+1)*div, (y*2/3)-10), i).draw(w)
    for i in range(n):
        Line(Point((i+2)*div, (y*2/3)+20), Point((i+2)*div, y*19/20)).draw(w)
        Line(Point((i+2)*div-5, (y*2/3)+20), Point((i+2)*div-5, y*19/20)).draw(w)

def reportfile(irrigationdictionary, pressuredictionary, flowdictionary, miniqdictionary):
    outfile= open(asksaveasfilename(), "w")
    n = int(irrigationdictionary["numlat"])
    print(("Node n").ljust(15), ("Flow Rate, Q").ljust(20), ("Pressure, P").ljust(20), ("Lateral Flow Rate, q").ljust(20), file = outfile)
    print("="*80, file = outfile)
    for i in range(n+1):
        print(str(i).rjust(5), " "*10, str(flowdictionary[i]).rjust(10), " "*10, str(pressuredictionary[i]).rjust(10), " "*10, str(miniqdictionary[i]).rjust(10), file = outfile)
    outfile.close()

#==========================================================
def main():
    #####Display 1#####
    w, x, y = getScsz("Drip/Sprinkler Irrigation System by Dr. Tamimi")
    logo = beLogo(w,x,y)
    line1, line2, line3 = instructions(w,x,y)
    okBox(w,x,y, "Please Click Here to Continue...", "white", "black")
    line1.undraw(), line2.undraw(), line3.undraw()
    logo.undraw()
    #####Display 2#####
    table1 = table(w,x,y)
    # get returns from parameters prompt
    qnot_in, pnot_in, sectlen_in, numlat_in, orfk_in, orfx_in, diam_in, cval_in = paramprompt(w, x, y)
    okBox(w,x,y, "Please Change Default Values as Needed and Click Here to Draw the Irrigation Sysytem", "black", "light blue")
    # get dictionary from the altered parameter entries
    irridict = parachange(qnot_in, pnot_in, sectlen_in, numlat_in, orfk_in, orfx_in, diam_in, cval_in)
    # initialize, calculate, and construct dictionaries from the parameters
    pressdct, flowdct, miniqdct, hldct = construct_dcts(irridict["qnot"], irridict["pnot"], irridict["sectlen"], irridict["numlat"], irridict["orfk"], irridict["orfx"], irridict["diam"], irridict["cval"])
    table1.undraw()
    #####Display 3#####
    # draw the pipelines
    pipelines(w,x,y, irridict)
    okBox(w,x,y, "Click Here to Calculate Flow Rates into Each Lateral/Sprinkler", "black", "yellow")
    #####Display 4#####
    okBox(w,x,y, "Analysis Complete. Click to Write Results/Table to Output File", "yellow", "dark blue")
    #####Display 5#####
    reportfile(irridict, pressdct, flowdct, miniqdct)
    okBox(w,x,y, "Results are Saved. Click Here to EXIT Program", "black", "yellow")
    w.close()

if __name__ == '__main__':
    main()
