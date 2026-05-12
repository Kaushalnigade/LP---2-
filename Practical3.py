def find(parent, i):

    if parent[i] != i:
        parent[i] = find(parent, parent[i])

    return parent[i]


def union(parent, x, y):

    parent[x] = y


def kruskal(v, edges):

    edges.sort(key=lambda x: x[2])

    max_vertex = max(max(src, dst) for src, dst, _ in edges) if edges else v - 1

    parent = list(range(max(v, max_vertex + 1)))

    result = []
    cost = 0

    for src, dst, w in edges:

        root_u = find(parent, src)
        root_v = find(parent, dst)

        if root_u != root_v:

            result.append((src, dst, w))
            cost += w

            union(parent, root_u, root_v)

    print("\nEdges in Minimum Spanning Tree:")

    for u, v, w in result:
        print(f"{u} -- {v} == {w}")

    print(f"Minimum Cost = {cost}")


vertices = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []

print("Enter edges (u v weight):")

for _ in range(e):

    u, v, w = map(int, input().split())

    edges.append([u, v, w])

kruskal(vertices, edges)



#Krushkal's Algo 
#Time Complexity :- 
#Best Case = O(E logE)
#Worst Case = O(E logE)

#Space Complexity 
# best case and worst case = O(V+E)




#Prim's Algo 
#Time Complexity and Space Complexity Using Adjacency Matrix
#Best Case	O(V²)
#Worst Case	O(V²)


#Time Complexity and Space Complexity  Using Priority Queue + Adjacency List
#Best Case	O(E log V)
#Worst Case	O(E log V)