class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        look = 0
        checker = set(nums)


        for i in range(len(nums)):
            if nums[i] - 1 not in checker:
                difference = 1

                while nums[i] + difference in checker:
                    difference += 1
                
                look = max(look, difference)
        return look