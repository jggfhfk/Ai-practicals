def create_graph():
    graph = {}
    print("Enter the number of edges:")
    num_edges = int(input())
    print("Enter the edges of the graph in the format 'node: [adjacent_nodes]':")
    for _ in range(num_edges):
        edge = input().strip()
        node, adjacent_nodes = edge.split(':')
        node = node.strip()
        adjacent_nodes = [adj.strip() for adj in adjacent_nodes.split(',')]
        graph[node] = adjacent_nodes
    return graph

# --------------------------BFS----------------------------
def bfs(graph, start_node):
    visited = []
    queue = [start_node]
    
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node, end=" ")
            visited.append(node)
            queue.extend(graph[node])

print("BFS:")
graph = create_graph()
start_node = input("Enter the starting node for BFS: ")
bfs(graph, start_node)
print()

# --------------------------DFS----------------------------
def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

print("DFS:")
graph = create_graph()
start_node = input("Enter the starting node for DFS: ")
dfs(graph, start_node, set())
print()
