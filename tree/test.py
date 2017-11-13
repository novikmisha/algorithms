from tree import Tree

import subprocess
import sys

if __name__ == "__main__":
    tree = Tree(5)
    tree.add_value(3)
    tree.add_value(9)
    tree.add_value(10)
    tree.add_value(6)
    tree.add_value(7)


    tree.traverse()
    tree.rotate_to_root(7)

    tree.traverse()
    tree.rotate_to_root(7)
    tree.traverse()

    tree.add_value(2)
    tree.add_value(4)

    tree.add_value(8)
    tree.traverse()

    tree.rotate_to_root(4)
    tree.delete(4)
    tree.traverse()

    subprocess.call("ponysay Я СДЕЛАЛЪ", shell=True)
