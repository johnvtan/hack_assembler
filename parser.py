# hack assembler implementation
# this file contains the Parser class, which parses the source hack asm code

class Commands:
    # basically an enum for different command types
    C_COMMAND, A_COMMAND, L_COMMAND = range(3)

class Parser:
    
    def __init__(self, filename):
        # Constructor - needs input filename f

        # when parser is initialized, it opens the asm file
        # we're checking to make sure its a .asm file
        # storing the open file as self.f
        if filename.split('.')[1] == 'asm':
            try:
                self.f = open(filename, 'r')
            except OSError:
                print('Cannot open ', filename) 
        else:
            raise ValueError('File name needs to end in ".asm"')

        # tracks current command
        self.current_command = None

    def advance(self):
        # reads next command from input and makes it current command
        self.current_command = self.f.readline()
        return

    def command_type(self):
        # returns the type of current command
        if self.current_command[0] == '@':
            # if the command starts with @, then its an A command
            return Commands.A_COMMAND
        elif self.current_command[0] == '(':
            return Commands.L_COMMAND
        else:
            return Commands.C_COMMAND

    def symbol(self):
        # returns the symbol or decimal of the current A or L Command
        if self.command_type() == Commands.A_COMMAND:
            return ''.join([self.current_command[i] for i in range(1, len(self.current_command) - 1)])
        elif self.command_type() == Commands.L_COMMAND:
            return ''.join([self.current_command[i] for i in range(1, len(self.current_command) - 2)])
        else:
            raise ValueError('Command cannot be a C_COMMAND for symbol() method')

    def dest(self):
        return
     
           
            
if __name__ == '__main__':
    # testing stuff
    p = Parser('test.asm')
    p.advance()
    print(p.current_command)
    print(p.command_type())
    print(p.symbol())



