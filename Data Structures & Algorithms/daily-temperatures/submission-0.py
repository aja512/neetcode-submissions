class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                stackTemp, stackIdx= stack.pop()
                result[stackIdx] = idx - stackIdx
            stack.append((temp, idx))
        return result
