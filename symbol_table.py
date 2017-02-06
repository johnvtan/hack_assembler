# contains symbol table class for storing symbols/labels from program

class SymbolTable:
    def __init__(self):
        
        # table contains all symbols, including these predefined ones
        self.table = {'SP': 0, 'LCL': 1, 'ARG': 2,
                      'THIS': 3, 'THAT': 4, 'R0': 0, 
                      'R1': 1, 'R2': 2, 'R3': 3, 'R4': 4,
                      'R5': 5, 'R6': 6, 'R7': 7, 'R8': 8,
                      'R9': 9, 'R10': 10, 'R11': 11, 'R12': 12,
                      'R13': 13, 'R14': 14, 'R15': 15, 
                      'SCREEN': 0x4000, 'KBD': 0x6000}

    def add_entry(self, symbol, address):
        # method for adding symbol to table
        self.table[symbol] = address

    def contains(self, symbol):
        # checking if symbol is in dictionary
        if symbol in self.table:
            return True
        return False

    def get_address(self, symbol):
        return self.table[symbol]
