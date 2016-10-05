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
    op_args = ["proc", "BR_address"]
    
    
    def __eq__(self, other):
        if self.inst_format != other.inst_format:
            return False
        elif self.opcode != other.opcode:
            return False
        elif self.operation != other.operation:
            return False
        elif self.op_args != other.op_args:
            return False
        else:
            return True


    def execute(self, proc, BR_address):
        if not isinstance(proc, core):
            raise TypeError("proc must be an ARMv8Core")
        if type(BR_address) is not int:
            raise TypeError("BR_address must be of type int")
        if BR_address < 0 or BR_address > pow(2, 26):
            raise ValueError("BR_address value out of range for 26 bits")
        if self.operation is not None:
            self.operation(proc, BR_address)

    def __init__(self, opcode, operation):
        if type(opcode) is not int:
            raise TypeError("opcode must be of type int")
        args = getargspec(operation).args
        if len(args) > len(self.op_args) or args != self.op_args:
            err_str = ("operation must be a function " +
                       "accepting {} ".format(len(self.op_args)) +
                       "arguments: {}".format(self.op_args))
            raise TypeError(err_str)
        self.opcode = opcode
        self.operation = operation
