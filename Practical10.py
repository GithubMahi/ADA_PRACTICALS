def prim_mst(graph):
    n = len(graph)
    selected = [False] * n
    key = [999999] * n
    parent = [-1] * n

    key[0] = 0

    for _ in range(n - 1):
        min_key = 999999
        u = -1
        for v in range(n):
            if not selected[v] and key[v] < min_key:
                min_key = key[v]
                u = v

        selected[u] = True

        for v in range(n):
            if graph[u][v] != 0 and not selected[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u

    print("Edge\tWeight")
    total_cost = 0
    for i in range(1, n):
        print(f"{parent[i]} - {i}\t{graph[i][parent[i]]}")
        total_cost += graph[i][parent[i]]

    print("Total cost of MST =", total_cost)


if __name__ == "__main__":
    graph = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0]
    ]

    print("Prim's Minimum Spanning Tree:")
    prim_mst(graph)
