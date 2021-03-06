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
    op_args = ["proc","Rm","shamt","Rn","Rd"]
    
    
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


    def execute(self, proc, Rm, shamt, Rn, Rd):
        if not isinstance(proc, core):
            raise TypeError("proc must be an ARMv8Core")
        if type(Rm) is not str:
            raise TypeError("Rm must be of type str")
        if type(shamt) is not int:
            raise TypeError("shamt must be of type int")
        if type(Rn) is not str:
            raise TypeError("Rn must be of type str")
        if type(Rd) is not str:
            raise TypeError("Rd must be of type str")
        if self.operation is not None:
            self.operation(proc, Rm, shamt, Rn, Rd)


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