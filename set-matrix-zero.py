from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        xMax = len(matrix)
        yMax = len(matrix[0])
        for x in range(xMax):
            if 0 in matrix[x]:
                matrix[x] = [0]*yMax

