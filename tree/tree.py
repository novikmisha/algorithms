from node import Node

class Struct(object): pass

class Tree:
    def __init__(self, root = None):
        self.path = []
        if root is not None:
            self.root = Node(root)

    def add_value(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.__add(value, self.root)

    def __add(self, value, node):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
                node.left.parent = node
            else:
                self.__add(value, node.left)
        else:
            if node.right is None:
                node.right = Node(value)
                node.right.parent = node
            else:
                self.__add(value, node.right)

    def find(self, value):
        if self.root is None:
            return None
        else:
            node = self.__find(value, self.root)

            if node is not None:
                return node.value
            else:
                return None

    def __find(self, value, node):
        if value is node.value:
            return node
        elif node.left is not None and node.value > value:
            return self.__find(value, node.left)
        elif node.right is not None:
            return self.__find(value, node.right)

        return None

    def __find_min(self, node = None):
        # if we use root
        if node is None:
            node = self.root
        '''
        if node.right is not None:
            node = node.right
        else:
            return node
        '''

        if node.left is not None:
            return self.__find_min(node = node.left)
        else:
            return node


    def delete(self, value):
        node = self.__find(value, self.root)

        if node is not None:
            # case 1, no children
            if node.left is None and node.right is None:
                parent = node.parent
                if value < parent.value:
                    parent.left = None
                else:
                    parent.right = None

            # case 2, has 2 child
            elif node.left is not None and node.right is not None:
                # find min value in right branch
                min_node = self.__find_min(node.right)
                node.value = min_node.value
                if node.right == min_node:
                    node.right = min_node.right
                else:
                    min_node.parent.left = min_node.right

            #case 3, has one child
            elif node.left is not None or node.right is not None:
                # find not empty branch
                branch = node.left or node.right
                parent = node.parent

                if value < parent.value:
                    parent.left = branch
                    branch.parent = parent
                else:
                    parent.right = branch
                    branch.parent = parent


    def right_rotate(self, node):
        '''
        new_root = self.root.right
        if new_root is not None:
            self.root.right, new_root.left = new_root.left, self.root
            self.root = new_root
        '''
        y = node.left
        node.left = y.right
        if y.right is not None:
            y.right.parent = node

        y.parent = node.parent

        if node.parent is None:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y
        y.right = node
        node.parent = y

    def left_rotate(self, node):
        '''
        new_root = self.root.left
        if new_root is not None:
            self.root.left, new_root.right = new_root.left, self.root
            self.root = new_root

       '''
        y = node.right
        node.right = y.left
        if y.left is not None:
            y.left.parent = node

        y.parent = node.parent

        if node.parent is None:
            self.root = y
        elif node == node.parent.right:
            node.parent.right = y
        else:
            node.parent.left = y
        y.left = node
        node.parent = y


    def rotate_to_root(self, value):
        node = self.__find(value, self.root)

        if node is None:
            return

        while node.parent is not None:
            parent = node.parent

            if parent.left == node:
                self.right_rotate(parent)
            else:
                self.left_rotate(parent)

            self.traverse()

            
    def traverse(self):
        print("*********")
        thislevel = [self.root]
        a = '                                                  '
        while thislevel:
            nextlevel = list()
            a = a[:len(a) // 2]
            string = ""
            for n in thislevel:
                if n is None:
                    n = Node("!")

                string += a + str(n.value)
                if n.left is not None: 
                    nextlevel.append(n.left)
                else:
                    nextlevel.append(None)

                if n.right is not None: 
                    nextlevel.append(n.right)
                else:
                    nextlevel.append(None)


            thislevel = nextlevel

            br = True
            for n in thislevel:
                if n is not None:
                    br = False
                    break

            print()
            print(string)

            if br:
                break
