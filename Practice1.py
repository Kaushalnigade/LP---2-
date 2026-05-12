def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        if node in graph:
            for neighbour in graph[node]:
                dfs(visited, graph, neighbour)


def bfs(visited, graph, node, queue):
    visited.add(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


def main():
    visited1 = set()  # For DFS
    visited2 = set()  # For BFS
    queue = []        # For BFS

    n = int(input("Enter number of nodes: "))
    graph = dict()

    for i in range(1, n + 1):
        edges = int(input(f"Enter number of edges for node {i}: "))
        graph[i] = []

        for j in range(1, edges + 1):
            node = int(input(f"Enter edge {j} for node {i}: "))
            graph[i].append(node)

    print("The following is DFS:")
    dfs(visited1, graph, 1)

    print("\nThe following is BFS:")
    bfs(visited2, graph, 1, queue)


if __name__ == "__main__":
    main()


# Breadth First Search (BFS) for Undirected Graph
# Time Complexity:
# Best Case  : O(V + E) 
# Worst Case : O(V + E)

# Explanation:
# In BFS:
# - Every vertex is visited exactly once.
# - Every edge is explored exactly once.


# Space Complexity:
# Best Case  : O(V)
# Worst Case : O(V)


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