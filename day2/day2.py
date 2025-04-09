from MyMods.ReadDataFile import read_data
from day2.intcode import IntCode

datalines = read_data("day2/input_day2.txt")

data1 = """1,9,10,3,2,3,11,0,99,30,40,50""".split(",")
data2 = """1,0,0,0,99""".split(",") # becomes 2,0,0,0,99 (1 + 1 = 2).
data3 = """2,3,0,3,99""".split(",")  # becomes 2,3,0,6,99 (3 * 2 = 6).
data4 = """2,4,4,5,99,0""".split(",")  # becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
data5 = """1,1,1,4,99,5,6,0,99""".split(",")  # becomes 30,1,1,4,2,5,6,0,99.

"""
Opcode 1 adds together numbers read from two positions and stores the result in a third position. The three integers immediately after the opcode tell you these three positions - the first two indicate the positions from which you should read the input values, and the third indicates the position at which the output should be stored.

For example, if your Intcode computer encounters 1,10,20,30, it should read the values at positions 10 and 20, add those values, and then overwrite the value at position 30 with their sum.

Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead of adding them. Again, the three integers after the opcode indicate where the inputs and outputs are, not their values.
"""

    
def part1():
    # Your code for part 1 goes here
    intcode = IntCode(data5)
    
        
def part2():
    # Your code for part 2 goes here
    pass
