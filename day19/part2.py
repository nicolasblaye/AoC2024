import time

with open("input.txt", 'r') as f:
    input_data = f.readlines()


def can_design(design, patterns, pattern_dict, memoize):
    if len(design) == 0:
        return 1
    if design in memoize:
        return memoize[design]
    res = 0
    if design[0] in pattern_dict:
        for pattern in pattern_dict[design[0]]:
            if design.startswith(pattern):
                res += can_design(design[len(pattern):], patterns, pattern_dict, memoize)
        memoize[design] = res
    else:
        memoize[design] = 0
    return res

patterns = list(map(lambda x: x.strip(), input_data[0].split(",")))
pattern_dict = dict()
for pattern in patterns:
    first_letter = pattern[0]
    if first_letter not in pattern_dict:
        pattern_dict[first_letter] = []
    pattern_dict[first_letter].append(pattern)

result = 0
start = time.time()
memoize = dict()
for i in range(2, len(input_data)):
    design = input_data[i].strip()
    res_des = can_design(design, patterns, pattern_dict, memoize)
    result += res_des

print(result, "Elapsed: ", round(time.time() - start, 6), "seconds")