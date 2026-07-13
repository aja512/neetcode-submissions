# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []

        def postOrdr(node):
            if not node:
                return
            postOrdr(node.left)
            postOrdr(node.right)
            result.append(node.val)
        
        postOrdr(root)

        return result
        
