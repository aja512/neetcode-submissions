from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # result[i] will store all valid combinations for i pairs of parentheses
        result = [[] for _ in range(n + 1)]
        result[0] = [""]  # Base case: 0 pairs of parentheses is an empty string

        # Iterate from 1 to n to build up the solution
        for i in range(1, n + 1):
            # The string can be split into a "core" part and a "remainder" part
            # The core part is enclosed in one pair of parentheses: "(...)"
            # The remainder part is a valid parenthesis string of the remaining size
            for j in range(i):
                # j is the number of pairs inside the outer parentheses
                # The remaining (i-1-j) pairs are placed after it
                for left_part in result[j]:
                    for right_part in result[i - 1 - j]:
                        result[i].append(f"({left_part}){right_part}")

        return result[n]
