import copy
import math
import sys
import time

def octal_to_dec(octal):
    print(octal)
    result = 0
    str_octal = str(octal)
    for i in range(1, len(str_octal)+1):
        result += int(str_octal[-i]) * math.pow(8, i-1)
    return int(result)


with open("input.txt", 'r') as f:
    input_data = f.readlines()

A = int(input_data[0].split(":")[1].strip())
B = int(input_data[1].split(":")[1].strip())
C = int(input_data[2].split(":")[1].strip())

program = list(map(lambda x: int(x.strip()), input_data[4].split(":")[1].strip().split(",")))

def to_combo(literal, current_reg):
    result = None
    if literal < 4:
        result = literal
    elif literal == 4:
        result = current_reg[0]
    elif literal == 5:
        result = current_reg[1]
    elif literal == 6:
        result = current_reg[2]
    return result


def adv(literal, index, current_reg):
    combo = to_combo(literal, current_reg)
    denominator = math.pow(2, combo)
    result = current_reg[0] / denominator
    current_reg[0] = int(result)
    return index + 2, None

def bxl(literal, index, current_reg):
    bit_wise = current_reg[1] ^ literal
    current_reg[1] = bit_wise
    return index + 2, None

def bst(literal, index, current_reg):
    combo = to_combo(literal, current_reg)
    current_reg[1] = combo % 8
    return index + 2, None

def jnz(literal, index, current_reg):
    a_register = current_reg[0]
    if a_register != 0:
        return literal, None
    else:
        return index + 2, None

def bxc(literal, index, current_reg):
    current_reg[1] = current_reg[1] ^ current_reg[2]
    return index+2, None

def out(literal, index, current_reg):
    return index + 2, to_combo(literal, current_reg) % 8

def bdv(literal, index, current_reg):
    combo = to_combo(literal, current_reg)
    denominator = math.pow(2, combo)
    result = current_reg[0] / denominator
    current_reg[1] = int(result)
    return index + 2, None

def cdv(literal, index, current_reg):
    combo = to_combo(literal, current_reg)
    denominator = math.pow(2, combo)
    result = current_reg[0] / denominator
    current_reg[2] = int(result)
    return index + 2, None


def get_out_value(registers):
    current_reg = copy.copy(registers)
    values = []
    index = 0
    while index < len(program) - 1:
        current_op = program[index]
        current_lit = program[index + 1]
        new_value = None
        if current_op == 0:
            new_index, new_value = adv(current_lit, index, current_reg)
        elif current_op == 1:
            new_index, new_value = bxl(current_lit, index, current_reg)
        elif current_op == 2:
            new_index, new_value = bst(current_lit, index, current_reg)
        elif current_op == 3:
            new_index, new_value = jnz(current_lit, index, current_reg)
        elif current_op == 4:
            new_index, new_value = bxc(current_lit, index, current_reg)
        elif current_op == 5:
            new_index, new_value = out(current_lit, index, current_reg)
        elif current_op == 6:
            new_index, new_value = bdv(current_lit, index, current_reg)
        elif current_op == 7:
            new_index, new_value = cdv(current_lit, index, current_reg)
        if new_value is not None:
            values.append(new_value)

        index = new_index
    return values

def get_out_value_memoize(registers, memoize):
    current_reg = copy.copy(registers)
    values = []
    index = 0
    while index < len(program) - 1:
        if (current_reg[0], current_reg[1], current_reg[2], index) in memoize:
            return values + memoize[(current_reg[0], current_reg[1], current_reg[2], index)]
        current_op = program[index]
        current_lit = program[index + 1]
        new_value = None
        if current_op == 0:
            new_index, new_value = adv(current_lit, index, current_reg)
        elif current_op == 1:
            new_index, new_value = bxl(current_lit, index, current_reg)
        elif current_op == 2:
            new_index, new_value = bst(current_lit, index, current_reg)
        elif current_op == 3:
            new_index, new_value = jnz(current_lit, index, current_reg)
        elif current_op == 4:
            new_index, new_value = bxc(current_lit, index, current_reg)
        elif current_op == 5:
            new_index, new_value = out(current_lit, index, current_reg)
        elif current_op == 6:
            new_index, new_value = bdv(current_lit, index, current_reg)
        elif current_op == 7:
            new_index, new_value = cdv(current_lit, index, current_reg)
        if new_value is not None:
            values.append(new_value)

        index = new_index
    return values

# start = time.time()
# iteration = octal_to_dec(30000000)
# registers = [iteration, B, C]
# values = []
# memoize = dict()
# while program != values:
#     iteration += 1
#     registers = [iteration, B, C]
#     if iteration % 1000000 == 0:
#         print(iteration)
#     values = get_out_value_memoize(registers, memoize)
#     memoize[(registers[0], registers[1], registers[2], 0)] = values
#
# print(round(time.time() - start, 2), "seconds")
# print(iteration)

#print(get_out_value([117440, B, C]))

target = [2,4,1,2,7,5,4,3,0,3,1,7,5,5,3,0]
print(target)


not_done = True

def octal_to_dec_lis(octal_list):
    result = 0
    str_octal = "".join(map(lambda x: str(x), octal_list))
    for i in range(1, len(str_octal) + 1):
        result += int(str_octal[-i]) * math.pow(8, i - 1)
    return int(result)

# index = 0
# octal_number = [0] * len(target)
# while not_done or index < len(target) or new_sol == target:
#     ok = False
#     start=octal_number[index]
#     for i in range(start, 8):
#         octal_number[index] = i
#         new_sol = get_out_value([octal_to_dec_lis(octal_number), B, C])
#         if new_sol[-(index+1)] == target[-(index+1)]:
#             index += 1
#             ok = True
#             break
#     if not ok:
#        while octal_number[index] == 7:
#            octal_number[index] = 0
#            index -= 1
#        octal_number[index] = octal_number[index] + 1
#     print(octal_number, new_sol, target)
# print(octal_number)

print(octal_to_dec_lis([5, 3, 2, 2, 3, 5, 3, 7, 0, 1, 2, 3, 6, 0, 1, 7]))


