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
    op_args = ["proc","T_address","op","Rn","Rt"]

    def execute(self, proc, T_address, op, Rn, Rt):
        if not isinstance(proc, core):
            raise TypeError("proc must be an ARMv8Core")
        if type(T_address) is not int:
            raise TypeError("T_address must be of type int")
        if type(op) is not int:
            raise TypeError("op must be of type int")
        if type(Rn) is not int:
            raise TypeError("Rn must be of type int")
        if type(Rt) is not int:
            raise TypeError("Rt must be of type int")
        if self.operation is not None:
            self.operation(proc, T_address, op, Rn, Rt)

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
