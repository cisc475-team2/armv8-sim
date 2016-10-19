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