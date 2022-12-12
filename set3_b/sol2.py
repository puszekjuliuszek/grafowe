import os
from dimacs import *
from queue import PriorityQueue
from math import inf


class Node:
    def __init__(self):
        self.edges = {}

    def add_edge(self, to, weight):
        self.edges[to] = self.edges.get(to, 0) + weight

    def del_edge(self, to):
        del self.edges[to]


def merge_vertices(graph, x, y):
    y_list = list(graph[y].edges.items())
    for vertex, weight in y_list:
        if vertex != x:
            graph[x].add_edge(vertex, weight)
            graph[vertex].add_edge(x, weight)
        graph[y].del_edge(vertex)
        graph[vertex].del_edge(y)


def minimum_cut_phase(graph, V):
    a = 1  # a = dowolny wierzcholek # może to zawsze być wierzchołek numer 1 (lub 0 po przenumerowaniu)
    S = []
    queue = PriorityQueue()
    queue.put((0, a))
    visited = [False] * (V + 1)
    weights = [0] * (V + 1)

    while not queue.empty():  # while S nie zawiera wszystkich wierzcholkow:
        v_weight, v = queue.get()  # znajdz taki wierzcholek v, ze suma wag krawedzi z v do wierzcholkow w S jest maksymalna
        if not visited[v]:
            S.append(v)  # dolacz v do S (zapamietujac kolejnosc dodawania)
            visited[v] = True
            for u, u_weight in graph[v].edges.items():
                if not visited[u]:
                    weights[u] += u_weight
                    queue.put((-weights[u], u))
    s = S[-1]  # s = ostatni wierzcholek dodany do S
    t = S[-2]  # t = przedostatni wierzcholek dodany do S
    result = 0
    for vertex, weight in graph[s].edges.items():
        result += weight
    merge_vertices(graph, t, s)
    return result


def make_graph(file_path):
    V, L = loadWeightedGraph(file_path)
    vertices = V
    graph = [Node() for _ in range(V + 1)]
    for vertex1, vertex2, weight in L:
        graph[vertex1].add_edge(vertex2, weight)
        graph[vertex2].add_edge(vertex1, weight)
    return vertices, V, graph


def stoer_wagner_algorithm(file_path):
    vertices, V, graph = make_graph(file_path)
    result = inf
    while vertices > 1:
        result = min(result, minimum_cut_phase(graph, V))
        vertices -= 1
    return result


directory = os.listdir("graphs")
for i in directory:
    # 'grid100x100' takes too long so i skip it
    # if i != "grid100x100":
    file_path = "Graphs/" + i
    result = stoer_wagner_algorithm(file_path)
    solution = int(readSolution(file_path))
    if result == solution:
        print(f"result {result} for {i}")
    else:
        print(f"result {result} for {i} answer is {solution}")
