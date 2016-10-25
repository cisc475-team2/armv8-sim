"""
This package provides the ARMv8 ISA
"""
# Import instruction classes
from instruction import R, I, D, B, CB, IW

# Import instructions from modules below
from add import ADD
from sub import SUB
from addi import ADDI
from subi import SUBI
from udiv import UDIV