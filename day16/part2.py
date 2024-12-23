import sys
import time
import copy

# score for input
best_path_part_1 = 85480

# score for input test small
#best_path_part_1 = 7036

# score for input test
#best_path_part_1 = 11048

import sys

sys.setrecursionlimit(1000000)

def compute_path(pos, dir, best_path, grid, score, paths, dir_list):
    if (pos, dir) in paths and paths[(pos, dir)][0] < score or score > best_path_part_1:
        return

    paths[(pos, dir)] = (score, dir_list)

    new_pos = directions[dir](pos)

    turns = turn_90[dir]
    for new_dir in turns:
        new_dir_list = copy.copy(dir_list)
        new_dir_list[-1] = new_dir
        compute_path(pos, new_dir, best_path, grid, score + 1000, paths, new_dir_list)

    if grid[new_pos[1]][new_pos[0]] == '.':
        new_dir_list = copy.copy(dir_list)
        new_dir_list.append(dir)
        compute_path(new_pos, dir, best_path, grid, score + 1, paths, new_dir_list)
        return

    elif grid[new_pos[1]][new_pos[0]] == 'E':
        print(score+1)
        if score+1 == best_path_part_1:
            new_dir_list = copy.copy(dir_list)
            new_dir_list.append(dir)
            best_path.add("".join(new_dir_list))
            return
    else:
        return


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

with open("input.txt", 'r') as f:
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

paths = dict()
best_path = set()
compute_path(start, '>', best_path, grid, 0, paths, ['>'])

visited = set()
visited.add(start)
visited.add(end)
for path in best_path:
    current_pos = start
    for direction in path:
        new_pos = directions[direction](current_pos)
        if grid[new_pos[1]][new_pos[0]] == '.':
            visited.add(new_pos)
            current_pos = new_pos

for pos in visited:
    grid[pos[1]][pos[0]] = 'O'

print(len(visited))

