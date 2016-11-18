# package imports
#from CLI import ARMv8Core
#from CLI import armv8_isa
#from CLI import instruction
import sys

# main function
def main():
 #   c = ARMv8Core()
    print("Welcome to our ARMv8 simulator!")
    print("Type help at any time for a list of commands, instructions, and tips")
    print ""
    running = True
    while(running):
        args = raw_input("Enter a command or an ARMv8 instruction: ")
        #print "you entered", args
        if args == "help":
            print_commands()
            print_instructions()
            print_tips()
        elif args == "exit":
            running = False
        else:
            print "Please enter a valid command"
            print ""

########################################################################################
# printing functions
def print_commands():
    print "Commands:"
    print "  exit    exits and closes program"
    print ""

def print_instructions():
    print "Instructions:"
    print "  Key:"
    print "    Xd = destination register where value is stored"
    print "    Xn = register where 1st value to be used is stored"
    print "    Xm = register where 2nd value to be used is stored"
    print "    d, n, and m must be integers between 0 and 31"
    print "    SP = stack pointer (can be used in certain instructions in place of Xd)"
    print "    #imm = immediate value to be used in insturction (used in place of register and is not stored)"
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

###############################################################################################
# running main
main()