with open("input.txt", 'r') as f:
    input_data = list(map(lambda x: int(x), f.read()))

space_map = dict()
value_map = dict()
values = []
empty_index = []
index = 0

for i in range(len(input_data)):
    nb_repeat = input_data[i]
    if i % 2 == 0:
        value = int(i / 2)
        value_map[str(value)] = (index, nb_repeat) # store index and repeat number
        values.append(value)
    else:
        space_map[str(index)] = nb_repeat  # store repeat number for space
        empty_index.append(index)
    index += nb_repeat

for i in range(len(values)-1, -1, -1):
    value = values[i]
    value_index, value_repeat = value_map[str(value)]
    for k in range(len(empty_index)):
        index = empty_index[k]
        # can't move file after its current position
        if index >= value_index:
            break
        if space_map[str(index)] >= value_repeat:
            new_index = index + value_repeat
            space_left = space_map[str(index)] - value_repeat
            if space_left == 0:
                empty_index.pop(k)
            else:
                empty_index[k] = new_index
                space_map[str(new_index)] = space_left  # append new index for new space
            value_map[str(value)] = (index, value_repeat)
            break

result = 0

for value, (index, repeat) in value_map.items():
    for i in range(index, index+repeat):
        result += int(value) * i

print(result)