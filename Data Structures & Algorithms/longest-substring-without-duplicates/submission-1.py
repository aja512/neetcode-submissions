class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = set()
        count = 0
        pointer = 0

        for i in range(len(s)):
            
            while s[i] in check:
                check.remove(s[pointer])
                pointer += 1
            
            check.add(s[i])
            count = max(count, i - pointer + 1)    
        
        return count
