import time
import sys

sys.setrecursionlimit(1500000)

def explore_area(x, y, visited, grid, area, perimeter):
    letter = grid[y][x]
    visited.add((x, y))
    area.add((x, y))
    # up
    if y > 0 and grid[y-1][x] == letter:
        if (x, y-1) not in visited:
            _, _, perimeter = explore_area(x, y-1, visited, grid, area, perimeter)
    else:
        perimeter += 1
    # down
    if y < len(grid)-1 and grid[y + 1][x] == letter:
        if (x, y + 1) not in visited:
            _, _, perimeter = explore_area(x, y + 1, visited, grid, area, perimeter)
    else:
        perimeter += 1
    # right
    if x < len(grid[j])-1 and grid[y][x+1] == letter:
        if (x+1, y) not in visited:
            _, _, perimeter = explore_area(x+1, y, visited, grid, area, perimeter)
    else:
        perimeter += 1
    # left
    if x > 0 and grid[y][x-1] == letter:
        if (x-1, y) not in visited:
            _, _, perimeter = explore_area(x-1, y, visited, grid, area, perimeter)
    else:
        perimeter += 1

    return letter, len(area), perimeter


with open("input.txt", 'r') as f:
    input_date = f.readlines()

grid = []

for line in input_date:
    grid.append(line.strip())

visited = set()

start = time.time()
result = dict()
for j in range(len(grid)):
    for i in range(len(grid[j])):
        if (i, j) not in visited:
            letter, area, perimeter = explore_area(i, j, visited, grid, set(), 0)
            if letter not in result:
                result[letter] = []
            result[letter].append((area, perimeter))

solution = 0
for areas in result.values():
    solution += sum(map(lambda x: x[0] * x[1], areas))


print(round(time.time() - start, 5), "seconds\n", result, "\nSolution: ", solution)
