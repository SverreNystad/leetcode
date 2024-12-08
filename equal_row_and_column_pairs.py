from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        equals = 0
        length = len(grid)
        rows = []
        columns = []

        rows = grid[:length]
        columns = [[grid[i][j] for i in range(length)] for j in range(length)]

        rows = [sorted(row) for row in rows]
        columns = [sorted(column) for column in columns]

        for row in rows:
            for col in columns:
                if row == col:
                    equals += 1
        return equals
