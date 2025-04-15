from MyMods.ReadDataFile import read_data
from day5.opcodecompiler import OpCodeCompiler

# datalines = read_data("day5/input_day5.txt")
data = """1002,4,3,4,99""".split(",")

    
def part1():
    print("== Day5 part 1 ==")
    # Your code for part 1 goes here
    op = OpCodeCompiler(data, 1)
    print(op.output)
        
def part2():
    # Your code for part 2 goes here
    pass
