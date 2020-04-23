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
    numlat = 18
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
    while i <= numlat:
        # determine pressdct
        if flowdct[i-1] > 0:
            pressdct[i] = pressdct[i-1] - hldct[i-1]
        else:
            pressdct[i] = 0
        #pressdct[i] = round(pressdct[i], 2)
        # determine minidct
        if orfk*(pressdct[i])**orfx <= flowdct[i-1]:
            miniqdct[i] = orfk*pressdct[i]**orfx
        else:
            miniqdct[i] = flowdct[i-1]
        #miniqdct[i] = round(miniqdct[i], 5)
        # determine flowdct
        flowdct[i] = flowdct[i-1] - miniqdct[i]
        #flowdct[i] = round(flowdct[i], 5)
        # determine hldict
        hldct[i] = (1000.0)*(9.806)*((4*sectlen**(0.54)*flowdct[i])/(math.pi*3600000*0.85*cval*(diam**2)*((diam/4)**0.63)))**(1/0.54)
        #hldct[i] = hldct[i]
        i = i + 1
    return pressdct, flowdct, miniqdct, hldct

def enddisplay(numlat, pressuredictionary, flowdictionary, miniqdictionary):
    n = numlat
    print(("Node n").ljust(15), ("Flow Rate, Q").ljust(20), ("Pressure, P").ljust(20), ("Lateral Flow Rate, q").ljust(20))
    print("="*80)
    # truncate lists for n >= 12
    if n >= 12:
        pressuredictionary[12] = pressuredictionary[13]
        miniqdictionary[12] = miniqdictionary[13]
    for i in range(n+1):
        flow = flowdictionary[i]
        press = float(pressuredictionary[i])
        miniq = miniqdictionary[i]
        flow = str(round(flow, 4))
        press = str(round(press, 2))
        miniq = str(round(miniq, 5))
        print(str(i).rjust(5), " "*10, flow.rjust(10), " "*10, press.rjust(10), " "*10, miniq.rjust(10))

#==========================================================
def main():
    qnot, pnot, sectlen, numlat, orfk, orfx, diam, cval = getvars()
    pressdct, flowdct, miniqdct, hldct = construct_dcts(qnot, pnot, sectlen, numlat, orfk, orfx, diam, cval)
    enddisplay(numlat, pressdct, flowdct, miniqdct)


if __name__ == '__main__':
    main()
