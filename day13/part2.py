import sys
import time

def format_coordinate(line, sign, add):
    x, y = map(lambda x: int(x.strip().split(sign)[1]), line.split(":")[1].split(","))
    return x + add, y + add

def play(a_button, b_button, prize):
    b_press_nom = prize[1] * a_button[0] - prize[0] * a_button[1]
    b_press_div = a_button[0] * b_button[1] - a_button[1] * b_button[0]

    if b_press_nom % b_press_div == 0:
        a_press_nom = prize[1] - b_button[1] * int(b_press_nom / b_press_div)
        a_press_div = a_button[1]

        if a_press_nom % a_press_div == 0:
            return 3 * int(a_press_nom / a_press_div) + int(b_press_nom / b_press_div)
    return 0




with open("input.txt", 'r') as f:
    input_data = f.readlines()

result = 0
for i in range(0, len(input_data), 4):
    a_button = format_coordinate(input_data[i], "+", 0)
    b_button = format_coordinate(input_data[i + 1], "+", 0)
    prize = format_coordinate(input_data[i+2], "=", 10000000000000)

    result += play(a_button, b_button, prize)
print(result)
