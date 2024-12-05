import re

with open("input.txt", 'r') as f:
    input_data = f.readlines()

regex = re.compile("mul\(\d{1,3},\d{1,3}\)")



result = 0
for line in input_data:
    matches = re.findall(regex, line)
    for match in matches:
        part1, part2 = match.split(",")

        i = int(part1[4:])
        j = int(part2[:-1])

        print(match, i, j)
        result+= i*j

print(result)