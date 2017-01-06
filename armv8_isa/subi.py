"""
This module provides the I-format SUBI instruction
"""
from armv8_isa import I

def operation(proc, ALU_immediate, Rn, Rd):
    raw = proc.reg[Rn].get() - ALU_immediate
    if raw < proc.reg[Rd].data_min():
        result = 0
    else:
        result = raw
    proc.reg[Rd].set(result)

SUBI = I(0x688, operation)