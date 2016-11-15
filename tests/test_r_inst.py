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
        c.reg["X0"].set(3)
        c.reg["X1"].set(4)
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
        armv8_isa.MUL.execute(c, "X0", 0x1F, "X1", "X2")
        self.assertEqual(c.reg["X2"].get(), 50)
        
    def test_umulh(self):
        c = ARMv8Core()
        c.reg["X0"].set(10)
        c.reg["X1"].set(5)
        armv8_isa.UMULH.execute(c, "X0", 0, "X1", "X2")
        self.assertEqual(c.reg["X2"].get(), 50)
        
    def test_sdiv(self):
        c = ARMv8Core()
        c.reg["X0"].set(10)
        c.reg["X1"].set(5)
        armv8_isa.SDIV.execute(c, "X0", 0x02, "X1", "X2")
        self.assertEqual(c.reg["X2"].get(), 2)
        
    def test_and(self):
        c = ARMv8Core()
        c.reg["X0"].set(10)
        c.reg["X1"].set(5)
        armv8_isa.AND.execute(c, "X0", 0, "X1", "X2")
        self.assertEqual(c.reg["X2"].get(), 0)
        
    def test_eor(self):
        c = ARMv8Core()
        c.reg["X0"].set(10)
        c.reg["X1"].set(5)
        armv8_isa.EOR.execute(c, "X0", 0, "X1", "X2")
        self.assertEqual(c.reg["X2"].get(), 15)
        
    def test_lsl(self):
        c = ARMv8Core()
        c.reg["X0"].set(10)
        c.reg["X1"].set(2)
        armv8_isa.LSL.execute(c, "X0", 0, "X1", "X2")
        self.assertEqual(c.reg["X2"].get(), 40)
        
    def test_lsr(self):
        c = ARMv8Core()
        c.reg["X0"].set(40)
        c.reg["X1"].set(2)
        armv8_isa.LSR.execute(c, "X0", 0, "X1", "X2")
        self.assertEqual(c.reg["X2"].get(), 10)
        
    def test_orr(self):
        c = ARMv8Core()
        c.reg["X0"].set(10)
        c.reg["X1"].set(25)
        armv8_isa.ORR.execute(c, "X0", 0, "X1", "X2")
        self.assertEqual(c.reg["X2"].get(), 27)
        
