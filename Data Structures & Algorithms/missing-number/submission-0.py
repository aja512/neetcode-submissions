class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sumTotal = sum(nums)

        rangeTotal = (len(nums) * (len(nums) + 1)) // 2

        return rangeTotal - sumTotal