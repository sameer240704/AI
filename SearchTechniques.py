# BFS
def BFS_Traversal(adjList, startNode, visited):
    queue = []
    
    visited[startNode] = True
    queue.append(startNode)
    
    while queue:
        currentNode = queue.pop(0)
        print(currentNode, end=" ")
        
        for neighbor in adjList[currentNode]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

def addEdge(adjList, u, v):
    adjList[u].append(v)

def main():
    vertices = int(input("Enter the number of vertices in the graph: "))
    
    adjList = [[] for _ in range(vertices)]
    
    edges = int(input("Enter the number of edges in the graph: "))
    
    print("Enter the edges in the formal 'u, v', where u and v are the vertices connected by the edges: ")
    for _ in range(edges):
        u, v = map(int, input().split())
        addEdge(adjList, u, v)
        
    visited = [False] * vertices
        
    startNode = int(input("Enter the starting node for BFS Traversal in the graph: "))
    BFS_Traversal(adjList, startNode, visited)

if __name__ == "__main__":
    main()


#DFS
class Graph:
    def __init__(self):
        self.graph = {}
    
    def addEdge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
        
    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v, end=" ")
        
        for neighbor in self.graph.get(v, []):
            if neighbor not in visited:
                self.DFSUtil(neighbor, visited)
                
    def DFS(self, v):
        visited = set()
        self.DFSUtil(v, visited)

if __name__ == "__main__":
    g = Graph()
    
    edges = int(input("Enter the number of edges in the graph: "))
    
    print("Enter the edges in format 'u, v', where u and v are vertices connected by an edge: ")
    for i in range(edges):
        u, v = map(int, input().split())
        g.addEdge(u, v)
    
    startVertex = int(input("Enter the starting vertex for DFS Traversal: "))
    
    print(f"DFS Traversal starting from vertex {startVertex} is: ")
    g.DFS(startVertex)


# IDDFS
class Graph: 
    def __init__(self,vertices):
        self.V = vertices
        self.graph = {}
        for i in range(self.V):
            self.graph[i] = []

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def DLS(self,src,target,maxDepth):
        if src == target : 
            return True, 0  
    
        if maxDepth <= 0 : 
            return False, 0 

        for i in self.graph[src]:
            found, depth = self.DLS(i,target,maxDepth-1)
            if found:
                return True, depth + 1  
        return False, 0

    def IDDFS(self,src, target, maxDepth):
        for i in range(maxDepth):
            found, depth = self.DLS(src, target, i)
            if found:
                return True, depth  
        return False, 0

def createGraph():
    vertices = int(input("Enter the number of vertices in the graph: "))
    g = Graph(vertices)
    edges = int(input("Enter the number of edges: "))
    print("Enter edges in the format 'u v', where u and v are vertices connected by an edge:")
    for _ in range(edges):
        u, v = map(int, input().split())
        g.addEdge(u, v)
    return g
 
if __name__ == "__main__":
    g = createGraph()
 
    target = int(input("Enter the target vertex: "))
    maxDepth = int(input("Enter the maximum depth: "))
    src = int(input("Enter the source vertex: "))
     
    print("IDDFS")
    found, depth = g.IDDFS(src, target, maxDepth)
    if found:
        print("Target is reachable from source within max depth at depth:", depth)
    else:
        print("Target is NOT reachable from source within max depth")


# GREEDY BEST FIRST SEARCH
'''
graph = {
    'A': [('B', 1), ('C', 2), ('D', 3)],
    'B': [('E', 4)],
    'C': [('F', 5), ('E', 6)],
    'D': [('F', 7)],
    'E': [('G', 8)],
    'F': [('G', 9)],
    'G': []
}

heuristic = {
    'A': 40,
    'B': 32,
    'C': 25,
    'D': 35,
    'E': 19,
    'F': 17,
    'G': 0
}
'''

import heapq

def get_graph():
    graph = {}
    num_edges = int(input("Enter the number of edges: "))
    print("Enter the edges in the format 'node1 node2 cost':")
    for _ in range(num_edges):
        u, v, cost = input().split()
        cost = int(cost)
        if u in graph:
            graph[u].append((v, cost))
        else:
            graph[u] = [(v, cost)]
        if v not in graph:
            graph[v] = []
    return graph

def get_heuristic():
    heuristic = {}
    num_nodes = int(input("Enter the number of nodes: "))
    print("Enter the heuristic values in the format 'node heuristic':")
    for _ in range(num_nodes):
        node, h = input().split()
        h = int(h)
        heuristic[node] = h
    return heuristic

def greedy_best_first_search(graph, heuristic, start, goal):
    pq = []
    heapq.heappush(pq, (heuristic[start], start))
    visited = set()
    parent = {start: None}

    while pq:
        _, current = heapq.heappop(pq)
        
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path
        
        visited.add(current)

        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                heapq.heappush(pq, (heuristic[neighbor], neighbor))
                parent[neighbor] = current

    return None

def main():
    graph = get_graph()
    heuristic = get_heuristic()
    start = input("Enter the start node: ")
    goal = input("Enter the goal node: ")
    
    path = greedy_best_first_search(graph, heuristic, start, goal)

    if path:
        print("Path found:", " -> ".join(path))
    else:
        print("No path found")

if __name__ == "__main__":
    main()