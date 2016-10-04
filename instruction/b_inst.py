"""
This module provides a base class for all B type ARMv8 instructions.
"""
from inspect import getargspec
from instruction import core


class b_inst:
    """
    This class provides a base for a B format instructions.
    """

    inst_format = 'B'
    opcode = 0b0

    operation = None

    def execute(BR_address):
        if type(BR_address) not int:
            raise TypeError("BR_address must be of type int")
        else if BR_address < 0 or BR_address > pow(2, 26):
            raise ValueError("BR_address value out of range for 26 bits")
        if operation:
            operation(BR_address)

    def __init__(self, opcode, operation):
        if type(opcode) not int:
            raise TypeError("opcode must be of type int")
        args = getargspec(operation).args
        if len(args) > 1 or args[0] != "BR_address":
            raise TypeError("operation must be a function accepting 1 " +
                            "argument: BR_address")
        self.opcode = opcode
        self.operation = operation
