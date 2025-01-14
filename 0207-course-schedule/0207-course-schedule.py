class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # use a hashmap?
        # this is a graph problem imo, setup the graph and if it's cyclic then it cannot be completed. else it can
        
        # adjacency list
        # ingress array
        
        adj = [[] for _ in range(numCourses)]
        indeg = [0] * numCourses
        # setup adj
        for p in prerequisites:
            adj[p[1]].append(p[0])
            indeg[p[0]] += 1
        
        queue = []
        for i in range(numCourses):
            if indeg[i] == 0: queue.append(i)
        
        visited = 0
        while queue:
            node = queue.pop(0)
            visited += 1
            for nei in adj[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    queue.append(nei)
        
        return visited == numCourses
