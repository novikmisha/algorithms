def bfs(graph, start = 0):
    visited, queue = [], [start]

    while queue:
        vertex = queue.pop(0)

        if vertex not in visited:
            visited.append(vertex)

            for i in range(vertex + 1, len(graph)):
                if graph[vertex][i] == 1:
                    queue.append(i)

    return visited


def is_connected(graph):
    return len(graph) == len(bfs(graph))
