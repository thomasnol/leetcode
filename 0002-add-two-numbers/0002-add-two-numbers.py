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
        while l1 or l2 or remainder == 1:
            newval = 0
            if l1:
                val1 = l1.val
                l1 = l1.next
                newval += val1
            if l2:
                val2 = l2.val
                l2 = l2.next
                newval += val2
            newval += remainder
            if newval >= 10:
                remainder = 1
                newval -= 10
            else:
                remainder = 0
            newnode = ListNode(newval)
            pointer.next = newnode
            pointer = pointer.next

        return root.next