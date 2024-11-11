import math
from MyMods.Matrix import Matrix


class CableMap(Matrix):
    DIRS = {
        'U': (-1, 0),
        'D': (1, 0),
        'R': (0, 1),
        'L': (0, -1),
    }
    def __init__(self, dimj, dimi):
        super().__init__(dimj, dimi, '.')
        self.start = (math.floor(dimj / 2), math.floor(dimi / 2))
        self.crossings = []

    def process_data_lines(self, datalines):
        lines = datalines.split("\n")
        for index, line in enumerate(lines):
            wire = index + 1  # wire 1 = 1, wire 2 = 2
            datas = line.strip().split(",")
            j, i = self.start
            for dirs in datas:
                dr = dirs[0]
                unts = int("".join(dirs[1:]))
                j, i = self.do_dirs(dr, unts, j ,i , wire)
        

    def do_dirs(self, dr, unts, j, i, wire):
        # for loop over unts
        print(f"moving {unts} units to {dr}.")
        for n in range(unts + 1):
            newj, newi = j + (self.DIRS[dr][0] * n), i + (self.DIRS[dr][1] * n)
            otherwire = 2 if wire == 1 else 1
            if self.grid[newj][newi] == '.':
                self.grid[newj][newi] = f"{wire}"
            elif self.grid[newj][newi] == f"{otherwire}":
                self.grid[newj][newi] = 'X'
                if newj != self.start[0] and newi != self.start[1]:
                    self.crossings.append((newj, newi))
        return newj, newi


    def _manhattan_distance(self, coords):
        x = abs(self.start[0] - coords[0])
        y = abs(self.start[1] - coords[1])
        return x + y


    def shortest_manhattan_distance(self):
        shortest = {
            'dist': 1000000000,
            'coordinates': (-1, -1),
        }
        for crd in self.crossings:
            print(f"{crd} -> {self._manhattan_distance(crd)}")
            if self._manhattan_distance(crd) < shortest['dist']:
                shortest['dist'] = self._manhattan_distance(crd)
                shortest['coordinates'] = crd
        return shortest
