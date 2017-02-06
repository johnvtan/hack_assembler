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

    def has_more_commands(self):
        # returns True if there are more lines to be read, False if EOF
        # storing current position so that we can go back
        current_pos = self.f.tell()
        
        if self.f.readline() == '':
            # then we're at the end of file
            self.f.seek(current_pos)            # return to prev position
            return False
        else:
            self.f.seek(current_pos)
            return True

    def advance(self):
        # reads next command from input and makes it current command
        # todo: cleaning current command (removing comments and whitespace)
        self.current_command = self.f.readline()
        
        # removing whitespace and newline character
        self.current_command = (self.current_command.replace(' ', '')).rstrip('\n')
                           
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
            return ''.join([self.current_command[i] for i in range(1, len(self.current_command))])
        elif self.command_type() == Commands.L_COMMAND:
            return ''.join([self.current_command[i] for i in range(1, len(self.current_command) - 1)])
        else:
            raise ValueError('Command cannot be a C_COMMAND for symbol() method')
     
    def tokenize_C_inst(self):
        # method to separate dest, comp, and jump tokens from C instruction string
        # C instruction is in form dest=comp;jump
        if self.command_type() == Commands.C_COMMAND:
            # first split command by = - first part should be dest
            split_command = self.current_command.split('=')
            dest = split_command[0]
            if len(split_command) > 1:
                # if there's still stuff left, then split again by ;
                second_split = split_command[1].split(';')
                # first part of this split is comp
                comp = second_split[0]
                if len(second_split) > 1:
                    # if theres still more stuff left, then the rest is jump
                    jump = second_split[1]
                else:
                    jump = ''
            else:
                comp = ''
        return dest, comp, jump
            


