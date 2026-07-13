class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        def calculate(operation, a, b):
            if operation == "+":
                return a + b
            elif operation == "-":
                return b - a
            elif operation == "*":
                return a * b
            elif operation == "/":
                return int(b / a)
        

        for char in tokens:
            try:
                # Attempt to convert the token to an integer
                stack.append(int(char))
            except ValueError:
                # If conversion fails, it's an operator
                a = stack.pop()
                b = stack.pop()
                result = calculate(char, a, b)
                stack.append(result)
        
        return stack[0]