import math
from AoC19.MyMods.Matrix import Matrix


class CableMap(Matrix):
    DIRS = {
        'U': (-1, 0),
        'D': (1, 0),
        'R': (0, 1),
        'L': (0, -1),
    }
    def __init__(self, dimj, dimi):
        super().__init__(dimj, dimi, '.')
        self.start = (math.floor(dimj / 2), math.floor(dimi // 2))
        print(self.grid)

            j, i = self.start


    def do_dirs(self, dr, unts, j, i, wire):
        for loop over unts
        newj, newi = j + (self.DIRECTION[dr][0] * unts), i + self.DIRECTION[dr][1]
        if self.grid[newj][newi] == '.' or self.grid[newj][newi] == 'o':
            self.grid[newj][newi] = f"{wire}"
        elif self.grid[newj][newi] == '1' or self.grid[newj][newi] == '2':
            self.grid[newj][newi] = 'X'
        elif self.grid[newj][newi] == 'X':
            self.grid[newj][newi] = 'X'
        return newj, newi
