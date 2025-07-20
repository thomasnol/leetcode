class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # pop explored squares so that the cur matrix always represents all unexplored squares
        ret = []
        while matrix:
            # right side: entire first array
            ret += matrix.pop(0)
            # down side: last entry of every array
            if matrix and matrix[0]:
                for row in matrix:
                    ret.append(row.pop())
            # left side: entire last array, in reverse order
            if matrix:
                ret += (matrix.pop()[::-1])
            # up side: first entry of every array, in reverse order
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ret.append(row.pop(0))
        return ret