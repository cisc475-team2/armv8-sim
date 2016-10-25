"""
This module provides tests for I-format instructions.
"""
from tests import ARMv8Core
from tests import armv8_isa
import unittest


class I_Instructions_Test(unittest.TestCase):
    
    
    def test_addi(self):
        c = ARMv8Core()
        c.reg["X0"].set(1)
        armv8_isa.ADDI.execute(c, 1, "X0", "X1") # immediate = 1
        self.assertEqual(c.reg["X1"].get(), 2)
        
    def test_subi(self):
        c = ARMv8Core()
        c.reg["X0"].set(1)
        armv8_isa.ADDI.execute(c, 1, "X0", "X1") # immediate = 1
        self.assertEqual(c.reg["X1"].get(), 0)