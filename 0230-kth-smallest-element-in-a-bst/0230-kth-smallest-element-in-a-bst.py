# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        to_exp = []
        # to_exp.append(root)
        node = root
        while node or to_exp:
            while node:
                to_exp.append(node)
                node = node.left
            node = to_exp.pop()
            k -= 1
            if k == 0:
                return node.val
            node = node.right


# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         to_exp = []
#         node = root
#         while node or to_exp:
#             while node:
#                 to_exp.append(node)
#                 node = node.left
#             node = to_exp.pop()
#             k -= 1
#             if k == 0:
#                 return node.val
#             node = node.right
