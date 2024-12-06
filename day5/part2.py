with open("input.txt", 'r') as f:
    input_data = f.readlines()

def is_correctly_ordered(page_mapping, values):
    is_update_correct = True
    needed_update = set()
    for value in values:
        if value in needed_update:
            is_update_correct = False
            break
        if str(value) in page_mapping:
            for mapping in page_mapping[str(value)]:
                needed_update.add(mapping)
    return is_update_correct

def swap_element(a, b, values):
    tmp = values[b]
    values[b] = values[a]
    values[a] = tmp

def reorder(page_mapping, values):
    i = 0
    print(values)
    while i < len(values):
        value = values[i]
        if str(value) in page_mapping:
            index = i
            for mapping in page_mapping[str(value)]:
                if mapping in values:
                    current_index = len(values) - values[::-1].index(mapping) - 1
                    if current_index > index:
                        index = current_index
            if index > i:
                swap_element(i, index, values)
                #print(values)
            else:
                i+=1
        else:
            i += 1
    return values



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
        values = list(map(lambda x: int(x), line.split(",")))
        if not is_correctly_ordered(page_mapping, values):
            result += reorder(page_mapping, values)[int(len(values)/2)]
print(result)
