# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second = slow.next
        prev = slow.next = None

        while second:
            tmp = second.next
            second.next = prev
            prev, second = second, tmp
        
        curr, second = head, prev

        while second:
            tmp1, tmp2 = curr.next, second.next
            curr.next, second.next = second, tmp1
            curr, second = tmp1, tmp2
        



            