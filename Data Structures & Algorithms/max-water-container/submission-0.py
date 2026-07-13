class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        mxArea = 0

        i, j = 0, len(heights) - 1

        while i < j:
            result = (j - i) * min(heights[i], heights[j])
            mxArea = max(mxArea, result)
            if heights[i] <= heights[j]:
                i += 1
            else: 
                j -= 1 
        return mxArea