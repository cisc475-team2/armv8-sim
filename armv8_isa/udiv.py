"""
This module provides the R-format UDIV instruction
"""
from armv8_isa import R

def operation(proc, Rm, shamt, Rn, Rd):
    raw = proc.reg[Rn].get() / proc.reg[Rm].get()
    result = int(raw % proc.reg[Rd].data_min())
    proc.reg[Rd].set(result)
    # need to error check when dividing by 0, look up what happens if ARM tries to divide by 0

UDIV = R(0x4D6, operation)