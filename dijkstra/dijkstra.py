def dijkstra(graph):
    lens, queue = dict(), [0]
    lens[0] = 0

    while queue:
        vertex = queue.pop()

        for n in range(len(graph)):
            if graph[vertex][n] > 0:
                if n in lens and lens[n] > lens[vertex] + graph[vertex][n]:
                    queue.remove(n)
                    lens[n] = lens[vertex] + graph[vertex][n]
                else:
                    lens[n] = lens[vertex] + graph[vertex][n]

                for i in range(len(queue)):
                    if lens[queue[i]] < lens[n]:
                        queue.insert(i, n)

                if n not in queue:
                    queue.append(n)

    return lens


if __name__ == "__main__":
    graph = [[0, 1, 1, 0, 0, 0, 0],
             [0, 0, 0, 2, 0, 3, 0],
             [0, 0, 0, 4, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0, 5],
             [0, 0, 0, 0, 0, 0, 2],
             [0, 0, 0, 0, 0, 0, 0]];

    print(dijkstra(graph))
