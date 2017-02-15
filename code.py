# part of hack assembler implementation
# following api proposed in chapter 6 of nand2tetris

_comp_table = {'0': '0101010',
        '1': '0111111',
       '-1': '0111010',
        'D': '0001100',
        'A': '0110000',
       '!D': '0001101',
       '!A': '0110001',
       '-D': '0001111',
       '-A': '0110011',
      'D+1': '0011111',
      'A+1': '0110111',
      'D-1': '0001110',
      'A-1': '0110010',
      'D+A': '0000010',
      'D-A': '0010011',
      'A-D': '0000111',
      'D&A': '0000000',
      'D|A': '0010101',
        'M': '1110000',
       '!M': '1110001',
       '-M': '1110011',
      'M+1': '1110111',
      'M-1': '1110010',
      'D+M': '1000010',
      'D-M': '1010011',
      'M-D': '1000111',
      'D&M': '1000000',
      'D|M': '1010101'}

_dest_table = {'NULL' : '000',
           'M'   : '001',
           'D'   : '010',
           'MD'  : '011',
           'A'   : '100',
           'AM'  : '101',
           'AD'  : '110',
           'AMD' : '111'}

_jump_table = {'NULL' : '000',
           'JGT' : '001',
           'JEQ' : '010',
           'JGE' : '011',
           'JLT' : '100',
           'JNE' : '101',
           'JLE' : '110',
           'JMP' : '111'}

    

def get_A_inst(address):
	# returns the full binary string for corresponding A instruction
	# zfill fills the string with 0s to the left the specified number of digits
	return '0' + str(bin(int(address)))[2:].zfill(15) 

def get_C_inst(d, c, j):
	# returns full binary string for C instruction
	return '111' + comp(c) + dest(d) + jump(j)

def dest(d):
	# returns 8 bit binary string for dest part of C instrcution
	return _dest_table[d]

def comp(c):
	# returns 3 bit binary string from comp table
	return _comp_table[c]

def jump(j):
	# returns 3 bit binary string from jump table
	return _jump_table[j]







