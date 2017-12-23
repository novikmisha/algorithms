from edge import Edge
from insert import insert_sort


def kruskal(edges):
    edges, vertexes = insert_sort(edges, dict())

    graph_size = len(vertexes.keys())
    graph = list()
    i = 0

    while len(graph) < graph_size - 1:
        edge = edges[i]
        i += 1

        if vertexes[edge.first] < 2 and vertexes[edge.second] < 2:
            vertexes[edge.first] += 1
            vertexes[edge.second] += 1
            graph.append(edge)

    return graph


if __name__ == "__main__":
    edges = list()
    edges.append(Edge(1, 'a', 'b'))
    edges.append(Edge(8, 'a', 'c'))
    edges.append(Edge(3, 'c', 'b'))
    edges.append(Edge(4, 'b', 'd'))
    edges.append(Edge(2, 'd', 'e'))
    edges.append(Edge(3, 'b', 'e'))
    edges.append(Edge(-1, 'c', 'd'))

    graph = kruskal(edges)
    for edge in graph:
        print("{} - {} {}".format(edge.value, edge.first, edge.second))
