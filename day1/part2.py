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

result = 0
for i in list_1:
    occurence = 0
    for j in list_2:
        if i == j:
            occurence +=1
        if i < j:
            break
    result += i * occurence

print(result)