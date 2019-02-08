# Thuy Le - MHI 289I - Homework 1 - Part 1

# variables
PV = 5000
ra = 6.5
r = 0.065/12
n = 12

# table headers
print("Payment schedule for a loan of $%2d at %.1f" % (PV, ra) + "% interest, repaid over", int(n), "year:")
print("month", "payment", "remaining")

for m in range(1,13,1): # generates sequence of numbers for each of the 12 months
    P = r*PV/(1-(1+r)**(-n)) # P is payment per month needed to pay off loan in 1 year
    RP = ((PV)*(1-((1+r)**(m-n))))/(1-((1+r)**(-n))) # RP is reamaining principal
    print(" %3d %7.2f %9.2f" % (m, P, RP)) # print statement for all 3 components