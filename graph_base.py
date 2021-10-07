"""
    Classes for directed weighted graph.
"""

class Node():

    def __init__(self, key: int) -> None:
        self.key = key


class Edge():

    def __init__(self, fro: Node, to: Node, weight: int):
        self.fro = fro
        self.to = to
        self.weight = weight


class Graph():

    def __init__(self):
        self.vertex = {}
        self.edge = []

    def add_vertex(self, key: int) -> None:
        if key not in self.vertex:
            self.vertex[key] = Node(key)
        else:
            print("Key already in graph")

    def add_edge(self, fro: int, to: int, weight: int) -> None:
        
        if fro in self.vertex and to in self.vertex: 
            self.edge.append(
                Edge(self.vertex[fro], self.vertex[to], weight)
            )
        else:
            print("Key not in graph")

    def debug(self):

        print("Vertex:")
        for key in self.vertex:
            print(key)
        print()

        print("Edge:")
        for e in self.edge:
            print("From:", e.fro.key, " To:", e.to.key, " Weight:", e.weight)


def main():

    G = Graph()
    G.add_vertex(key=0)
    G.add_vertex(key=1)
    G.add_edge(fro=0, to=1, weight=1)
    G.debug()

if __name__ == "__main__":
    main()
