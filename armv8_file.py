"""
This module handles file parsing for armv8-sim.
"""
from armv8_core import ARMv8Core


def coreParseFile(core, file):
    """
    Parse a given file with a given ARMv8Core.
    """
    labels = {}
    code = {}
    
    lines = file.read().splitlines()
    
    PC = 0
    for line in lines:
        if line.endswith(":"):
            if " " not in line:
                labels[line[:-1]] = PC
        
        PC = PC + 4
    
    PC = 0
    for line in lines:
        cline = [x.replace(',','') for x in line.split()]
        code[PC] = cline
    
        PC = PC + 4
    
    print labels
    print code
    
    return


def parseFile(file):
    """
    Method for quickly parsing a file with a new ARMv8Core.
    """
    c = ARMv8Core()
    return coreParseFile(c, file)