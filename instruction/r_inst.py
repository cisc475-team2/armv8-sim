"""
This module provides a base class for all R type ARMv8 instructions.
"""
from inspect import getargspec
from instruction import core


class r_inst:
    """
    This class provides a base for a R format instructions.
    """

    inst_format = 'R'
    opcode = 0b0

    operation = None