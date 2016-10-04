"""
This module provides a base class for all D type ARMv8 instructions.
"""
from inspect import getargspec
from instruction import core


class d_inst:
    """
    This class provides a base for all D instructions.
    """

    inst_format = 'D'
    name = ""
    opcode = 0b0

    operation = None

    def execute(DT_address, op, Rn, Rt):
        if operation:
            operation(DT_address, op, Rn, Rt)

    def __init__(self, name, opcode, operation):
        if type(name) not str:
            raise TypeError("name must be of type str")
        if type(opcode) not int:
            raise TypeError("opcode must be of type int")
        args = getargspec(operation).args
        a = set(args)
        b = set(["DT_address", "op", "Rn", "Rt"])
        if len(args) != 4 or a == b:
            raise TypeError("operation must be a function accepting 4 " +
                            "arguments: DT_address, op, Rn, Rt")
        self.name = name
        self.opcode = opcode
        self.operation = operation
