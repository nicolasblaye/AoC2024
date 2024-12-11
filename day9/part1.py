with open("input.txt", 'r') as f:
    input_data = list(map(lambda x: int(x), f.read()))

result = [0] * input_data[0]

index = input_data[0]
current_space_index = 1
for i in range(len(input_data)-1, -1, -2):
    repeat_number = input_data[i]
    number = int(i / 2)

    if current_space_index >= i:
        break

    for j in range(current_space_index, len(input_data), 2):
        space = input_data[j]
        if space < repeat_number:
            result = result + [number] * space
            repeat_number -= space

            repeat_next = input_data[j+1]
            number_next = int((j+1) / 2)

            if number_next == number:
                result = result + [number_next] * repeat_number
                repeat_number = 0
            else:
                result = result + [number_next] * repeat_next
        else:
            result = result + [number] * repeat_number
            input_data[j] = space - repeat_number
            current_space_index = j
            break


count = 0
for i in range(len(result)):
    count += i * result[i]

print(count)
