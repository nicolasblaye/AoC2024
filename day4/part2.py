def check_cross(grid, x_index, y_index):
    cross_1 = "".join([grid[y_index-1][x_index-1], 'A', grid[y_index+1][x_index+1]])
    cross_2 = "".join([grid[y_index-1][x_index+1], 'A', grid[y_index+1][x_index-1]])
    return cross_1 in ['MAS', 'SAM'] and cross_2 in ['MAS', 'SAM']

with open("input.txt", 'r') as f:
    input_data = f.readlines()

grid=[]
for line in input_data:
    grid.append(line.strip())

result = 0
for j in range(1, len(grid)-1):
    for i in range(1, len(grid[j])-1):
        if grid[j][i] == 'A':
            if check_cross(grid, i, j):
                result += 1
print(result)
