import sys
from collections import defaultdict

class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append(Edge(u, v, w))

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        rootx = self.find(parent, x)
        rooty = self.find(parent, y)

        if rank[rootx] < rank[rooty]:
            parent[rootx] = rooty
        elif rank[rootx] > rank[rooty]:
            parent[rooty] = rootx
        else:
            parent[rooty] = rootx
            rank[rootx] += 1

    def KruskalMST(self):
        result =[]
        i, e = 0, 0
        self.edges = sorted(self.edges, key=lambda edge: edge.weight)

        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        
        while e < self.V -1 :
            u, v, w = self.edges[i].source, self.edges[i].destination, self.edges[i].weight
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1    
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        print("Following are the edges in the constructed MST")
        for u, v, weight in result:
            print("%d - %d: %d" % (u, v, weight))

g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

g.KruskalMST()

------------------------------------------
// output: Following are the edges in the constructed MST
2 - 3: 4
0 - 3: 5
0 - 1: 10


//This output represents the edges in the minimum spanning tree, which has been found using Kruskal's algorithm.
The edges are sorted by their weights, and the union-find algorithm is used to check for cycles in the graph.
If a cycle is not detected, the edge is added to the result.




