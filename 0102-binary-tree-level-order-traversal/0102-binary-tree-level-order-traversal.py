# import queue

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # iterative: iterate level by level through the tree, fill the queue with all nodes of next level, add any encountered nodes into the output.
        final = []
        queue = []
        if root is None: return []
        queue.append(root)
        while len(queue) > 0:
            row = []
            l = len(queue)
            for i in range(l):
                curNode = queue.pop(0)
                row.append(curNode.val)
                if (curNode.left): queue.append(curNode.left)
                if (curNode.right): queue.append(curNode.right)
            final.append(row)
        return final

        # res = []
        # # cLevel = queue.Queue(maxsize = 2000)
        # cLevel = []
        # # nLevel = queue.Queue(maxsize = 2000)
        # nLevel = []
        # if root is None: return []
        # cLevel.append(root)
        # while len(nLevel) > 0 or len(cLevel) > 0:
        #     if len(cLevel) > 0: res.append([])
        #     while len(cLevel) > 0:
        #         curNode = cLevel.pop()
        #         res[-1].append(curNode.val)
        #         # res.append(curNode.val)
        #         if (curNode.left): nLevel.append(curNode.left)
        #         if (curNode.right): nLevel.append(curNode.right)
        #     if len(nLevel) > 0: res.append([])
        #     while len(nLevel) > 0:
        #         curNode = nLevel.pop()
        #         res[-1].append(curNode.val)
        #         # res.append(curNode.val)
        #         if (curNode.left): cLevel.append(curNode.left)
        #         if (curNode.right): cLevel.append(curNode.right)
        # return res