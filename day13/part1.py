import sys
import time

def format_coordinate(line, sign):
    x, y = map(lambda x: int(x.strip().split(sign)[1]), line.split(":")[1].split(","))
    return x, y

def is_possible(a_button, b_button, prize):
    is_x_reachable = prize[0] <= 100 * a_button[0] + 100 * b_button[0]
    is_y_reachable = prize[1] <= 100 * a_button[1] + 100 * b_button[1]

    return is_x_reachable and is_y_reachable

def play(a_button, b_button, prize):
    a_press = 0
    current_position = (0, 0)
    if is_possible(a_button, b_button, prize):
        while current_position != prize and a_press <= 100:
            distance_x = prize[0] - current_position[0]
            distance_y = prize[1] - current_position[1]
            if distance_x % b_button[0] == 0 and distance_y % b_button[1] == 0 and  distance_x / b_button[0] == distance_y / b_button[1]:
                b_press = int(distance_x / b_button[0])
                if b_press <= 100:
                    #print(prize, a_press, b_press, prize[0] == a_press * a_button[0] + b_press * b_button[0], prize[1] == a_press * a_button[1] + b_press * b_button[1])
                    return a_press * 3 + b_press
                else:
                    return 0
            else:
                a_press += 1
                current_position = (current_position[0] + a_button[0], current_position[1] + a_button[1])
    return 0




with open("input.txt", 'r') as f:
    input_data = f.readlines()

result = 0
for i in range(0, len(input_data), 4):
    a_button = format_coordinate(input_data[i], "+")
    b_button = format_coordinate(input_data[i + 1], "+")
    prize = format_coordinate(input_data[i+2], "=")

    result += play(a_button, b_button, prize)

print(result)


