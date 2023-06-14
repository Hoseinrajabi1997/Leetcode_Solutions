class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = collections.defaultdict(int)
        for i in nums:
            result[i] += 1
        return sorted(result, key=result.get, reverse=True)[:k]