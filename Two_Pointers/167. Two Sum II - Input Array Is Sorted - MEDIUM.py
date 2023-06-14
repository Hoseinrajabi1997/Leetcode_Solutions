class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while j > i:
            val = numbers[i] + numbers[j]
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            elif val < target:
                i += 1
            else:
                j -= 1
