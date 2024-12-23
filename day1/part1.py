with open("input.txt", 'r') as f:
    input_data = f.readlines()

list_1 = []
list_2 = []

for line in input_data:
    line = line.strip()
    values = line.split(" ")
    list_1.append(int(values[0]))
    list_2.append(int(values[-1]))

list_1.sort()
list_2.sort()

print(sum(map(lambda x: abs(x[0] - x[1]), zip(list_1, list_2))))
