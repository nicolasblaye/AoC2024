import sys
import time


with open("input.txt", 'r') as f:
    input_data = f.readlines()

width = 101
height = 103

robots = []
for line in input_data:
    p, v = line.split(" ")
    p, v = p.split("=")[1], v.split("=")[1]
    p_x, p_y = list(map(lambda x: int(x), p.strip().split(",")))
    v_x, v_y = list(map(lambda x: int(x), v.strip().split(",")))

    # after 100 moves
    p_x = (p_x + 100 * v_x) % width
    p_y = (p_y + 100 * v_y) % height

    robots.append((p_x, p_y))

top_left = []
top_right = []
bottom_left = []
bottom_right = []
for robot in robots:
    x, y = robot
    if x < int(width / 2) and y < int(height / 2):
        top_left.append(robot)
    elif x > int(width / 2) and y < int(height / 2):
        top_right.append(robot)
    elif x < int(width / 2) and y > int(height / 2):
        bottom_left.append(robot)
    elif x > int(width / 2) and y > int(height / 2):
        bottom_right.append(robot)

print(len(top_left) * len(top_right) * len(bottom_right) * len(bottom_left))