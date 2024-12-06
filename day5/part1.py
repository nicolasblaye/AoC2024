with open("input.txt", 'r') as f:
    input_data = f.readlines()


page_mapping = dict()
result = 0
for line in input_data:
    line = line.strip()
    if '|' in line:
        i, j = line.split('|')
        if j in page_mapping:
            page_mapping[j].append(int(i))
        else:
            page_mapping[j] = [int(i)]
    if ',' in line:
        is_update_correct = True
        values = list(map(lambda x: int(x), line.split(",")))
        needed_update = set()
        for value in values:
            if value in needed_update:
                is_update_correct = False
                break
            if str(value) in page_mapping:
                for mapping in page_mapping[str(value)]:
                    needed_update.add(mapping)
        if is_update_correct:
            result += values[int(len(values)/2)]

print(result)
