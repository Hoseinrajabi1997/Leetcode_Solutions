class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix[0]) - 1
        bottom, top = 0, len(matrix) - 1
        while bottom <= top:
            mid =  bottom + (top - bottom) // 2
            print("mid", mid)
            if matrix[mid][0] <= target and target <= matrix[mid][r]:
                break
            elif matrix[mid][0] > target:
                top = mid - 1
            else:
                bottom = mid + 1
        while l <= r:
            m = l + ((r - l) // 2)
            if matrix[mid][m] > target:
                r = m - 1
            elif matrix[mid][m] < target:
                l = m + 1
            else:
                return True
        return False