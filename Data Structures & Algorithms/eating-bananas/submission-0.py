class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        result = right

        while left <= right:
            mid = (left + right) // 2

            time = 0

            for p in piles:
                time += math.ceil(float(p)/ mid)
            if time <= h:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result

        
