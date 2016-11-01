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
        
    def test_udiv(self):
        c = ARMv8Core()
        c.reg["X0"].set(10)
        c.reg["X1"].set(5)
        armv8_isa.UDIV.execute(c, "X0", 0x03, "X1", "X2")
        self.assertEqual(c.reg["X2"].get(), 2)
        
    def test_mul(self):
        c = ARMv8Core()
        c.reg["X0"].set(10)
        c.reg["X1"].set(5)
        armv8_isa.UDIV.execute(c, "X0", 0x1F, "X1", "X2")
        self.assertEqual(c.reg["X2"].get(), 50)
        
    def test_umulh(self):
        c = ARMv8Core()
        c.reg["X0"].set(10)
        c.reg["X1"].set(5)
        armv8_isa.UDIV.execute(c, "X0", 0, "X1", "X2")
        self.assertEqual(c.reg["X2"].get(), 50)
        
    def test_sdiv(self):
        c = ARMv8Core()
        c.reg["X0"].set(10)
        c.reg["X1"].set(5)
        armv8_isa.UDIV.execute(c, "X0", 0x02, "X1", "X2")
        self.assertEqual(c.reg["X2"].get(), 2)
