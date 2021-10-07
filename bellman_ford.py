import math

"""
    Graph is represented as an adjacency matrix:
        G = [
            [0, -5, 6],
            [-5, 0, inf],
            [6, inf, 0]
        ]
    inf represent no path to vertex.
"""

def bellman_ford(G: list[list[int]], s: int) -> tuple[list[int], list[int]]:
    
    dist = [math.inf]*len(G)
    pred = [None]*len(G)

    dist[s] = 0 # assuming no negative cycle


    return (dist, pred)


def main():

    G = [
        [0, -5, 6],
        [-5, 0, math.inf],
        [6, math.inf, 0]
    ]

    (dist, pred) = bellman_ford(G, 0)
    print(dist)

if __name__ == "__main__":
    main()
