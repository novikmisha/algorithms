def dfs(vertex, matching, used):
    if used[vertex]:
        return False

    used[vertex] = True

    for to in graph[vertex]:
        if matching[to] is -1 or dfs(matching[to], matching, used):
            matching[to] = vertex
            return True

    return False


def fill(value, size):
    array = []

    for i in range(0, size):
        array.append(value)

    return array


if __name__ == "__main__":
    graph = [[4, 7],
             [4, 5],
             [6, 7],
             [5],
             [0, 1],
             [1, 3],
             [2],
             [0, 2]]

    matching = []
    used = []

    N = 8

    matching = fill(-1, N)

    for i in range(0, N):
        used = fill(False, N)
        dfs(i, matching, used)

    for i in range(0, N):
        if matching[i] is not -1:
            print("{} {}".format(i, matching[i]))


