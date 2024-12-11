import time

def blink(stones):
    result = []
    for stone in stones:
        if stone == 0:
            result.append(1)
        elif len(str(stone)) % 2 == 0:
            string_value = str(stone)
            first_number = int(str(stone)[:int(len(string_value)/2)])
            second_number = int(str(stone)[int(len(string_value)/2):])
            result.append(first_number)
            result.append(second_number)
        else:
            result.append(stone * 2024)
    return result


with open("input.txt", 'r') as f:
    stones = list(map(lambda x: int(x), f.read().split(" ")))

nb_blink = 75
start = time.time()
for i in range(nb_blink):
    print(i, "elapsed", time.time() - start)
    stones = blink(stones)
print(len(stones))
