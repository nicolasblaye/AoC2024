import sys
import time

# return the current position of the robot and the grid
def move_left(start_position, end_position, grid):
    j = start_position[1]
    for i in range(end_position[0], start_position[0]-1):
        grid[j][i] = 'O'
    grid[start_position[1]][start_position[0]-1] = '@'
    grid[start_position[1]][start_position[0]] = '.'
    return (start_position[0]-1, start_position[1]), grid

# return the current position of the robot and the grid
def move_right(start_position, end_position, grid):
    j = start_position[1]
    for i in range(end_position[0], start_position[0]+1, -1):
        grid[j][i] = 'O'
    grid[start_position[1]][start_position[0] + 1] = '@'
    grid[start_position[1]][start_position[0]] = '.'
    return (start_position[0]+1, start_position[1]), grid

# return the current position of the robot and the grid
def move_up(start_position, end_position, grid):
    i = start_position[0]
    for j in range(end_position[1], start_position[1]):
        grid[j][i] = 'O'
    grid[start_position[1]-1][start_position[0]] = '@'
    grid[start_position[1]][start_position[0]] = '.'
    return (start_position[0], start_position[1]-1), grid

# return the current position of the robot and the grid
def move_down(start_position, end_position, grid):
    i = start_position[0]
    for j in range(end_position[1], start_position[1]-1, -1):
        grid[j][i] = 'O'
    grid[start_position[1]+1][start_position[0]] = '@'
    grid[start_position[1]][start_position[0]] = '.'
    return (start_position[0], start_position[1]+1), grid


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
            new_line.append(char)
            if char == '@':
                start = (i, j)
            i += 1
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
    #print(move)
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
        # scan to find either last box or wall
        while grid[scan_position[1]][scan_position[0]] not in ('#', '.'):
            scan_position = (scan_position[0], scan_position[1]-1)
        if grid[scan_position[1]][scan_position[0]] == '.':
            robot_position, grid = move_up(robot_position, scan_position, grid)
    if move == 'v':
        scan_position = robot_position
        # scan to find either last box or wall
        while grid[scan_position[1]][scan_position[0]] not in ('#', '.'):
            scan_position = (scan_position[0], scan_position[1]+1)
        if grid[scan_position[1]][scan_position[0]] == '.':
            robot_position, grid = move_down(robot_position, scan_position, grid)
    #print(robot_position)
    #for line in grid:
    #    print("".join(line))
    #print("***************")


## compute the score
res = 0
for j in range(len(grid)):
    for i in range(len(grid[j])):
        if grid[j][i] == 'O':
            res += 100 * j + i

print(res)