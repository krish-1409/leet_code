# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow,fast = head,head
        if not head:
            return None
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                slow = head
                break
        if slow!=head or not slow.next:   #second condition is to handle a single node.
            return None
        while slow!=fast:
            fast = fast.next
            slow = slow.next
        return slow