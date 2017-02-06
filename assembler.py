# Assembler class using Parser and Code classes
from parser import Parser
from parser import Commands
import code
import sys

class Assembler:
    
    def __init__(self):
        pass

    def first_pass(self, filename):
        p = Parser(filename)
    
        # creating new file name to write binary to
        newfile = filename.split('.')[0] + '.hack'
        with open(newfile, 'w') as f:
            while p.has_more_commands():
                p.advance()
                if p.command_type() == Commands.C_COMMAND:
                    d, c, j = p.tokenize_C_inst()
                    line = code.get_C_inst(d, c, j)
                elif p.command_type() == Commands.A_COMMAND:
                    line = code.get_A_inst(p.symbol())
                
                # at the end, write the line with the newline character
                f.write(line + '\n')
        f.close()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise Exception('User must pass in the file name as second argument. Assembler.py file.asm')
    a = Assembler()
    a.first_pass(sys.argv[1]) 
                
