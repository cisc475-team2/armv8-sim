"""
This module provides the R-format SUB instruction
"""
from armv8_isa import R

def operation(proc, Rm, shamt, Rn, Rd):
    raw = proc.reg[Rn].get() - proc.reg[Rm].get()
    if raw < proc.reg[Rd].data_min():
        result = 0
    else result = raw
    proc.reg[Rd].set(result)

SUB = R(0x658, operation)