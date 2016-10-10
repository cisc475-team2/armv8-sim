"""
This module provides a class representing an ARMv8 processor core.
"""


class ARMv8Core:
    """
    This class provides a basic representation of an ARMv8 processor.
    Registers and flags are handled here.
    """


    class Register:
        """
        This class provides a representation of an ARMv8 processor register.
        """

        number = 0
        reserved = False
        static = False
        data = 0b0
        
        
        def __eq__(self, other):
            if self.number != other.number:
                return False
            elif self.reserved != other.reserved:
                return False
            elif self.static != other.static:
                return False
            elif self.data != other.data:
                return False
            else:
                return True


        def __init__(self, number, reserved, static):
            if type(number) is not int:
                raise TypeError("Register number must be of type int")
            if type(reserved) is not bool:
                raise TypeError("Register reserved must be of type bool")
            if type(static) is not bool:
                raise TypeError("Register static must be of type bool")
            self.number = number
            self.reserved = reserved
            self.static = static
        
        
        def data_max(self):
            return 18446744073709551615
        
        
        def data_min(self):
            return 0
        
        
        def set(self, data):
            if type(data) is not int:
                raise TypeError("Register data must be of type int")
            if data < self.data_min():
                ves = ("Value of data out of range: " +
                       "{} < {}".format(data,self.data_min()))
                raise ValueError(ves)
            if data > self.data_max():
                ves = ("Value of data out of range: " +
                       "{} > {}".format(data,self.data_max()))
                raise ValueError(ves)
            if not self.static:
                self.data = data
        
        
        def get(self, binary=False, hexa=False):
            if type(binary) is not bool:
                raise TypeError("Value of binary must be of type bool")
            if binary:
                return "{0:b}".format(self.data)
            elif hexa:
                return hex(self.data)
            else:
                return self.data
    
    
    reg = {
        "X0": Register(0, False, False),
        "X1": Register(1, False, False),
        "X2": Register(2, False, False),
        "X3": Register(3, False, False),
        "X4": Register(4, False, False),
        "X5": Register(5, False, False),
        "X6": Register(6, False, False),
        "X7": Register(7, False, False),
        "X8": Register(8, False, False),
        "X9": Register(9, False, False),
        "X10": Register(10, False, False),
        "X11": Register(11, False, False),
        "X12": Register(12, False, False),
        "X13": Register(13, False, False),
        "X14": Register(14, False, False),
        "X15": Register(15, False, False),
        "X16": Register(16, False, False),
        "X17": Register(17, False, False),
        "X18": Register(18, False, False),
        "X19": Register(19, False, False),
        "X20": Register(20, False, False),
        "X21": Register(21, False, False),
        "X22": Register(22, False, False),
        "X23": Register(23, False, False),
        "X24": Register(24, False, False),
        "X25": Register(25, False, False),
        "X26": Register(26, False, False),
        "X27": Register(27, False, False),
        "X28": Register(28, False, False),
        "X29": Register(29, False, False),
        "X30": Register(30, False, False),
        "XZR": Register(31, True, True)
    }
    
    
    flag_negative = False
    flag_zero = False
    flag_overflow = False
    flag_carry = False


    def __init__(self):
        self.reg.update({"IP0": self.reg["X16"], "IP1": self.reg["X17"],
                         "SP": self.reg["X28"], "FP": self.reg["X29"],
                         "LR": self.reg["X30"]})