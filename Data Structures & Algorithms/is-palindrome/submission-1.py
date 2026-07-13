class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for i in range(len(s)):
            if s[i].isalnum():
                res += s[i].lower()
        # print(res)
        return res == res[::-1]
