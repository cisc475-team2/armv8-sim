"""
This module provides the R-format ADDS instruction
"""
from armv8_isa import R

def operation(proc, Rm, shamt, Rn, Rd):
    raw = proc.reg[Rn].get() + proc.reg[Rm].get()
    # set flags
    #if (raw < 0):
        # set negative flag
        
    #else if (raw == 0):
        # set 0 flag
        
    #else if (raw > proc.reg[Rd].data_max()):
        # set carry flag
    #else if ():
        # set overflow flag
    result = int(raw % proc.reg[Rd].data_max())
    proc.reg[Rd].set(result)

ADDS = R(0x558, operation)