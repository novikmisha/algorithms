from bfs import is_connected
from check import check
from find import find_cycle

if __name__ == "__main__":
    graph = [[0, 1, 0, 0, 1, 0],
             [1, 0, 1, 1, 0, 1],
             [0, 1, 0, 1, 1, 1],
             [0, 1, 1, 0, 1, 1],
             [1, 0, 1, 1, 0, 1],
             [0, 1, 1, 1, 1, 0]]

    another_graph = \
            [[0, 1, 0, 0, 1, 0, 0],
             [1, 0, 1, 1, 0, 1, 0],
             [0, 1, 0, 1, 1, 1, 0],
             [0, 1, 1, 0, 1, 1, 0],
             [1, 0, 1, 1, 0, 1, 0],
             [0, 1, 1, 1, 1, 0, 0],
             [0, 0, 0, 0, 0, 0, 0]]

    third_graph = \
            [[0, 1, 0, 0, 1],
             [1, 0, 1, 0, 0],
             [0, 1, 0, 1, 0],
             [0, 0, 1, 0, 1],
             [1, 0, 0, 1, 0]]
    
    print(is_connected(graph))
    print(is_connected(another_graph))

    print(check(graph))
    print(check(another_graph))

    print(find_cycle(graph))
    print(find_cycle(third_graph, queue = [0], cycle = []))
