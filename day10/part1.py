def find_next_value(i, j, grid, value, reached_heights):
    if grid[j][i] == '9':
        if (i, j) not in reached_heights:
            reached_heights.add((i, j))
            return 1
        else:
            return 0
    result = 0
    next_value = str(int(value)+1)
    # UP
    if j > 0 and grid[j-1][i] == value:
        result += find_next_value(i, j-1, grid, next_value, reached_heights)
    # DOWN
    if j < len(grid)-1 and grid[j+1][i] == value:
        result += find_next_value(i, j+1, grid, next_value, reached_heights)
    # RIGHT
    if i < len(grid[j])-1 and grid[j][i+1] == value:
        result += find_next_value(i+1, j, grid, next_value, reached_heights)
    # LEFT
    if i > 0 and grid[j][i-1] == value:
        result += find_next_value(i-1, j, grid, next_value, reached_heights)

    return result

def get_all_train(i, j, grid):
    reached_heights = set()
    return find_next_value(i, j, grid, str(int('1')), reached_heights)


with open("input.txt", 'r') as f:
    input_data = f.readlines()


grid = []

for line in input_data:
    grid.append(line.strip())

result = 0
for j in range(len(grid)):
    for i in range(len(grid[j])):
        if grid[j][i] == '0':
            result += get_all_train(i, j, grid)

print(result)