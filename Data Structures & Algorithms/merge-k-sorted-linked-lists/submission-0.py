from heapq import heappush, heappop
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class NodeWrapper:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0: return None
        res = ListNode(0)
        curr = res
        minHeap = []

        for l in lists:
            if l:
                heappush(minHeap, NodeWrapper(l))

        while minHeap:
            smallest = heappop(minHeap)
            curr.next = smallest.node
            curr = curr.next

            if smallest.node.next:
                heappush(minHeap, NodeWrapper(smallest.node.next))
        
        return res.next
