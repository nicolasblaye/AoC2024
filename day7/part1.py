with open("input.txt", 'r') as f:
    input_data = f.readlines()

count = 0
for line in input_data:
    test_value, equation = line.split(":")
    test_value = int(test_value)
    equation = list(map(lambda x: int(x), equation.strip().split(" ")))

    results = [equation[0]]
    for i in range(1, len(equation)):
        value = equation[i]
        new_results = []
        for result in results:
            add = result + value
            multiply = result * value
            new_results.append(add)
            new_results.append(multiply)
        results = new_results

    for result in results:
        if result == test_value:
            count += test_value
            break

print(count)
