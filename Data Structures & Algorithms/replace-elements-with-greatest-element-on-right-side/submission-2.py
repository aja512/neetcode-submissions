class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [0] * len(arr)
        rightMax = -1

        for i in range(len(arr) - 1, -1, -1):
            ans[i] = rightMax
            rightMax = max(arr[i], rightMax)
        return ans

'''
Algorithm
1. Create a result array ans of the same size as the input.
2. Initialize rightMax to -1 (the value for the last position).
3. Traverse the array from right to left using index i.
4. For each index i, store the current rightMax in ans.
5. Update rightMax to be the maximum of itself and arr[i].
6. Return the ans array.
'''