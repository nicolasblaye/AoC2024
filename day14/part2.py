import sys
import time


with open("input.txt", 'r') as f:
    input_data = f.readlines()

width = 101
height = 103

grid = [[' '] * width for _ in range(height)]

def print_grid(grid, f, seconds):
    for x in range(len(grid[0])):
        count = 0
        for y in range(len(grid)):
            if grid[y][x] == 'x':
                count += 1
                if count == 10:
                    f.write("\n" + "".join(["*"] * width) + "\n")
                    f.write("Time Elapsed: " + str(seconds) + "\n")
                    for line in grid:
                        f.write("".join(line) + "\n")
                    return
            else:
                count = 0



with open("tree.txt", "w+") as f:
    robots = []
    for line in input_data:
        p, v = line.split(" ")
        p, v = p.split("=")[1], v.split("=")[1]
        p_x, p_y = list(map(lambda x: int(x), p.strip().split(",")))
        v_x, v_y = list(map(lambda x: int(x), v.strip().split(",")))

        grid[p_y][p_x] = "x"
        robots.append((p_x, p_y, v_x, v_y))

    seconds = 0
    while seconds < 10000:
        grid = [[' '] * width for _ in range(height)]
        seconds += 1
        new_robot = []
        for robot in robots:
            p_x, p_y, v_x, v_y = robot
            p_x = (p_x + v_x) % width
            p_y = (p_y + v_y) % height
            new_robot.append((p_x, p_y, v_x, v_y))
            grid[p_y][p_x] = "x"
        robots = new_robot
        print_grid(grid, f, seconds)

