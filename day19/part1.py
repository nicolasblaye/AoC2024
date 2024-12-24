
with open("input.txt", 'r') as f:
    input_data = f.readlines()


def can_design(design, patterns):
    if len(design) == 0:
        return True
    res = False
    for pattern in patterns:
        if design.startswith(pattern):
            res = res or can_design(design[len(pattern):], patterns)
    return res

patterns = list(map(lambda x: x.strip(), input_data[0].split(",")))

result = 0
for i in range(2, len(input_data)):
    design = input_data[i].strip()
    if can_design(design, patterns):
        result += 1

print(result)