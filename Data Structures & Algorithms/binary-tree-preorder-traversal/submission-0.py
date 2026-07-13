# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []

        def preOrdr(node):
            if not node:
                return 
            result.append(node.val)
            preOrdr(node.left)
            preOrdr(node.right)
        
        preOrdr(root)
        return result

        