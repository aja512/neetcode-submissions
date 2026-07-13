class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = [[] for _ in range(n + 1)]
        result[0] = [""]

        for beg in range(n + 1):
            for end in range(beg):
                for left in result[end]:
                    for right in result[beg - end - 1]:
                        result[beg].append("(" + left + ")" + right)
        
        return result[-1]