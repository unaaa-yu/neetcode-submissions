# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        node1 = head
        node2 = head.next
        while node1 and node2:
            if node1 == node2:
                return True
            node1 = node1.next
            if not node2.next:
                break
            node2 = node2.next.next
        return False

        