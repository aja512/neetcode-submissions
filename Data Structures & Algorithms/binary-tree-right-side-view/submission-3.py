# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([root])
        result = []

        while q:
            # The rightmost node for the current level is the last node in the queue
            # rightmost = q[-1]
            result.append(q[-1].val)
            
            for _ in range(len(q)):
                node = q.popleft()
                q.append(node.left) if node.left else None
                q.append(node.right) if node.right else None

        return result