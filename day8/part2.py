with open("input.txt", 'r') as f:
    input_data = f.readlines()

grid = []
char_map = dict()
for i in range(len(input_data)):
    line = input_data[i].strip()
    new_line = []
    for char in line:
        new_line.append(char)
    line = new_line
    grid.append(line)
    for j in range(len(line)):
        char = line[j]
        if char != '.':
            if char not in char_map:
                char_map[char] = [(j, i)]
            else:
                char_map[char].append((j, i))

antinodes = set()
for positions in char_map.values():
    for i in range(len(positions)):
        for j in range(i+1, len(positions)):
            antenna_1 = positions[i]
            antenna_2 = positions[j]

            x_diff = antenna_2[0] - antenna_1[0]
            y_diff = antenna_2[1] - antenna_1[1]

            # ascend
            current_x = antenna_2[0]
            current_y = antenna_2[1]
            while 0 <= current_x < len(grid[0]) and  0 <= current_y < len(grid):
                antinodes.add((current_x, current_y))
                current_x += x_diff
                current_y += y_diff

            # descend
            current_x = antenna_1[0]
            current_y = antenna_1[1]
            while 0 <= current_x < len(grid[0]) and 0 <= current_y < len(grid):
                antinodes.add((current_x, current_y))
                current_x -= x_diff
                current_y -= y_diff

print(antinodes)
correct_nodes = list(filter(lambda x: 0 <= x[0] < len(grid[0]) and 0 <= x[1] < len(grid), antinodes))
print(len(correct_nodes))
