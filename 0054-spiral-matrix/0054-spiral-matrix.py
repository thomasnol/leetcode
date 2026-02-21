class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # edit matrix inplace
        # right: entire first row
        # down: last element of every row
        # left: entire last row, reversed
        # up: first element of every row, reversed
        res = []
        while matrix:
            if matrix:
                res += (matrix.pop(0))
            
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())
            
            if matrix:
                res += (matrix.pop()[::-1])
            
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))
        return res