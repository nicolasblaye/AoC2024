with open("input.txt", 'r') as f:
    input_data = f.readlines()

def is_report_safe(values):
    current_sign = 0
    is_safe = True
    for i in range(len(values) - 1):
        current = values[i]
        next = values[i + 1]
        is_safe = 1 <= abs(current - next) <= 3
        if current_sign == 0:
            current_sign = current - next
        else:
            is_safe = is_safe and current_sign * (current - next) > 0
        if not is_safe:
            break
    return is_safe


## bruteforce solution
safe_count = 0
for line in input_data:
    line = line.strip()
    input_values = list(map(lambda x: int(x), line.split(" ")))
    is_safe = True
    if not is_report_safe(input_values):
        for i in range(len(input_values)):
            is_safe = is_report_safe(input_values[0:i] + input_values[i+1:])
            if is_safe:
                break
    if is_safe:
        safe_count += 1

print(safe_count)



