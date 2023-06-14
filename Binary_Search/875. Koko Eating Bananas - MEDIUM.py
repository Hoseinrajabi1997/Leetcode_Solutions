class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_spead = math.ceil(sum(piles) / h)
        l, r = min_spead , max(piles)
        while l < r:
            mid = l + (r-l) // 2
            total = sum([math.ceil(x/mid) for x in piles])
            if total <= h:
                r = mid
            else:
                l = mid + 1
        return r