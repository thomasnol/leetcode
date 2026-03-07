# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # we could run through both binary trees, collect all the leaves into arrays, then compare the 2 arrays
        # to do this we'll do an iterative depth first search?
        # we could also try to do a post-order traversal but I don't think that would work
        arr1 = []
        arr2 = []
        stack = [root1]
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                arr1.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        stack = [root2]
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                arr2.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return arr1 == arr2