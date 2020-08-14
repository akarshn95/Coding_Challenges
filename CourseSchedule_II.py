class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        WHITE = 1   # unvisited
        GREY = 2    # current DFS     
        BLACK = 3   # DFS complete
        
        adj_list = defaultdict(list)
        
        for des,src in prerequisites:
            adj_list[src].append(des)
            
        res = []
        is_possible = True
        
        # make all white to start with
        color = {k:WHITE for k in range(numCourses)}
        
        def dfs(node):
            nonlocal is_possible
            
            if not is_possible:
                return
            
            color[node] = GREY
            
            for neigh in adj_list[node]:
                if color[neigh] == WHITE:
                    dfs(neigh)
                # forms a cycle and hence not possible
                elif color[neigh] == GREY:
                    is_possible = False
            
            color[node] = BLACK
            res.append(node)
            
        for vertex in range(numCourses):
            if color[vertex] == WHITE:
                dfs(vertex)
                
        
        return res[::-1] if is_possible else []
