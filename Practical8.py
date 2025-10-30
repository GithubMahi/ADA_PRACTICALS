def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}

print("DFS:")
dfs(graph, 0)
