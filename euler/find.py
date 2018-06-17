from check import check

import copy

def find_cycle(graph, queue = [0], cycle = []):
    while queue:
        vertex = queue.pop(-1)

        for n in range(len(graph)):
            if graph[vertex][n] == 1:
                queue.append(n)
                graph[vertex][n] = 0
                graph[n][vertex] = 0
                find_cycle(graph, queue, cycle)

        cycle.append(vertex)
    
    return cycle
