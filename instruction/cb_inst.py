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
    op_args = ["proc","COND_BR_address","Rt"]
        
    
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


    def execute(self, proc, COND_BR_address, Rt):
        if not isinstance(proc, core):
            raise TypeError("proc must be an ARMv8Core")
        if type(COND_BR_address) is not int:
            raise TypeError("COND_BR_address must be of type int")
        if type(Rt) is not int:
            raise TypeError("Rt must be of type int")
        if self.operation is not None:
            self.operation(proc, COND_BR_address, Rt)

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