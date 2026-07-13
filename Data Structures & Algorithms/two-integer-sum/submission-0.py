class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()

        for idx in range(len(nums)):
            if target - nums[idx] in seen:
                return sorted([idx, nums.index(target - nums[idx])])
            seen.add(nums[idx])
            