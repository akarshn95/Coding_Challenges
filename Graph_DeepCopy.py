class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        
        new_graph=Node(node.val)
        queue=[node]
        visited={}
        
        visited[node]=new_graph
        
        while queue:
            
            current_node=queue.pop(0)
            
            for n in current_node.neighbors:
                if n not in visited:
                    visited[n]=Node(n.val)
                    queue.append(n)
                visited[current_node].neighbors.append(visited[n])
        
        return new_graph
