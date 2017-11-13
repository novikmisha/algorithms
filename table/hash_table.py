import random


class HashTable():
    CONSTANT = 131

    def __init__(self):
        self._table = [set() for i in range(0, self.CONSTANT)] 

    def add(self, value):
        hash = self._hash_function(value)
        self._table[hash].add(value)
    
    def delete(self, value):
        hash = self._hash_function(value)

        if value in self._table[hash]:
            self._table[hash].remove(value)

    def find(self, value):
        hash = self._hash_function(value)

        if value in self._table[hash]:
            return value
        else:
            raise LookupError('No such element')

    def _hash_function(self, value) :
        return hash(value) % self.CONSTANT 


if __name__ == "__main__":
    table = HashTable()
    for i in range(0, 1000):
        table.add(random.randint(0, 100000))

    table.add(132)
    table.add(5632)
    table.add(5632)

    for i in range(0, table.CONSTANT):
        print("{} - {}".format(i, table._table[i]))

    table.delete(5632)

    for i in range(0, table.CONSTANT):
        print("{} - {}".format(i, table._table[i]))

