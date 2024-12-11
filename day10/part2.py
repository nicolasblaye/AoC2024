def find_next_value(i, j, grid, value):
    if grid[j][i] == '9':
        return 1
    result = 0
    next_value = str(int(value)+1)
    # UP
    if j > 0 and grid[j-1][i] == value:
        result += find_next_value(i, j-1, grid, next_value)
    # DOWN
    if j < len(grid)-1 and grid[j+1][i] == value:
        result += find_next_value(i, j+1, grid, next_value)
    # RIGHT
    if i < len(grid[j])-1 and grid[j][i+1] == value:
        result += find_next_value(i+1, j, grid, next_value)
    # LEFT
    if i > 0 and grid[j][i-1] == value:
        result += find_next_value(i-1, j, grid, next_value)

    return result

def get_all_train(i, j, grid):
    return find_next_value(i, j, grid, str(int('1')))


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