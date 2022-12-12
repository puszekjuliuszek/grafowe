from dimacs import *


class Node:
    def __init__(self):
        self.edges = {}  # słownik  mapujący wierzchołki do których są krawędzie na ich wagi
        self.active = True
        self.made_of = []

    def addEdge(self, to, weight):
        self.edges[to] = self.edges.get(to, 0) + weight  # dodaj krawędź do zadanego wierzchołka
        # o zadanej wadze; a jeśli taka krawędź
        # istnieje, to dodaj do niej wagę

    def delEdge(self, to):
        del self.edges[to]  # usuń krawędź do zadanego wierzchołka


def make_graph(V, L):
    G = [Node() for _ in range(V)]

    for (x, y, c) in L:
        G[x - 1].addEdge(y - 1, c)
        G[y - 1].addEdge(x - 1, c)
    return G


def print_graph(G):
    for i in range(0, len(G)):
        if G[i].active:
            if len(G[i].made_of) == 0:
                print("Wierzchołek " + str(i + 1) + " ma sąsiada:")
            else:
                # made_of_vertexes = str(i) + ", " for i in G[i].made_of
                print("Wierzchołek " + str(i + 1) + " zrobiony z" + " ma sąsiada:")
            for neighbour in G[i].edges.keys():
                print("    " + str(neighbour + 1) + " z wagą " + str(G[i].edges[neighbour]))


def mergeVertices(G, x, y):
    G.append(Node())
    for neighbour in G[y - 1].edges.keys():
        if neighbour not in G[-1].edges and neighbour != x - 1:
            G[-1].addEdge(neighbour, G[y - 1].edges[neighbour])
    for neighbour in G[x - 1].edges.keys():
        if neighbour not in G[-1].edges and neighbour != y - 1:
            G[-1].addEdge(neighbour, G[x - 1].edges[neighbour])

    G[x - 1].active = False
    G[y - 1].active = False
    G[-1].made_of.append(x - 1)
    G[-1].made_of.append(y - 1)


def how_many_vrtex(G):
    pass


def minimumCutPhase(G):
    a = 0  # może to zawsze być wierzchołek numer 1 (lub 0 po przenumerowaniu)
    S = {a}
    n = how_many_vrtex(G)

    while len(S) < n:
        for i in range(len(G)):
            if i not in S:

        znajdz
        taki
        wierzcholek
        v, ze
        suma
        wag
        krawedzi
        z
        v
        do
        wierzcholkow
        w
        S
        jest
        maksymal

        dolacz
        v
        do
        S(zapamietujac
        kolejnosc
        dodawania)

        s = ostatni
        wierzcholek
        dodany
        do
        S
        t = przedostatni
        wierzcholek
        dodany
        do
        S

        # tworzone przecięcie jest postaci S = {s}, T = V - {s}
        zapamietaj
        sume
        wag
        krawedzi
        wychodzacych
        z
        s
        jako
        potencjalny_wynik

        mergeVertices(G, s, t)

        return potencjalny_wynik

    if __name__ == '__main__':
        V, E = loadWeightedGraph('graphs/cycle')
        G = make_graph(V, E)
        mergeVertices(G, 1, 2)
        print_graph(G)
