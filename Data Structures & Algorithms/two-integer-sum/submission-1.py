class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()

        for i in range(len(nums)):
            if target - nums[i] in seen:
                return sorted([i, nums.index(target - nums[i])])
            seen.add(nums[i])