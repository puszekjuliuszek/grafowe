from dimacs import *
from collections import deque

def bfs(G, t):
    parent = [None for _ in range(V)]
    visited = [0 for _ in range(V)]
    ans = []
    minimum = float("inf")
    q = deque()
    q.append(0)
    while(q):
        vertex=q.popleft()
        if(vertex==t):
            break
        for i in range(V):
            if(G[vertex][i]!=None and visited[i]==0 and G[vertex][i]>0):
                q.append(i)
                parent[i]=vertex
                visited[i]=1
    iter=t
    if(parent[iter]==None):
        return None,None
    while(True):
        if(iter==0):
            new = ans[::-1]
            return new,minimum
        minimum = min(minimum,G[parent[iter]][iter])
        ans.append(iter)
        iter=parent[iter]



def edmonds_karp(V, L, last):
    G = [[None for _ in range(V)] for _ in range(V)]
    Residudal = [[None for _ in range(V)] for _ in range(V)]
    for i in range(len(L)):
        x=L[i][0]-1
        y=L[i][1]-1
        G[x][y]=1
        G[y][x]=1
        Residudal[y][x]=0
        Residudal[x][y]=0
    while(True):
        path,flow = bfs(G, last)
        vertex=0
        if(path==None):
            break
        else:
            for i in range(len(path)):
                G[vertex][path[i]]-=flow
                Residudal[path[i]][vertex]+=flow
                vertex=path[i]
    endflow=0
    for i in range(V):
        if(Residudal[i][0]!=None):
            endflow+=Residudal[i][0]
    return endflow

if __name__ == '__main__':
    V, E = loadWeightedGraph('graphs/clique200')
    edges_amount=float('inf')
    for i in range(1,V):
        edges_amount = min(edges_amount, edmonds_karp(V, E, i))
    print(edges_amount)

