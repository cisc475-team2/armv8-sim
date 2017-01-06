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
        
    def test_addis(self):
        c = ARMv8Core()
        c.reg["X0"].set(0)
        armv8_isa.ADDIS.execute(c, 0, "X0", "X0")
        self.assertEqual(c.flag_zero, True)
        
    def test_subi(self):
        c = ARMv8Core()
        c.reg["X0"].set(1)
        armv8_isa.SUBI.execute(c, 1, "X0", "X1") # immediate = 1
        self.assertEqual(c.reg["X1"].get(), 0)
    
    def test_subis(self):
        c = ARMv8Core()
        c.reg["X1"].set(1)
        armv8_isa.SUBIS.execute(c, 1, "X1", "X1")
        self.assertEqual(c.flag_zero, True)
        
    def test_andi(self):
        c = ARMv8Core()
        c.reg["X0"].set(20)
        armv8_isa.ANDI.execute(c, 5, "X0", "X1") # immediate = 1
        self.assertEqual(c.reg["X1"].get(), 4)
        
    def test_eori(self):
        c = ARMv8Core()
        c.reg["X0"].set(5)
        armv8_isa.EORI.execute(c, 10, "X0", "X1") # immediate = 1
        self.assertEqual(c.reg["X1"].get(), 15)
        
    def test_orri(self):
        c = ARMv8Core()
        c.reg["X0"].set(25)
        armv8_isa.ORRI.execute(c, 10, "X0", "X1") # immediate = 1
        self.assertEqual(c.reg["X1"].get(), 27)