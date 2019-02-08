# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 02:21:39 2019

@author: tweeb
"""
# Thuy Le - MHI 289I - Homework 1 - Part 2

# interest rate conversion
ra = float(input("What is the annual interest rate (enter it without the % sign)? "))
r = (ra/100)/12

# principle value borrowed
PV = float(input("How much is being borrowed (no commas)? "))

# number of months per years
na = int(input("How many years is the loan for? "))
n = na*12

# print statement for headers 
print("Payment schedule for a loan of $%2d at %.1f" % (PV, ra) + "% interest, repaid over", int(na), "year:")
print("month", "payment", "remaining")

for m in range(1,13,1): # generates sequence of numbers for each of the 12 months
    P = r*PV/(1-(1+r)**(-n)) # P is payment per month needed to pay off loan in 1 year
    RP = ((PV)*(1-((1+r)**(m-n))))/(1-((1+r)**(-n))) # RP is reamaining principal
    print(" %3d %7.2f %9.2f" % (m, P, RP)) # print statement for all 3 components