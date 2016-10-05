"""
unittest unit tests for internal files of instruction module and the instruction module itself.
"""
import unittest

import instruction
import r_inst
import i_inst
import d_inst
import b_inst
import cb_inst
import iw_inst

class r_test(unittest.TestCase):
    
    def test_import(self):
        def op_r_a(proc, Rm, shamt, Rn, Rd):
            return
        def op_r_b(proc, Rm, shamt, Rn, Rd):
            return
        
        r_a = r_inst.r_inst(0x001, op_r_a)
        r_b = r_inst.r_inst(0x001, op_r_b)
        r_c = r_inst.r_inst(0x002, op_r_a)
        r_d = r_inst.r_inst(0x001, op_r_a)
        i_r_a = instruction.R(0x001, op_r_a)
        i_r_b = instruction.R(0x001, op_r_b)
        i_r_c = instruction.R(0x002, op_r_a)
        i_r_d = instruction.R(0x001, op_r_a)
        
        self.assertNotEqual(r_a, r_b)
        self.assertNotEqual(r_a, r_c)
        self.assertEqual(r_a, r_a)
        self.assertEqual(r_a, r_d)
        self.assertNotEqual(i_r_a, i_r_b)
        self.assertNotEqual(i_r_a, i_r_c)
        self.assertEqual(i_r_a, i_r_a)
        self.assertEqual(i_r_a, i_r_d)
        self.assertNotEqual(r_a, i_r_b)
        self.assertNotEqual(r_a, i_r_c)
        self.assertEqual(r_a, i_r_a)
        self.assertEqual(r_a, i_r_d)

class i_test(unittest.TestCase):
    
    def test_import(self):
        def op_i_a(proc, ALU_immediate, Rn, Rd):
            return
        def op_i_b(proc, ALU_immediate, Rn, Rd):
            return
        
        i_a = i_inst.i_inst(0x001, op_i_a)
        i_b = i_inst.i_inst(0x001, op_i_b)
        i_c = i_inst.i_inst(0x002, op_i_a)
        i_d = i_inst.i_inst(0x001, op_i_a)
        i_i_a = instruction.I(0x001, op_i_a)
        i_i_b = instruction.I(0x001, op_i_b)
        i_i_c = instruction.I(0x002, op_i_a)
        i_i_d = instruction.I(0x001, op_i_a)
        
        self.assertNotEqual(i_a, i_b)
        self.assertNotEqual(i_a, i_c)
        self.assertEqual(i_a, i_a)
        self.assertEqual(i_a, i_d)
        self.assertNotEqual(i_i_a, i_i_b)
        self.assertNotEqual(i_i_a, i_i_c)
        self.assertEqual(i_i_a, i_i_a)
        self.assertEqual(i_i_a, i_i_d)
        self.assertNotEqual(i_a, i_i_b)
        self.assertNotEqual(i_a, i_i_c)
        self.assertEqual(i_a, i_i_a)
        self.assertEqual(i_a, i_i_d)

class d_test(unittest.TestCase):
    
    def test_import(self):
        def op_d_a(proc, T_address, op, Rn, Rt):
            return
        def op_d_b(proc, T_address, op, Rn, Rt):
            return
        
        d_a = d_inst.d_inst(0x001, op_d_a)
        d_b = d_inst.d_inst(0x001, op_d_b)
        d_c = d_inst.d_inst(0x002, op_d_a)
        d_d = d_inst.d_inst(0x001, op_d_a)
        i_d_a = instruction.D(0x001, op_d_a)
        i_d_b = instruction.D(0x001, op_d_b)
        i_d_c = instruction.D(0x002, op_d_a)
        i_d_d = instruction.D(0x001, op_d_a)
        
        self.assertNotEqual(d_a, d_b)
        self.assertNotEqual(d_a, d_c)
        self.assertEqual(d_a, d_a)
        self.assertEqual(d_a, d_d)
        self.assertNotEqual(i_d_a, i_d_b)
        self.assertNotEqual(i_d_a, i_d_c)
        self.assertEqual(i_d_a, i_d_a)
        self.assertEqual(i_d_a, i_d_d)
        self.assertNotEqual(d_a, i_d_b)
        self.assertNotEqual(d_a, i_d_c)
        self.assertEqual(d_a, i_d_a)
        self.assertEqual(d_a, i_d_d)

class b_test(unittest.TestCase):
    
    def test_import(self):
        def op_b_a(proc, BR_address):
            return
        def op_b_b(proc, BR_address):
            return
        
        b_a = b_inst.b_inst(0x001, op_b_a)
        b_b = b_inst.b_inst(0x001, op_b_b)
        b_c = b_inst.b_inst(0x002, op_b_a)
        b_d = b_inst.b_inst(0x001, op_b_a)
        i_b_a = instruction.B(0x001, op_b_a)
        i_b_b = instruction.B(0x001, op_b_b)
        i_b_c = instruction.B(0x002, op_b_a)
        i_b_d = instruction.B(0x001, op_b_a)
        
        self.assertNotEqual(b_a, b_b)
        self.assertNotEqual(b_a, b_c)
        self.assertEqual(b_a, b_a)
        self.assertEqual(b_a, b_d)
        self.assertNotEqual(i_b_a, i_b_b)
        self.assertNotEqual(i_b_a, i_b_c)
        self.assertEqual(i_b_a, i_b_a)
        self.assertEqual(i_b_a, i_b_d)
        self.assertNotEqual(b_a, i_b_b)
        self.assertNotEqual(b_a, i_b_c)
        self.assertEqual(b_a, i_b_a)
        self.assertEqual(b_a, i_b_d)

class cb_test(unittest.TestCase):
    
    def test_import(self):
        def op_cb_a(proc, COND_BR_address, Rt):
            return
        def op_cb_b(proc, COND_BR_address, Rt):
            return
        
        cb_a = cb_inst.cb_inst(0x001, op_cb_a)
        cb_b = cb_inst.cb_inst(0x001, op_cb_b)
        cb_c = cb_inst.cb_inst(0x002, op_cb_a)
        cb_d = cb_inst.cb_inst(0x001, op_cb_a)
        i_cb_a = instruction.CB(0x001, op_cb_a)
        i_cb_b = instruction.CB(0x001, op_cb_b)
        i_cb_c = instruction.CB(0x002, op_cb_a)
        i_cb_d = instruction.CB(0x001, op_cb_a)
        
        self.assertNotEqual(cb_a, cb_b)
        self.assertNotEqual(cb_a, cb_c)
        self.assertEqual(cb_a, cb_a)
        self.assertEqual(cb_a, cb_d)
        self.assertNotEqual(i_cb_a, i_cb_b)
        self.assertNotEqual(i_cb_a, i_cb_c)
        self.assertEqual(i_cb_a, i_cb_a)
        self.assertEqual(i_cb_a, i_cb_d)
        self.assertNotEqual(cb_a, i_cb_b)
        self.assertNotEqual(cb_a, i_cb_c)
        self.assertEqual(cb_a, i_cb_a)
        self.assertEqual(cb_a, i_cb_d)

class iw_test(unittest.TestCase):
    
    def test_import(self):
        def op_iw_a(proc, MOV_immediate, Rd):
            return
        def op_iw_b(proc, MOV_immediate, Rd):
            return
        
        iw_a = iw_inst.iw_inst(0x001, op_iw_a)
        iw_b = iw_inst.iw_inst(0x001, op_iw_b)
        iw_c = iw_inst.iw_inst(0x002, op_iw_a)
        iw_d = iw_inst.iw_inst(0x001, op_iw_a)
        i_iw_a = instruction.IW(0x001, op_iw_a)
        i_iw_b = instruction.IW(0x001, op_iw_b)
        i_iw_c = instruction.IW(0x002, op_iw_a)
        i_iw_d = instruction.IW(0x001, op_iw_a)
        
        self.assertNotEqual(iw_a, iw_b)
        self.assertNotEqual(iw_a, iw_c)
        self.assertEqual(iw_a, iw_a)
        self.assertEqual(iw_a, iw_d)
        self.assertNotEqual(i_iw_a, i_iw_b)
        self.assertNotEqual(i_iw_a, i_iw_c)
        self.assertEqual(i_iw_a, i_iw_a)
        self.assertEqual(i_iw_a, i_iw_d)
        self.assertNotEqual(iw_a, i_iw_b)
        self.assertNotEqual(iw_a, i_iw_c)
        self.assertEqual(iw_a, i_iw_a)
        self.assertEqual(iw_a, i_iw_d)

if __name__ == '__main__':
    unittest.main()