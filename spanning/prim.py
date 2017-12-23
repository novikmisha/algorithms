import random
from math import inf

from edge import Edge
from insert import insert_sort


def prim(graph):
    result = []
    vertex = random.randint(0, len(graph) - 1)
    queue = set()
    queue.add(vertex)

    while len(result) < len(graph) - 1:
        min = inf
        vertex = None
        another = None

        for value in queue:
            for i in range(len(graph)):

                if graph[value][i] < min:
                    min = graph[value][i]
                    vertex = value
                    another = i
            ''' 
            if vertex is not value:
                queue.remove(value)
            '''
                    
        queue.add(another)
        result.append(Edge(graph[vertex][another], vertex, another))

        graph[vertex][another] = inf
        graph[another][vertex] = inf

    return result


if __name__ == "__main__":
    graph = [[inf, 1, inf, inf, 1, inf],
             [1, inf, 2, 3, inf, 1],
             [inf, 2, inf, 4, 2, 3],
             [inf, 3, 4, inf, 2, 3],
             [1, inf, 2, 2, inf, 3],
             [inf, 1, 3, 3, 3, inf]]

    graph = prim(graph)
    for edge in graph:
        print("{} - {} {}".format(edge.value, edge.first, edge.second))
