"""
This module provides the I-format ORRI instruction
"""
from armv8_isa import I

def operation(proc, ALU_immediate, Rn, Rd):
    raw = proc.reg[Rn].get() | ALU_immediate
    result = int(raw % proc.reg[Rd].data_max())
    proc.reg[Rd].set(result)

ORRI = I(0x590, operation)
#or 0x591