import copy

with open("input.txt", 'r') as f:
    input_data = f.readlines()

bytes = []
for line in input_data:
    x,y = map(lambda x: int(x), line.strip().split(","))
    bytes.append((x,y))

width = height = 71
grid = [['.'] * height for _ in range(width)]

for i in range(1024):
    x, y = bytes[i]
    grid[y][x] = '#'

for line in grid:
    print("".join(line))

def bfs(grid, start, finish):
    visited = set(start)
    paths = [[start]]
    while True:
        new_paths = []
        if len(paths) == 0:
            return -1
        for path in paths:
            if path[-1] == finish:
                return len(path)
            cur_x, cur_y = path[-1]
            if cur_y > 0 and grid[cur_y-1][cur_x] == '.' and (cur_x, cur_y-1) not in visited:
                new_path = copy.copy(path)
                new_path.append((cur_x, cur_y-1))
                visited.add((cur_x, cur_y-1))
                new_paths.append(new_path)
            if cur_y < height-1 and grid[cur_y+1][cur_x] == '.' and (cur_x, cur_y+1) not in visited:
                new_path = copy.copy(path)
                new_path.append((cur_x, cur_y+1))
                visited.add((cur_x, cur_y+1))
                new_paths.append(new_path)
            if cur_x > 0 and grid[cur_y][cur_x-1] == '.' and (cur_x-1, cur_y) not in visited:
                new_path = copy.copy(path)
                new_path.append((cur_x-1, cur_y))
                visited.add((cur_x-1, cur_y))
                new_paths.append(new_path)
            if cur_x < width-1 and grid[cur_y][cur_x+1] == '.' and (cur_x+1, cur_y) not in visited:
                new_path = copy.copy(path)
                new_path.append((cur_x+1, cur_y))
                visited.add((cur_x+1, cur_y))
                new_paths.append(new_path)
        paths = new_paths

i = 1024
x,y = bytes[1023]
while bfs(grid, (0, 0), (width-1, height-1)) != -1:
    x,y = bytes[i]
    grid[y][x] = '#'
    i+=1
print(x,y)
