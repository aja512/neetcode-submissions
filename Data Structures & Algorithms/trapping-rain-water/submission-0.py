class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:  
            return 0
        
        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        trappedWater = 0

        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                trappedWater += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                trappedWater += rightMax - height[right]
        
        return trappedWater
            