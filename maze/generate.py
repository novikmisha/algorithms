import random

SIZE = 30

class Cell():
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.visited = False
        self.path = False
        # does the wall exist
        self.top = None
        self.bottom = None
        self.left = None
        self.right = None

def print_maze(maze, rows, cols):
    for row in range(rows):
        a = '+'
        b = '| '
        for col in range(cols):
            #c = ' '
            if maze[row][col].path:
                c = 'X'
            else:
                c = ' '
            if maze[row][col].top is None:
                a += ' - +'
            else:
                a += '   +'

            if maze[row][col].right is None:
                b += c + ' | '
            else:
                b += c + '   '

        print(a)
        print(b)

    a = '+'
    for col in range(cols):
        if maze[rows - 1][col].bottom is None:
            a += ' - +'
        else:
            a += '   +'

    print(a)


def get_near(maze, cell, rows, cols):
    result = set()

    for row in range(cell.row - 1, cell.row + 2):
        for col in range(cell.col -  1, cell.col + 2):
            if 0 <= row < rows and 0 <= col < cols and maze[row][col].visited == False:
                if row == cell.row + 1 and col == cell.col - 1:
                    continue
                elif row == cell.row + 1 and col == cell.col + 1:
                    continue
                elif row == cell.row - 1 and col == cell.col - 1:
                    continue
                elif row == cell.row - 1 and col == cell.col + 1:
                    continue

                result.add(maze[row][col])

    return result


def remove_wall(maze, cell):
    list_maze = list(maze)
    random.shuffle(list_maze)
    for maze_cell in list_maze:
        if maze_cell.row == cell.row and maze_cell.col - 1 == cell.col:
            maze_cell.left = cell
            cell.right = maze_cell
            break
        elif maze_cell.row == cell.row and maze_cell.col + 1 == cell.col:
            maze_cell.right = cell
            cell.left = maze_cell
            break
        elif maze_cell.col == cell.col and maze_cell.row - 1 == cell.row:
            maze_cell.top = cell
            cell.bottom = maze_cell
            break
        elif maze_cell.col == cell.col and maze_cell.row + 1 == cell.row:
            maze_cell.bottom = cell
            cell.top = maze_cell
            break

    
def generate(rows, cols):
    maze = [[] for i in range(rows)]
    new_maze = set()
    cells = set()

    for row in range(rows):
        for col in range(cols):
            maze[row].append(Cell(row, col))
    
    row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)
    maze[row][col].visited = True
    new_maze.add(maze[row][col])
    near = get_near(maze, maze[row][col], rows, cols) 
    cells = cells.union(near)

    completed = False
    while not completed:
        rand = random.randint(0, len(cells) - 1)
        new_cell = list(cells)[rand]
        new_maze.add(new_cell)
        cells.remove(new_cell)
        new_cell.visited = True

        remove_wall(new_maze, new_cell)

        near = get_near(maze, new_cell, rows, cols) 
        cells = cells.union(near)

        if len(cells) == 0:
            completed = True

    return maze

def dfs_start(maze, start, end):
    # govnocodim
    for row in maze:
        for node in row:
            node.visited = False

    return dfs(maze, start, end, [])


def dfs(maze, current, end, path):
    current.visited = True
    if current == end:
        path.append(current)
        return path

    for node in get_childrens(current):
        temp_path = path[:]
        temp_path.append(current)
        p = dfs(maze, node, end, temp_path)
        if p:
            return p

    return None


def get_childrens(current):
    childrens = set()
    if current.top is not None and not current.top.visited:
        childrens.add(current.top)
 
    if current.bottom is not None and not current.bottom.visited:
        childrens.add(current.bottom)


    if current.left is not None and not current.left.visited:
        childrens.add(current.left)
  

    if current.right is not None and not current.right.visited:
        childrens.add(current.right)

    return childrens


if __name__ == "__main__":
    maze = generate(SIZE, SIZE)
    # print_maze(maze, 8, 8)
    p = dfs_start(maze, maze[0][0], maze[SIZE - 1][SIZE - 1])

    for node in p:
        node.path = True

    print_maze(maze, SIZE, SIZE)
