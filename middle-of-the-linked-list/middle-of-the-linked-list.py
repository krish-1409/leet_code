# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        while head.next!=None :
            slow = slow.next
            head = head.next.next
            if not head:
                break
        return slow
        