import time
import sys

sys.setrecursionlimit(1500000)
stone_value = dict()

def blink(stone, nb_blink, stone_value):
    ## result of a blink for one stone
    if str(stone) in stone_value and str(nb_blink) in stone_value[str(stone)]:
        return stone_value[str(stone)][str(nb_blink)]

    if nb_blink == 0:
        return 1

    if stone == 0:
        value = blink(1, nb_blink-1, stone_value)
    elif len(str(stone)) % 2 == 0:
        string_value = str(stone)
        first_number = int(str(stone)[:int(len(string_value)/2)])
        second_number = int(str(stone)[int(len(string_value)/2):])

        value =  blink(first_number, nb_blink-1, stone_value) + blink(second_number, nb_blink-1, stone_value)
    else:
        value =  blink(stone * 2024, nb_blink-1, stone_value)

    if str(stone) not in stone_value:
        stone_value[str(stone)] = dict()
    stone_value[str(stone)][str(nb_blink)] = value
    return value


with open("input.txt", 'r') as f:
    stones = list(map(lambda x: int(x), f.read().split(" ")))



nb_blink = 75
start = time.time()
result = 0
for stone in stones:
    value = blink(stone, nb_blink, dict())
    result += value
print(result, round(time.time() - start, 2), "seconds")
