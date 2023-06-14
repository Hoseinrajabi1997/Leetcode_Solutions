class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        l, r = 0, len(height) -1
        leftmx, rightmx = height[l], height[r]
        while l<r:
            if leftmx < rightmx:
                l += 1
                leftmx = max(leftmx, height[l])
                result += leftmx - height[l]
            else:
                r -= 1
                rightmx = max(rightmx, height[r])
                result += rightmx - height[r]
        return result
# second solution with two traversal idea. needs edit from right to left
# result = 0
# if len(height) == 1:
#     return 0

# if height[0] == 0:
#     height = height[1:]

# if height[len(height)-1] == 0:
#     height = height[:len(height)-2]

# i, j= 0, 1
# temp = 0
# while i < len(height) and j < len(height):
#     print(i,j)
#     if height[i] <= height[j]:
#         print(temp)
#         result += ((j-i-1)*height[i]) - temp
#         temp = 0
#         j += 1
#         i = j-1
#     else:
#         temp += height[j]
#         j += 1
# i = len(height) -1
# j = len(height) -2
# temp = 0
# print("===========")
# while i >= 0 and j >= 0:
#     if height[i] < height[j]:
#         print(temp)
#         result += ((i-j-1)*height[i]) - temp
#         temp = 0
#         i = j
#         j -= 1
#     else:
#         temp += height[j]
#         j -= 1
# return result