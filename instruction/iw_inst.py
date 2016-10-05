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
    op_args = ["proc","MOV_immediate","Rd"]
            

    def execute(self, proc, MOV_immediate, Rd):
        if not isinstance(proc, core):
            raise TypeError("proc must be an ARMv8Core")
        if type(MOV_immediate) is not int:
            raise TypeError("MOV_immediate must be of type int")
        if type(Rd) is not int:
            raise TypeError("Rd must be of type int")
        if self.operation is not None:
            self.operation(proc, MOV_immediate, Rd)


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