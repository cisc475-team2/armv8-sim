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
from mul import MUL
from umulh import UMULH
from sdiv import SDIV
from andr import AND
from andi import ANDI
from eor import EOR
from eori import EORI
from lsl import LSL
from lsr import LSR
from orr import ORR
from orri import ORRI