"""
Test cases for armv8_core.py
"""
from tests import ARMv8Core
from tests import instruction
import unittest

class ARMv8Core_Test(unittest.TestCase):
    
    
    def test_reg_aliases(self):
        c = ARMv8Core()
        c.reg["IP0"].set(10)
        self.assertEqual(c.reg["IP0"].get(),c.reg["X16"].get())
        self.assertEqual(c.reg["IP0"], c.reg["X16"])
    
    def test_reg_set_get(self):
        c = ARMv8Core()
        i = 0
        while i < 31:
            c.reg["X{}".format(i)].set(i+1)
            i = i + 1
        
        j = 0
        while j < 31:
            a = c.reg["X{}".format(j)].get(hexa=True)
            b = c.reg["X{}".format(j)].get(binary=True)
            self.assertEqual(a, hex(j+1))
            self.assertNotEqual(a, hex(0))
            self.assertEqual(b, "{0:b}".format(j+1))
            self.assertNotEqual(b, "{0:b}".format(0))
            j = j + 1
        
        self.assertEqual(i,j)