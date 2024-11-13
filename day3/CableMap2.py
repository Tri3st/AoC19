import math
import sys


class CableMap2:
    DIRS = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1),
    }
    def __init__(self):
        self.start = 0, 0
        self.wire = {
            '1' : [],
            '2': []
        }
        self.counter = 0
        self.crossings = []
        self.smallest_manhattan = sys.maxsize


    def process(self, data_lines):
        data_lines_strs = data_lines.split('\n')
        for index, data_line in enumerate(data_lines_strs):
            self.counter = 0
            wire_nr = index + 1
            j, i = self.start
            data_strs  = data_line.split(",")
            for data in data_strs:
                data2 = list(data)
                dr = data[0]
                unts = int("".join(data[1:]))
                # j, i = self._do_data(dr, unts, wire_nr, j, i)
                j, i = self._do_data2(dr, unts, wire_nr, j, i)
        # self._find_crossings()
        self._find_crossings2()


    def _do_data2(self, dr, unts, wire_nr, j, i):
        for n in range(1, unts + 1):
            self.counter += 1
            newj = (j + (self.DIRS[dr][0]) * n)
            newi = (i + (self.DIRS[dr][1]) * n)
            self.wire[str(wire_nr)].append((newj, newi, self.counter))
        return newj, newi


    def _find_crossings2(self):
        crossings = []
        for i, j, d in self.wire['1']:
            for (i2, j2, d2) in self.wire['2']:
                if i == i2 and j == j2 and i != 0 and j != 0:
                    self.crossings.append((i, j, d + d2))


    def get_least_steps(self):
        distances = [d for j,i,d in self.crossings]
        print(distances)
        return min(distances)


    def _do_data(self, dr, unts, wire_nr, j, i):
        for n in range(unts + 1):
            newj = (j + (self.DIRS[dr][0]) * n)
            newi = (i + (self.DIRS[dr][1]) * n)
            self.wire[str(wire_nr)].append((newj, newi))
        return newj, newi


    def _find_crossings(self):
        set1 = set(self.wire['1'])
        set2 = set(self.wire['2'])
        crossings = list(set1.intersection(set2))
        for index, crossing in enumerate(crossings):
            print(index, crossing)
            crs = {
                'id': index,
                'coords': crossing,
                'manhattan': abs(crossing[0]) + abs(crossing[1]),
            }
            if crs['coords'] != (0, 0):
                print(crs)
                self.crossings.append(crs)


    def get_smallest_manhattan(self):
        smallest = sys.maxsize
        for crossing in self.crossings:
            if crossing['manhattan'] < smallest:
                smallest = crossing['manhattan']
        self.smallest_manhattan = smallest
        return smallest
