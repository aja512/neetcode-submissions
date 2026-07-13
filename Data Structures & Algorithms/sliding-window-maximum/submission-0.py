class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mxInt = float('inf')
        result = []

        for i in range(len(nums) - k + 1):
            mxInt = nums[i]
            for j in range(i, i + k):
                mxInt = max(mxInt, nums[j]) 
            result.append(mxInt)
        
        return result
