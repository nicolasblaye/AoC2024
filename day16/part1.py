import sys
import time

sys.setrecursionlimit(1000000)

def compute_path(pos, dir, best_path, grid, score, paths):
    if (pos, dir) in paths and paths[(pos, dir)] <= score or score > best_path:
        return best_path

    if not (pos, dir) in paths:
        paths[pos, dir] = (0, [])

    paths[(pos, dir)] = score

    new_pos = directions[dir](pos)

    turns = turn_90[dir]
    for new_dir in turns:
        best_path = min(best_path, compute_path(pos, new_dir, best_path, grid, score + 1000, paths))

    if grid[new_pos[1]][new_pos[0]] == '.':
        path = compute_path(new_pos, dir, best_path, grid, score + 1, paths)
        return min(best_path, path)

    elif grid[new_pos[1]][new_pos[0]] == 'E':
        return min(best_path, score+1)

    else:
        return best_path


directions = {
    '^': lambda x: (x[0], x[1]-1),
    'v': lambda x: (x[0], x[1]+1),
    '>': lambda x: (x[0]+1, x[1]),
    '<': lambda x: (x[0]-1, x[1])
}

turn_90 = {
    '^': ['<', '>'],
    'v': ['<', '>'],
    '>': ['^', 'v'],
    '<': ['^', 'v']
}

with open("input_test_small.txt", 'r') as f:
    input_data = f.readlines()

## Prepare the grid
grid = []
start = (0, 0)
end = (0, 0)
i,j = 0,0
inputs = []
for line in input_data:
    new_line = []
    i = 0
    for char in line.strip():
        new_line.append(char)
        if char == 'S':
            start = (i, j)
        if char == 'E':
            end = (i, j)
        i += 1
    grid.append(new_line)
    j += 1

best_path = 1104800
paths = dict()
best_path = min(best_path, compute_path(start, '>', best_path, grid, 0, paths))
print(best_path)

