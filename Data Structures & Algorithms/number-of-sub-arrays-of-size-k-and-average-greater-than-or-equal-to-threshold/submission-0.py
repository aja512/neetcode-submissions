class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        currSum = sum(arr[:k - 1])
        total = 0
        for i in range(len(arr) - k + 1):
            currSum += arr[i + k - 1]
            if (currSum / k) >= threshold:
                total += 1
            currSum -= arr[i]
        return total
