# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # find out which l is larger, if any
        # enter the extra nodes
        # once lengths are equal
        # while l1 and l2 haven't hit end yet
        # add the values of both nodes plus past remainder, create remainder if needed
        # create a node with the value

        root = ListNode(0)
        pointer = root
        remainder = 0
        while l1 or l2 or remainder:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            newval = val1 + val2 + remainder 
            remainder = newval // 10
            newval = newval % 10
            pointer.next = ListNode(newval)
            pointer = pointer.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return root.next