"""
This module provides the I-format ANDI instruction
"""
from armv8_isa import I

def operation(proc, ALU_immediate, Rn, Rd):
    raw = proc.reg[Rn].get() & ALU_immediate
    result = int(raw % proc.reg[Rd].data_max())
    proc.reg[Rd].set(result)

ANDI = I(0x490, operation)
#or 491