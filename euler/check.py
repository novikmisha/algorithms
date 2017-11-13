from bfs import is_connected

def check(graph):
    if is_connected(graph):
        for row in graph:
            if sum(row) % 2 == 1:
                return False

        return True

    return False
