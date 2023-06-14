class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # using hashmap
        seen = {}
        for key, value in enumerate(nums):
            second = target - value
            if second in seen:
                return [key, seen[second]]
            seen[value] = key
