"""
This module provides a base class for all I type ARMv8 instructions.
"""
from inspect import getargspec
from instruction import core


class i_inst:
    """
    This class provides a base for a I format instructions.
    """

    inst_format = 'I'
    opcode = 0b0

    operation = None