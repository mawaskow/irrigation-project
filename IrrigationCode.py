'''
Author: Ales Waskow
Date: 20 April 2020
Class: BE 205
Assignment: Drip-Sprinkler Irrigation Program

Description:
Calculates the necessary outputs for IrrigationProject.pyw
'''

# import statements
import tkinter
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import csv
import math

# function definitions

def getvars():
    '''
    qnot = input("Enter qnot: ")
    pnot = input("Enter pnot: ")
    sectlen = input("Enter sectlen: ")
    numlat = float(input("Enter numlat: "))
    orfk = input("Enter orfk: ")
    orfx = input("Enter orfx: ")
    diam = input("Enter diam: ")
    cval = input("Enter cval: ")
    '''
    qnot = 9500.0
    pnot = 207000.0
    sectlen = 10.0
    numlat = 13
    orfk = 0.95
    orfx = 0.55
    diam = 0.1
    cval = 130.0
    return qnot, pnot, sectlen, numlat, orfk, orfx, diam, cval

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
    while i > numlat:
        # determine pressdct
        if flowdct[i-1] > 0:
            pressdct[i] = pressdct[i-1] - hldct[i-1]
        else:
            pressdct[i] = 0
        # determine minidct
        if orfk*(pressdct[i])**orfx <= flowdct[i-1]:
            miniqdct[i] = orfk*pressdct[i]**orfx
        else:
            miniqdct[i] = flowdct[i-1]
        # determine flowdct
        flowdct[i] = flowdct[i-1] - miniqdct[i]
        # determine hldict
        hldct[i] = (1000.0)*(9.806)*((4*sectlen**(0.54)*flowdct[i])/(math.pi*3600000*0.85*cval*(diam**2)*((diam/4)**0.63)))**(1/0.54)
        i = i + 1
    print(pressdct)
    print(flowdct)
    print(miniqdct)
    print(hldct)

#==========================================================
def main():
    qnot, pnot, sectlen, numlat, orfk, orfx, diam, cval = getvars()
    construct_dcts(qnot, pnot, sectlen, numlat, orfk, orfx, diam, cval)



if __name__ == '__main__':
    main()
