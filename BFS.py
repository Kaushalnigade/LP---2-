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
    visited = set()
    queue = []

    n = int(input("Enter number of nodes: "))
    graph = dict()

    for i in range(1, n + 1):
        edges = int(input(f"Enter number of edges for node {i}: "))
        graph[i] = []

        for j in range(1, edges + 1):
            node = int(input(f"Enter edge {j} for node {i}: "))
            graph[i].append(node)

    print("BFS Traversal:")
    bfs(visited, graph, 1, queue)


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