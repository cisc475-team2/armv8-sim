"""
This module provides tests for R-format instructions.
"""
from tests import ARMv8Core
from tests import armv8_isa
import unittest

class R_Instructions_Test(unittest.TestCase):
    
    
    def test_add(self):
        c = ARMv8Core()
        c.reg["X0"].set(1)
        c.reg["X1"].set(1)
        armv8_isa.ADD.execute(c, "X0", 0, "X1", "X2")
        self.assertEqual(c.reg["X2"].get(), 2)
        
    def test_sub(self):
        c = ARMv8Core()
        c.reg["X0"].set(4)
        c.reg["X1"].set(3)
        armv8_isa.SUB.execute(c, "X0", 0, "X1", "X2")
        self.assertEqual(c.reg["X2"].get(), 1)
        
    def test_addi(self):
        c = ARMv8Core()
        c.reg["X0"].set(1)
        armv8_isa.ADDI.execute(c, 1, "X0", "X1") # immediate = 1
        self.assertEqual(c.reg["X1"].get(), 2)