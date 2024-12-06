import copy

with open("input.txt", 'r') as f:
    input_data = f.readlines()

grid = []

def turn_right(direction):
    if direction == '^':
        return '>'
    elif direction == '>':
        return 'v'
    elif direction == 'v':
        return '<'
    elif direction == '<':
        return '^'

def find_start(grid):
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            if grid[j][i] in ['^', '>', '<', 'v']:
                return i, j, grid[j][i]

def move(x_index, y_index, direction):
    if direction == '^':
        return x_index, y_index-1
    elif direction == '>':
        return x_index+1, y_index
    elif direction == 'v':
        return x_index, y_index+1
    elif direction == '<':
        return x_index-1, y_index


for line in input_data:
    line_list = []
    for char in line.strip():
        line_list.append(char)
    grid.append(line_list)

x_index_start, y_index_start, direction_start = find_start(grid)
count = 0

for j in range(len(grid)):
    for i in range(len(grid[j])):
        if grid[j][i] not in ['#', '^', '>', '<', 'v']:
            new_grid = copy.deepcopy(grid)
            new_grid[j][i] = '#'
            inside_bound = True
            stuck = False
            x_index, y_index, direction = x_index_start, y_index_start, direction_start
            visited = {(x_index_start, y_index_start, direction)}
            while inside_bound and not stuck:
                new_x_index, new_y_index = move(x_index, y_index, direction)
                if new_x_index < 0 or new_x_index == len(new_grid[0]) or new_y_index < 0 or new_y_index == len(new_grid):
                    inside_bound = False
                elif new_grid[new_y_index][new_x_index] == '#':
                    direction = turn_right(direction)
                    visited.add((x_index, y_index, direction))
                else:
                    # guard is stuck if he comes back on a previous position with the same direction
                    if (new_x_index, new_y_index, direction) in visited:
                        count+=1
                        stuck = True
                    else:
                        visited.add((new_x_index, new_y_index, direction))
                    x_index, y_index = new_x_index, new_y_index

print(count)

