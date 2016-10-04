"""
This module provides a base class for all IW type ARMv8 instructions.
"""
from inspect import getargspec
from instruction import core


class iw_inst:
    """
    This class provides a base for an IW format instructions.
    """

    inst_format = "IW"
    opcode = 0b0

    operation = None