import sys
import time

# return the current position of the robot and the grid
def move_left(start_position, end_position, grid):
    j = start_position[1]
    for i in range(end_position[0], start_position[0]-1):
        grid[j][i] = grid[j][i+1]
    grid[start_position[1]][start_position[0]-1] = '@'
    grid[start_position[1]][start_position[0]] = '.'
    return (start_position[0]-1, start_position[1]), grid

# return the current position of the robot and the grid
def move_right(start_position, end_position, grid):
    j = start_position[1]
    for i in range(end_position[0], start_position[0]+1, -1):
        grid[j][i] = grid[j][i-1]
    grid[start_position[1]][start_position[0] + 1] = '@'
    grid[start_position[1]][start_position[0]] = '.'
    return (start_position[0]+1, start_position[1]), grid

def can_move_vertically(pos, grid, direction_fun):
    neighboor = (pos[0], direction_fun(pos[1]))
    if grid[neighboor[1]][neighboor[0]] == '[':
        neighboor_other = (pos[0]+1, direction_fun(pos[1]))
        return can_move_vertically(neighboor, grid, direction_fun) and can_move_vertically(neighboor_other, grid, direction_fun)
    if grid[neighboor[1]][neighboor[0]] == ']':
        neighboor_other = (pos[0]-1, direction_fun(pos[1]))
        return can_move_vertically(neighboor, grid, direction_fun) and can_move_vertically(neighboor_other, grid, direction_fun)
    if grid[neighboor[1]][neighboor[0]] == '#':
        return False
    if grid[neighboor[1]][neighboor[0]] == '.':
        return True


def move_vertically(pos, grid, direction_fun):
    neighboor = (pos[0], direction_fun(pos[1]))
    neighboor_other = None
    if grid[neighboor[1]][neighboor[0]] == '[':
        neighboor_other = (pos[0] + 1, direction_fun(pos[1]))
    if grid[neighboor[1]][neighboor[0]] == ']':
        neighboor_other = (pos[0] - 1, direction_fun(pos[1]))

    if neighboor_other is not None:
        grid = move_vertically(neighboor, grid, direction_fun)
        grid = move_vertically(neighboor_other, grid, direction_fun)

    grid[neighboor[1]][neighboor[0]] = grid[pos[1]][pos[0]]
    grid[pos[1]][pos[0]] = '.'

    return grid



with open("input.txt", 'r') as f:
    input_data = f.readlines()

## Prepare the grid
grid = []
start = (0, 0)
i,j = 0,0
inputs = []
for line in input_data:
    if line.startswith('#'):
        new_line = []
        i = 0
        for char in line.strip():
            if char in ('#', '.'):
                new_line.append(char)
                new_line.append(char)
            if char == 'O':
                new_line.append('[')
                new_line.append(']')
            if char == '@':
                new_line.append('@')
                new_line.append('.')
                start = (i, j)
            i += 2
        grid.append(new_line)
        j += 1
    else:
        if not line.startswith(' ') and not line.startswith("\n"):
            for char in line.strip():
                inputs.append(char)

for line in grid:
    print("".join(line))
print("***************")
robot_position = start
for move in inputs:
    print(move)
    if move == '<':
        scan_position = robot_position
        # scan to find either last box or wall
        while grid[scan_position[1]][scan_position[0]] not in ('#', '.'):
            scan_position = (scan_position[0]-1, scan_position[1])
        if grid[scan_position[1]][scan_position[0]] == '.':
            robot_position, grid = move_left(robot_position, scan_position, grid)
    if move == '>':
        scan_position = robot_position
        # scan to find either last box or wall
        while grid[scan_position[1]][scan_position[0]] not in ('#', '.'):
            scan_position = (scan_position[0]+1, scan_position[1])
        if grid[scan_position[1]][scan_position[0]] == '.':
            robot_position, grid = move_right(robot_position, scan_position, grid)
    if move == '^':
        scan_position = robot_position
        if can_move_vertically(robot_position, grid, lambda x: x-1):
            grid = move_vertically(robot_position, grid, lambda x: x-1)
            robot_position = (robot_position[0], robot_position[1]-1)
    if move == 'v':
        scan_position = robot_position
        if can_move_vertically(robot_position, grid, lambda x: x + 1):
            grid = move_vertically(robot_position, grid, lambda x: x + 1)
            robot_position = (robot_position[0], robot_position[1] + 1)
    print(robot_position)
    for line in grid:
        print("".join(line))
    print("***************")


## compute the score
res = 0
for j in range(len(grid)):
    for i in range(len(grid[j])):
        if grid[j][i] in ['[']:
            res += 100 * j + i

print(res)