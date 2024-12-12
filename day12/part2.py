import time
import sys

sys.setrecursionlimit(1500000)

def explore_area(x, y, visited, grid, area, perimeter):
    # perimeter is a dict of dict. The first key is the direction | or -, the second is the "index" so either the x_index or y_index
    # depending on the direction
    letter = grid[y][x]
    visited.add((x, y))
    area.add((x, y))
    # up
    if y > 0 and grid[y-1][x] == letter:
        if (x, y-1) not in visited:
            explore_area(x, y-1, visited, grid, area, perimeter)
    else:
        s = str(y - 0.25)
        if s not in perimeter['-']:
            perimeter['-'][s] = []
        perimeter['-'][s].append(x)
    # down
    if y < len(grid)-1 and grid[y + 1][x] == letter:
        if (x, y + 1) not in visited:
            explore_area(x, y + 1, visited, grid, area, perimeter)
    else:
        str1 = str(y + 0.25)
        if str1 not in perimeter['-']:
            perimeter['-'][str1] = []
        perimeter['-'][str1].append(x)
    # right
    if x < len(grid[j])-1 and grid[y][x+1] == letter:
        if (x+1, y) not in visited:
            explore_area(x+1, y, visited, grid, area, perimeter)
    else:
        str2 = str(x + 0.25)
        if str2 not in perimeter['|']:
            perimeter['|'][str2] = []
        perimeter['|'][str2].append(y)
    # left
    if x > 0 and grid[y][x-1] == letter:
        if (x-1, y) not in visited:
            explore_area(x-1, y, visited, grid, area, perimeter)
    else:
        str3 = str(x - 0.25)
        if str3 not in perimeter['|']:
            perimeter['|'][str3] = []
        perimeter['|'][str3].append(y)

    return letter, len(area), perimeter

def compute_line(perimeter):
    count = 0
    for values in perimeter.values():
        for index, fences in values.items():
            fences.sort()
            count += 1
            for i in range(0, len(fences)-1):
                if fences[i+1] - fences[i] > 1:
                    count += 1
    return count


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
            letter, area, perimeter = explore_area(i, j, visited, grid, set(), {'|': dict(), '-': dict()})
            if letter not in result:
                result[letter] = []
            result[letter].append((area, perimeter))

solution = 0
for areas in result.values():
    for area, perimeter in areas:
        # print(perimeter)
        line = compute_line(perimeter)
        # print(area, line)
        solution += area * line


print(round(time.time() - start, 5), "seconds\nSolution: ", solution)
