# Juliusz Wasieleski
from dimacs import *
from collections import deque


def make_graph(n, edges):
    graph = [[0 for _ in range(n)] for _ in range(n)]
    flow = [[0 for _ in range(n)] for _ in range(n)]
    for k in edges:
        graph[k[0] - 1][k[1] - 1] = k[2]
    return graph, flow


def find_path(parent, t):
    stack = [t]
    path = []
    while len(stack) > 0:
        v = stack.pop()
        path.append(v)
        if parent[v] is not None:
            stack.append(parent[v])
    return path


def bfs(G, Flow, s, t):
    parent = [None for _ in range(len(G))]
    visited = [False for _ in range(len(G))]
    que = deque()
    que.append(s)
    while que:
        u = que.popleft()
        for v in range(len(G)):
            if G[u][v] - Flow[u][v] > 0 and not visited[v]:
                parent[v] = u
                visited[v] = True
                if v == t:
                    return find_path(parent, t)
                que.append(v)
    return None


def dfs_visit(G, flow, s, t):
    n = len(G)
    visited = [False for _ in range(n)]
    parents = [None for _ in range(n)]
    stack = [s]
    visited[s] = True
    while len(stack) > 0:
        u = stack.pop()
        visited[u] = True
        for v in range(n):
            if not visited[v] and G[u][v] - flow[u][v] > 0:
                parents[v] = u
                if v == t:
                    return find_path(parents, t)
                stack.append(v)
    return None


def Edmonds_Karp(G, Flow, s, t):
    n = len(G)
    path = dfs_visit(G, Flow, s, t)
    while path != None:
        flow = min(G[path[i]][path[i - 1]] - Flow[path[i]][path[i - 1]] for i in range(len(path) - 1, 0, -1))
        print(flow)
        for i in range(len(path) - 1, 0, -1):
            Flow[path[i]][path[i - 1]] += flow
        path = bfs(G, Flow, s, t)
    return sum(Flow[s][i] for i in range(n))


if __name__ == "__main__":
    V, L = loadDirectedWeightedGraph("flow/simple")
    graph, flow = make_graph(V, L)
    print(Edmonds_Karp(graph, flow, 0, V - 1))
