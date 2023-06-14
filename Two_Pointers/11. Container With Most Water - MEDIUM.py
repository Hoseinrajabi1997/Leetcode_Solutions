class Solution:
    # def __init__(self):
    #     self.max = 0
    def maxArea(self, height: List[int]) -> int:
#     dp = [[-1 for _ in range(len(height))] for _ in range(len(height))]
#     i = 0
#     j = len(height) - 1
#     self.maxAreaRec(height, i, j, dp)
#     return self.max
    # def maxAreaRec(self, height, i , j, dp):

    #     if i >= j:
    #         return 0
    #     if dp[i][j] != -1:
    #         return dp[i][j]

    #     dp[i][j] = min(height[i],height[j]) * (j-i)
    #     if dp[i][j] > self.max:
    #         self.max = dp[i][j]
    #     self.maxAreaRec(height, i+1, j, dp)
    #     self.maxAreaRec(height, i, j-1, dp)
        i = 0
        j = len(height) - 1
        max = 0
        while i < j :
            cap = min(height[i],height[j]) * (j-i)
            if cap > max:
                max = cap
            if height[i] < height [j]:
                i += 1
            else:
                j -= 1
        return max