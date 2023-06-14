class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i,val in enumerate(nums):
            if i > 0 and nums[i-1] == val:
                continue
            l, r = i+1, len(nums) - 1
            while l < r:
                temp = val + nums[l] + nums[r]
                if temp > 0 :
                    r -= 1
                elif temp < 0:
                    l += 1
                else:
                    result.append([val, nums[l], nums[r]])
                    l +=1
                    r -= 1
                    while nums[l-1] == nums[l] and l < r:
                        l += 1
        return result