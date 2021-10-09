from data_structure import PriorityQueue
from math import inf, isinf

"""
    G is an adjacency matrix, s is the "source node" of the MST
"""
def prim(G: list[list[int]], s: int) -> list[int]:

    dist = [inf]*len(G)     # distance of nodes from s, dist[x] = inf means no path from s to x
    dist[s] = 0
    pred = [None]*len(G)    # pred[x] = y -> pred of x is y

    Q = PriorityQueue()         # Init Q with distance from s to every other vertex
    for i in range(len(G[s])):
        Q.insert(i, G[s][i])

    T = []
    while not Q.is_empty():
        u = Q.pop()
        T.append(u)
        for i in range(len(G[u])):
            if not isinf(G[u][i]) and u != i:  # i is neighbour of u
                if not i in T and G[u][i] < dist[i]:   # if s->u->i is quicker than s->i
                    dist[i] = G[u][i]   # dist = |s->u->i|
                    pred[i] = u         # u -> i
                    Q.update(i, dist[i])  # update the dist in Q
    
    return pred


if __name__ == "__main__":
    G = [
        [0, 10, 5, inf, inf],
        [10, 0, 3, 1, inf],
        [5, 3, 0, 9, 2],
        [inf, 1, 9, 0, 6],
        [inf, inf, 2, 6, 0]
    ]

    print(prim(G, 1))
