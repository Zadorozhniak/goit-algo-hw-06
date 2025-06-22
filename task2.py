from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
    
    def dfs(self, start, end, path=None, visited=None):
        if path is None:
            path = []
        if visited is None:
            visited = set()
        
        path.append(start)
        visited.add(start)
        
        if start == end:
            return path
        
        for neighbor in self.graph.get(start, []):
            if neighbor not in visited:
                result = self.dfs(neighbor, end, path.copy(), visited.copy())
                if result is not None:
                    return result
        return None
    
    def bfs(self, start, end):
        queue = deque()
        queue.append([start])
        visited = set()
        visited.add(start)
        
        while queue:
            path = queue.popleft()
            node = path[-1]
            
            if node == end:
                return path
            
            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
                    visited.add(neighbor)
        return None

# Створення графа з першого завдання
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('B', 'E')
g.add_edge('C', 'F')
g.add_edge('D', 'G')
g.add_edge('E', 'G')
g.add_edge('F', 'G')

# Пошук шляху від A до G
start = 'A'
end = 'G'

dfs_path = g.dfs(start, end)
bfs_path = g.bfs(start, end)

print(f"DFS шлях: {dfs_path}")
print(f"BFS шлях: {bfs_path}")