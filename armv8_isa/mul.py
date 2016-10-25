"""
This module provides the R-format MUL instruction
"""
from armv8_isa import R

def operation(proc, Rm, shamt, Rn, Rd):
    raw = proc.reg[Rn].get() * proc.reg[Rm].get()
    result = int(raw % proc.reg[Rd].data_max())
    proc.reg[Rd].set(result)

MUL = R(0x4D8, operation)