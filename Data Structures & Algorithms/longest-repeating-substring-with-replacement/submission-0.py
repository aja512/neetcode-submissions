from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = 0
        check = defaultdict()
        maxFreq = 0
        pointer = 0

        for idx in range(len(s)):
            check[s[idx]] = 1 + check.get(s[idx], 0)
            maxFreq = max(maxFreq, check[s[idx]])

            while (idx - pointer + 1) - maxFreq > k:
                check[s[pointer]] -= 1
                pointer += 1
            
            count = max(count, idx - pointer + 1)
        
        return count