"""
This module provides the R-format UDIV instruction
"""
from armv8_isa import R

def operation(proc, Rm, shamt, Rn, Rd):
    if (proc.reg[Rm].get() != 0):
        raw = proc.reg[Rn].get() / proc.reg[Rm].get()
        #result = int(raw % proc.reg[Rd].data_min())
        result = int(raw % proc.reg[Rd].data_max())
        proc.reg[Rd].set(result)
    else:
        print("Cannot divide by 0!") #need to check what ARM does when dividing by 0
UDIV = R(0x4D6, operation)