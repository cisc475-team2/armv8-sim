"""
This module provides the R-format LSL instruction
"""
from armv8_isa import R

def operation(proc, Rm, shamt, Rn, Rd):
    raw = proc.reg[Rn].get() << proc.reg[Rm].get()
    #raw = proc.reg[Rn].get() * 2**proc.reg[Rm].get()
    result = int(raw % proc.reg[Rd].data_max())
    proc.reg[Rd].set(result)

LSL = R(0x69B, operation)
# x << y is same as multiplying x by 2**y