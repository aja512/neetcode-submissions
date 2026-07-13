class MinStack:
    def __init__(self):
        self.min = float('inf')
        self.st = []


    def push(self, val: int) -> None:
        if not self.st:
            self.st.append(0)
            self.minVal = val
        else:
            self.st.append(val - self.minVal)
            if val < self.minVal:
                self.minVal = val

    def pop(self) -> None:
        if not self.st: return
        temp = self.st.pop()
        if temp < 0:
            self.minVal = self.minVal - temp
        
    def top(self) -> int:
        top = self.st[-1]

        if top > 0:
            return top + self.minVal
        else:
            return self.minVal
        

    def getMin(self) -> int:
        return self.minVal
        
