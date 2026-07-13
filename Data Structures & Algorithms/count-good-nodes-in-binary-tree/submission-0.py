# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: 
            return 0
        goodCount = 0
        q = collections.deque([(root, -float('inf'))])

        while q:
            node,mxVal = q.popleft()

            if node.val >= mxVal:
                goodCount += 1
            currentMax = max(mxVal, node.val)   
            if node.left:   
                q.append((node.left, currentMax))
            if node.right:  
                q.append((node.right, currentMax))
        
        return goodCount