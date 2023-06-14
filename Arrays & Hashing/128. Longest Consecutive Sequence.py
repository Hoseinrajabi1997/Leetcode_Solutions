class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        nums = set(nums)
        for num  in nums:
            length = 1
            if num-1 not in nums:
                while num+1 in nums:
                    length += 1
                    num = num+1
            result = max(result, length)
        return result