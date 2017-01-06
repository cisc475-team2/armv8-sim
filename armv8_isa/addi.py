"""
This module provides the I-format ADDI instruction
"""
from armv8_isa import I

def operation(proc, ALU_immediate, Rn, Rd):
    raw = proc.reg[Rn].get() + ALU_immediate
    result = int(raw % proc.reg[Rd].data_max())
    proc.reg[Rd].set(result)

ADDI = I(0x488, operation)