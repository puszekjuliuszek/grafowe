from queue import PriorityQueue
from math import inf
from dimacs import *

class Vertex():
    def __init__(self):
        self.neighbours = []
        self.d = None


def dijkstra_modified(G, start, end):
    Q = PriorityQueue()
    Q.put((inf, start))

    while G[end].d is None and not Q.empty():
        c, v = Q.get()
        if G[v].d == None:
            G[v].d = abs(c)
            for u, c in G[v].neighbours:
                Q.put((max((-1) * G[v].d, (-1) * abs(c)), u))

    return G[end].d


def make_graph(E, V):
    G = [Vertex() for _ in range(V)]
    for (x, y, c) in E:
        G[x-1].neighbours.append([y - 1, c])
        G[y-1].neighbours.append([x - 1, c])

    return G

if __name__== "__main__":
    V,E = loadWeightedGraph("test_grapghs/clique100")
    G = make_graph(E,V)
    print(dijkstra_modified(G,0,1))
