class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        total, lenght = len(s) - 1, 0

        while s[total] == ' ':
            total -= 1
        
        while total >= 0 and s[total] != ' ':
            lenght += 1
            total -= 1
        
        return lenght
        