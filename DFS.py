def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        if node in graph:
            for neighbour in graph[node]:
                dfs(visited, graph, neighbour)


def main():
    visited = set()

    n = int(input("Enter number of nodes: "))
    graph = dict()

    for i in range(1, n + 1):
        edges = int(input(f"Enter number of edges for node {i}: "))
        graph[i] = []

        for j in range(1, edges + 1):
            node = int(input(f"Enter edge {j} for node {i}: "))
            graph[i].append(node)

    print("DFS Traversal:")
    dfs(visited, graph, 1)


if __name__ == "__main__":
    main()
    

# Time Complexity of DFS:
# Best Case  : O(V + E)
# Worst Case : O(V + E)

# Space Complexity of DFS:
# Best Case  : O(V)
# Worst Case : O(V)

# DFS uses Stack / Recursion.
# Every vertex and edge is visited once.
# Hence complexity is O(V + E).

# For Undirected Graph:
# Each edge is visited twice in adjacency list
# but overall complexity remains O(V + E).