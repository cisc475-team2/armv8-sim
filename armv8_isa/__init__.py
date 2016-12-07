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
from adds import ADDS
from addis import ADDIS
from subs import SUBS
from subis import SUBIS

instset = {
    "ADD": ADD,
    "SUB": SUB,
    "ADDI": ADDI,
    "SUBI": SUBI,
    "UDIV": UDIV,
    "MUL": MUL,
    "UMULH": UMULH,
    "SDIV": SDIV,
    "AND": AND,
    "ANDI": ANDI,
    "EOR": EOR,
    "EORI": EORI,
    "LSL": LSL,
    "LSR": LSR,
    "ORR": ORR,
    "ORRI": ORRI,
    "ADDS": ADDS,
    "ADDIS": ADDIS,
    "SUBS": SUBS,
    "SUBIS": SUBIS
}