class Solution:
    def isValid(self, s: str) -> bool:
        matchCheck = {")":"(", ">":"<", "}":"{","]":"["}
        stack = [] 

        for char in s:
            if char in matchCheck:
                if stack and stack[-1] == matchCheck[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return len(stack) == 0
                