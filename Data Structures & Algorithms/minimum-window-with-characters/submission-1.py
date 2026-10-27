class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or t == "": return ""
        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        have, need = 0, len(countT)
        result, resLen = [-1, -1], float("inf")
        leftPtr = 0

        for ptr in range(len(s)):
            c = s[ptr]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                if ptr - leftPtr + 1 < resLen:
                    result = [leftPtr, ptr]
                    resLen = ptr - leftPtr + 1
                
                window[s[leftPtr]] -= 1

                if s[leftPtr] in countT and window[s[leftPtr]] < countT[s[leftPtr]]:
                    have -= 1

                leftPtr += 1
        
        left, right = result
        return s[left:right + 1] if resLen != float("inf") else ""