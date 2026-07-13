class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        speed = right

        while left <= right:
            hours = (left + right) // 2
            time = 0

            for p in piles:
                time += math.ceil(float(p)/ hours)
            # print(time)
            if time <= h:
                speed = min(speed, hours)
                right = hours - 1
            else:
                left = hours + 1
        
        return speed

        
