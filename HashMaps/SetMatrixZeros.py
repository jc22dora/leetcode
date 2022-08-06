from typing import List


class SetMatrixZeros:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = set(), set()
        rln, cln = len(matrix), len(matrix[0])
        for row in range(rln):
            for col in range(cln):
                if(matrix[row][col] == 0):
                    rows.add(row)
                    cols.add(col)
        for i in range(rln):
            for j in range(cln):
                if(i in rows or j in cols):
                    matrix[i][j] = 0

        return matrix
    