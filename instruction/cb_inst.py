"""
This module provides a base class for all CB type ARMv8 instructions.
"""
from inspect import getargspec
from instruction import core


class cb_inst:
    """
    This class provides a base for a CB format instructions.
    """

    inst_format = "CB"
    opcode = 0b0

    operation = None