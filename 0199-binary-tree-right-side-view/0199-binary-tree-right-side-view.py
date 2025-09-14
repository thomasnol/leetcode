# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        zhello bros. yeah this is an interesting question 
        
        basically we only prioritize (?) the right more node. 
        
        WAIT, BRO 
        
        we can just do a level wise bfs and just pick the last node of that node
        
        do it like a level 
        
        [1]
        [2,3]
        [null, 5, null, 4]    
        
        bfs uses a queue not recursion  
        
        visited is not needed since its doing down  
        
        lets print this. theres no queue in pyhton, 
        
        dequeue is more optimized than pop(0) for array. 
        
        wait lets try that
        
        yeah. 
        
        thats just a deque
        
        yeah that would work 
        
        it would have been easier to visualize with levels
        
        whats the test case?
        [0,1,2,null,3,4,null,null,5,9,null,null,6,10,null]
        """
        if not root:
            return []
        queue = deque([root])
        levels = []
        
        while queue:
            s = len(queue)
            # level = []
            last_val = root.val
            
            # this is a level wise bfs. 
    
            for _ in range(s):
                node = queue.popleft()
                last_val = node.val
                # level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # if level:
            if last_val is not None:
                # levels.append(level[-1])
                levels.append(last_val)
            
        return levels