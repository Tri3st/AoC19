from MyMods.ReadDataFile import read_data
from day3.CableMap import CableMap

datalines = read_data("day3/input_day3.txt")

datal = "\n".join(datalines)

data = """R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83"""  # = distance 159
data2 = """R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"""  # = distance 135

testdata = """R8,U5,L5,D3
U7,R6,D4,L4"""
    
def part1():
    # Your code for part 1 goes here
    m = CableMap(35000, 35000)
    m.process_data_lines(datal)
    print(m)
    print(m.crossings)
    print(m.shortest_manhattan_distance())

    
        
def part2():
    # Your code for part 2 goes here
    pass
