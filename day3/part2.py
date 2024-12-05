import re

with open("input.txt", 'r') as f:
    input_data = f.read()

regex = re.compile("mul\(\d{1,3},\d{1,3}\)")

do = re.compile("do\(\)")
dont = re.compile("don't\(\)")



result = 0
do_parts = re.split(do, input_data)
parts_to_do = []
for part in do_parts:
    parts_to_do.append(re.split(dont, part)[0])
# only select do parts
for i in range(0, len(parts_to_do)):
    part = parts_to_do[i]
    matches = re.findall(regex, part)
    for match in matches:
        part1, part2 = match.split(",")

        i = int(part1[4:])
        j = int(part2[:-1])

        print(match, i, j)
        result+= i*j

print(result)