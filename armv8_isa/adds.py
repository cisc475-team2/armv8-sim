"""
This module provides the R-format ADDS instruction
"""
from armv8_isa import R

def operation(proc, Rm, shamt, Rn, Rd):
    raw = proc.reg[Rn].get() + proc.reg[Rm].get()
    # set flags
    if (raw < 0):
        # set negative flag
        proc.flag_negative = True
        
    elif (raw == 0):
        # set 0 flag
        proc.flag_zero = True
        
    #elif (raw > proc.reg[Rd].data_max()):
        # set carry flag
        
    elif (raw > proc.reg[Rd].data_max()):
        # set overflow flag
        proc.flag_overflow = True
        
    result = int(raw % proc.reg[Rd].data_max())
    proc.reg[Rd].set(result)

ADDS = R(0x558, operation)