# Assembler class using Parser and Code classes
from parser import Parser
from parser import Commands
from symbol_table import SymbolTable
import code
import sys

class Assembler:
    
    def __init__(self):
        self.table = SymbolTable()
        self.address = 16

    def first_pass(self, filename):
        # first pass: advancing through file step by step to build up symbol table
        p = Parser(filename)
        current_address = 0
        while p.has_more_commands():
            p.advance()
            c_type = p.command_type()
            if c_type == Commands.C_COMMAND or c_type == Commands.A_COMMAND:
                # incrementing the instruction address
                current_address += 1
            elif c_type == Commands.L_COMMAND:
                # adding new symbol/label to table
                self.table.add_entry(p.symbol(), current_address)

    def second_pass(self, filename):
        # second pass: actually generate the binary for each instruction using the
        # symbol table built up from the first pass
        p = Parser(filename)

        # creating new file name, with .hack ending
        newfile = filename.split('.')[0] + '.hack'
        with open(newfile, 'w') as f:
            while p.has_more_commands():
                p.advance()
                c_type = p.command_type()
                if c_type == Commands.C_COMMAND:
                    d, c, j = p.tokenize_C_inst() 
                    line = code.get_C_inst(d, c, j)
                elif c_type == Commands.A_COMMAND:
                    # we need to check if the symbol is in the table and get its value
                    line = code.get_A_inst(self.check_symbol(p.symbol()))
                else:
                    # if its anything else, don't write anything and start again from
                    # next line
                    continue

                # writing the line to file
                f.write(line + '\n')
        f.close()
    
    def check_symbol(self, symbol):
        # method for checking if the symbol is a symbol and getting its value
        # from the table
        if symbol.isdigit():
            # if it's a digit, then return itself since we want that value
            return symbol
        else:
            if symbol not in self.table.table:
                # if not in table, then add it to the table starting from address 16
                self.table.add_entry(symbol, self.address)
                self.address += 1
            return self.table.get_address(symbol)
   
    def assemble(self, filename):
        #print('First pass...')
        self.first_pass(filename)
        #print('Second pass...')
        self.second_pass(filename) 

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise Exception('User must pass in the file name as second argument. Assembler.py file.asm')
    a = Assembler()
    a.assemble(sys.argv[1]) 
                
