class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        checker = set(nums)
        look = 0

        for i in range(len(nums)):
            if nums[i] - 1 not in checker:
                difference = 1
                while nums[i] + difference in checker:
                    difference += 1
                look = max(look, difference)
        return look