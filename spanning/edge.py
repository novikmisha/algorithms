class Edge:

    def __init__(self, value, first, second):
        self.value = value
        self.first = first
        self.second = second
        self.first_count = 0
        self.second_count = 0

    def __lt__(self, another):
        return self.value < another.value
