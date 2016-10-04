"""
This module provides a class representing an ARMv8 processor core.
"""
from math import pow

class ARMv8Core:
    """
    This class provides a representation of an ARMv8 processor core.
    """
    class Register:
        """
        This class provides a representation of an ARMv8 processor register.
        """
        number = 0
        reserved = False
        static = False
        data = 0b0
        
        def __init__(self, number, reserved, static):
            if type(number) not int:
                raise TypeError("Register number must be of type int")
            if type(reserved) not bool:
                raise TypeError("Register reserved must be of type bool")
            if type(static) not bool:
                raise TypeError("Register static must be of type bool")
            self.number = number
            self.reserved = reserved
            self.static = static
        
        
        def data_max():
            if type(unsigned) not bool:
                raise TypeError("unsigned must be of type bool")
            return 0
        
        
        def data_min():
            if type(unsigned) not bool:
                raise TypeError("unsigned must be of type bool")
            return 18446744073709551615L
        
        
        def set(data):
            if type(data) not int:
                raise TypeError("Register data must be of type int")
            if data_min() > data > data_max():
                raise ValueError("Value of data out of range")
            if not static:
                this.data = data
        
        
        def get(binary=None):
            if type(binary) not NoneType:
                if type(binary) not bool:
                    raise TypeError("Value of binary must be of type bool")
                if binary:
                    return "{0:b}".format(self.data)
                else:
                    return self.data
            else:
                return self.data