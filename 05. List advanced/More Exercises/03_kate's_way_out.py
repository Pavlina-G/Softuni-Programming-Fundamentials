def boundary_maze(maze, m, n):
    kate_one_out = False
    for row in range(m):
        for col in range(n):
            if (row == 0):
                if maze[row][col] == ' ':
                    maze[row][col] = 'E'
                if maze[row][col] == 'k':
                    kate_one_out = True
            elif (row == m - 1):
                if maze[row][col] == ' ':
                    maze[row][col] = 'E'
                if maze[row][col] == 'k':
                    kate_one_out = True
            elif (col == 0):
                if maze[row][col] == ' ':
                    maze[row][col] = 'E'
                if maze[row][col] == 'k':
                    kate_one_out = True
            elif (col == n - 1):
                if maze[row][col] == ' ':
                    maze[row][col] = 'E'
                if maze[row][col] == 'k':
                    kate_one_out = True

    return maze, kate_one_out


def is_valid_position(maze, pos_r, pos_c):
    if pos_r < 0 or pos_c < 0:
        return False
    if pos_r >= len(maze) or pos_c >= len(maze[0]):
        return False
    if maze[pos_r][pos_c] in ' E':
        return True
    return False


def solve_maze(maze, kate_row, kate_col):
    # Python list as a stack - append, pop
    stack = []
    path = []
    paths_len = []
    # Add kate position (as a tuple)
    stack.append((kate_row, kate_col))

    while len(stack) > 0:

        pos_r, pos_c = stack.pop()
        # print("Current position", pos_r, pos_c)
        path.append((pos_r, pos_c))

        if maze[pos_r][pos_c] == 'E':
            stack.append((kate_row, kate_col))
            paths_len.append(len(path))
            path = []
            continue

        if maze[pos_r][pos_c] == 'X': # Already visited
            continue

        if maze[pos_r][pos_c] == '#':
            continue

        maze[pos_r][pos_c] = 'X' # Mark position as visited

        # Check for all possible positions
        if is_valid_position(maze, pos_r - 1, pos_c):
            stack.append((pos_r - 1, pos_c))
        if is_valid_position(maze, pos_r + 1, pos_c):
            stack.append((pos_r + 1, pos_c))
        if is_valid_position(maze, pos_r, pos_c - 1):
            stack.append((pos_r, pos_c - 1))
        if is_valid_position(maze, pos_r, pos_c + 1):
            stack.append((pos_r, pos_c + 1))

    return paths_len


rows = int(input())
maze = []
kate_row = 0
kate_col = 0

for row in range(rows):
    row_elements = list(input())
    maze.append(row_elements)
    for col in range(len(row_elements)):
        if maze[row][col] == 'k':
            kate_row = row
            kate_col = col

m = len(maze)
n = len(maze[0])

maze, condition = boundary_maze(maze, m, n)
paths = (solve_maze(maze, kate_row, kate_col))

if condition and len(paths) == 0:
    print(f'Kate got out in 1 moves')
elif not condition and len(paths) == 0:
    print('Kate cannot get out')
else:
    print(f'Kate got out in {max(paths)} moves')
