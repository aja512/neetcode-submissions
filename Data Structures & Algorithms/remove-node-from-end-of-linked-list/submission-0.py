# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodeCount = 0
        ptr = head

        while ptr:
            nodeCount += 1
            ptr = ptr.next
        
        removeIndex = nodeCount - n
        if removeIndex == 0:
            return head.next

        ptr = head
        for i in range(nodeCount - 1):
            if i + 1 == removeIndex:
                ptr.next = ptr.next.next
            ptr = ptr.next
        
        return head
