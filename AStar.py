def aStarAlgo(start_node, stop_node):
    open_set = set([start_node])  # Fix: Initialize open_set as a set with start_node
    closed_set = set()
    g = {start_node: 0}  # Initialize g with the distance from start_node
    parents = {start_node: start_node}  # Initialize parents with the start_node itself as parent
    while len(open_set) > 0:
        n = None
        for v in open_set:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v
        if n == stop_node or Graph_nodes[n] is None:
            pass
        else:
            for (m, weight) in get_neighbors(n):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)
        if n is None:
            print('Path does not exist!')
            return None
        
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            distance = g[stop_node]  # Calculate the distance of the path
            print(f'Path found: {path}')
            print(f'Distance: {distance}')
            return path, distance
        open_set.remove(n)
        closed_set.add(n)
    print('Path does not exist!')
    return None, None

#define fuction to return neighbor and its distance
#from the passed node
def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None
    
def heuristic(n):
    H_dist = {
        'A': 10.1,
        'B': 5.8,
        'C': 3.4,
        'D': 9.2,
        'E': 7.1,
        'F': 3.5,
        'G': 0,
        'S': 11.5,
    }
    return H_dist[n]

Graph_nodes = {
    'A': [('S', 3), ('B', 4), ('D', 5)],
    'B': [('A', 4), ('C', 4), ('E', 5)],
    'C': [('B', 4)],
    'D': [('A', 5), ('S', 4), ('E', 2)],
    'E': [('D', 2), ('F', 4), ('B', 5)],
    'F': [('E', 4), ('G', 3.5)],
    'G': [('F', 3.5)],
    'S': [('A', 3), ('D', 4)],
}

path, distance = aStarAlgo('C', 'G')