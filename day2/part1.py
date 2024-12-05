with open("input.txt", 'r') as f:
    input_data = f.readlines()

safe_count = 0
for line in input_data:
    line = line.strip()
    values = list(map(lambda x: int(x), line.split(" ")))
    current_sign = 0
    is_safe = True
    for i in range(len(values) - 1):
        current = values[i]
        next = values[i+1]
        is_safe = 1 <= abs(current - next) <= 3
        if current_sign == 0:
            current_sign = current - next
        else:
            is_safe = is_safe and current_sign * (current - next) > 0
        if not is_safe:
            break
    if is_safe:
        safe_count += 1

print(safe_count)


