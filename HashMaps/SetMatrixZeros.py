from typing import List


class Solution:
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

if __name__ == "__main__":
    testcase1 =  [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    expected1 = [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    testcase2 = [[1,1,1],[1,0,1],[1,1,1]]
    expected2 = [[1,0,1],[0,0,0],[1,0,1]]
    testcase3 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    expected3 = [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    solution = Solution()
    #solution.setZeroes(testcase1)
    #print(testcase1 == expected1)
    print(solution.setZeroes(testcase1) == expected1)
    print(solution.setZeroes(testcase2) == expected2)
    print(solution.setZeroes(testcase3) == expected3)