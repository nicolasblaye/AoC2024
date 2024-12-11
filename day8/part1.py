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


            antinode_1 = (2 * antenna_2[0] - antenna_1[0], 2 * antenna_2[1] - antenna_1[1])
            antinode_2 = (antenna_1[0] - (antenna_2[0] - antenna_1[0]), antenna_1[1] - (antenna_2[1] - antenna_1[1]))

            antinodes.add(antinode_1)
            antinodes.add(antinode_2)

print(antinodes)
correct_nodes = list(filter(lambda x: 0 <= x[0] < len(grid[0]) and 0 <= x[1] < len(grid), antinodes))
print(len(correct_nodes))
