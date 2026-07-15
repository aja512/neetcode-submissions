# Classic Median of Median problems
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def helper(start, comb):
            # If combination size is same as or equal to k
            if len(comb) == k:
                res.append(comb.copy()) # Copying the contents of the current combination onto the result array
                return
            
            # Start generating all sorts of possible subsets from the start to n of size k
            for i in range(start, n + 1):
                comb.append(i)
                helper(i+1, comb)   # Recursive call of the function to consider other numbers and reduce logic
                comb.pop()  # Remove last element before trying another number
        
        helper(1, [])   # Pass it with the empty array
        return res