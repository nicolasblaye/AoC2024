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
    grid.append(line.strip())

x_index, y_index, direction = find_start(grid)
count = 1
inside_bound = True

visited = {(x_index, y_index)}
while inside_bound:
    new_x_index, new_y_index = move(x_index, y_index, direction)
    if new_x_index < 0 or new_x_index == len(grid[0]) or new_y_index < 0 or new_y_index == len(grid):
        inside_bound = False
    elif grid[new_y_index][new_x_index] == '#':
        direction = turn_right(direction)
    else:
        if (new_x_index, new_y_index) not in visited:
            count+=1
            visited.add((new_x_index, new_y_index))
        x_index, y_index = new_x_index, new_y_index

print(count)

