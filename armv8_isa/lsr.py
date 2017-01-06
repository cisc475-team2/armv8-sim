"""
This module provides the R-format LSR instruction
"""
from armv8_isa import R

def operation(proc, Rm, shamt, Rn, Rd):
    raw = proc.reg[Rn].get() >> proc.reg[Rm].get()
    result = int(raw % proc.reg[Rd].data_max())
    proc.reg[Rd].set(result)

LSR = R(0x69A, operation)
# x >> y is same as dividing x by 2**y