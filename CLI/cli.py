# package imports
from CLI import ARMv8Core
from CLI import armv8_isa
from CLI import instruction
import sys

# main function
def main():
    c = ARMv8Core()
    print("Welcome to our ARMv8 simulator!")
    print("Type help at any time for a list of commands, instructions, and tips")
    print ""
    running = True
    while(running):
        arg = raw_input("Enter a command or an ARMv8 instruction: ")
        str(arg)
        args = str.split(arg)
        
####### COMMANDS #################################################################################
        if args[0] == "help":
            print_commands()
            print_instructions()
            print_tips()
        elif args[0] == "exit":
            running = False
        elif args[0] == "printregs":
            print_all_registers(c)
            
####### INSTRUCTIONS ############################################################################
        elif args[0] == "ADD":
            if error_check(args) == 1:
                armv8_isa.ADD.execute(c, args[3], 0, args[2], args[1])
                print_register(args[1],c)
        elif args[0] == "ADDI":
            if error_check(args) == 1:
                armv8_isa.ADDI.execute(c, int(args[3]), args[2], args[1])
                print_register(args[1],c)
        elif args[0] == "SUB":
            if error_check(args) == 1:
                armv8_isa.SUB.execute(c, args[3], 0, args[2], args[1])
                print_register(args[1],c)
        elif args[0] == "SUBI":
            if error_check(args) == 1:
                armv8_isa.SUBI.execute(c, int(args[3]), args[2], args[1])
                print_register(args[1],c)
        elif args[0] == "MUL":
            if error_check(args) == 1:
                armv8_isa.MUL.execute(c, args[3], 0x1F, args[2], args[1])
                print_register(args[1],c)
        elif args[0] == "UMULH":
            if error_check(args) == 1:
                armv8_isa.UMULH.execute(c, args[3], 0, args[2], args[1])
                print_register(args[1],c)
            
        else:
            print "Please enter a valid command. Type 'help' for valid options."
            print ""

########################################################################################
# printing functions
def print_commands():
    print "Commands:"
    print "  exit           exits and closes program"
    print "  printregs      print all registers"
    print ""

def print_instructions():
    print "Instructions:"
    print "  Key:"
    print "    Xd = destination register where value is stored"
    print "    Xn = register where 1st value to be used is stored"
    print "    Xm = register where 2nd value to be used is stored"
    print "    d, n, and m must be integers between 0 and 31"
    print "    SP = stack pointer (can be used in certain instructions in place of Xd)"
    print "    #imm = immediate integer value to be used in insturction (used in place of register and is not stored)"
    print "  Arithmetic operations:"
    print "    ADD Xd, Xn, Xm           Add"
    print "    ADDI Xd, Xn, #imm        Add (immediate)"
    print "    SUB Xd, Xn, Xm           Subtract"
    print "    SUBI Xd. Xn, #imm        Subtract (immediate)"
    print "    MUL Xd, Xn, Xm           Multiply"
    print "    UMULH Xd, Xn, Xm         Unsigned multiply high"
    print "    SDIV Xd, Xn, Xm          Signed divide"
    print "    UDIV Xd. Xn, Xm          Unisnged Divide"
    print "  Logic operations:"
    print "    AND Xd, Xn, Xm           Bitwise AND"
    print "    ANDI Xd|SP, Xn, #imm     Bitwise AND immediate"
    print "    EOR Xd, Xn, Xm           Bitwise exclusive OR"
    print "    EORI Xd|SP, Xn, #imm     Bitwise exclusive OR (immediate)"
    print "    LSL Xd, Xn, Xm|#imm      Logical shift left (register or immediate)"
    print "    LSR Xd, Xn, Xm|#imm      Logical shift right (register or immediate)"
    print "    ORR Xd, Xn, Xm           Bitwise inclusive OR"
    print "    ORRI Xd|SP, Xn, #imm     Bitwise inclusive OR (immediate)"
    print ""
    
def print_tips():
    print "Tips:"
    print "  Checkout http://armsim.cs.uvic.ca/ for another ARM simulation tool"
    print ""
    
def print_register(register, core):
    print register + " = " + str(core.reg[register].get())
    print "Hex = " + hex(core.reg[register].get())
    print "Binary = " + bin(core.reg[register].get())
    print ""
    
def print_all_registers(core):
    for num in range(0,31):
        register = "X" + str(num)
        print_register(register, core)
        print "-----------------------------------"
    print_register("XZR", core)
    print ""
###############################################################################################
# error checking
def error_check(args):
    if len(args) != 4:
        print "Error: incorrect number of arguments."
        print "Instructions should have the following format:"
        print "eg. ADD X2 X0 X1 or ADDI X3 X2 2"
        print ""
        return -1
    else:
        return 1
    