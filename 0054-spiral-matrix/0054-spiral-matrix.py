from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])
        result = []

        while left < right and top < bottom:
            # left to right
            for i in range(left, right):
                result.append(matrix[top][i])
            top += 1

            # top to bottom
            for i in range(top, bottom):
                result.append(matrix[i][right - 1])
            right -= 1

            # right to left
            if top < bottom:
                for i in range(right - 1, left - 1, -1):
                    result.append(matrix[bottom - 1][i])
                bottom -= 1

            # bottom to top
            if left < right:
                for i in range(bottom - 1, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result
