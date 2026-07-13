class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        top, bottom = 0, m * n - 1

        while top <= bottom:
            mid = top + (bottom - top) // 2
            row, col = mid // n , mid % n

            if target > matrix[row][col]:
                top = mid + 1
            elif target < matrix[row][col]:
                bottom = mid - 1
            else:
                return True
        
        return False



        