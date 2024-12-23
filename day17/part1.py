import math

with open("input.txt", 'r') as f:
    input_data = f.readlines()

A = int(input_data[0].split(":")[1].strip())
B = int(input_data[1].split(":")[1].strip())
C = int(input_data[2].split(":")[1].strip())

program = list(map(lambda x: int(x.strip()), input_data[4].split(":")[1].strip().split(",")))

registers = [A, B, C]

def to_combo(literal):
    result = None
    if literal < 4:
        result = literal
    elif literal == 4:
        result = registers[0]
    elif literal == 5:
        result = registers[1]
    elif literal == 6:
        result = registers[2]
    return result


def adv(literal, index):
    print("adv")
    combo = to_combo(literal)
    denominator = math.pow(2, combo)
    result = registers[0] / denominator
    registers[0] = int(result)
    return index + 2, None

def bxl(literal, index):
    print("bxl")
    bit_wise = registers[1] ^ literal
    registers[1] = bit_wise
    return index + 2, None

def bst(literal, index):
    print("bst")
    combo = to_combo(literal)
    registers[1] = combo % 8
    return index + 2, None

def jnz(literal, index):
    print("jnz")
    a_register = registers[0]
    if a_register != 0:
        return literal, None
    else:
        return index + 2, None

def bxc(literal, index):
    print("bxc")
    registers[1] = registers[1] ^ registers[2]
    return index+2, None

def out(literal, index):
    print("out")
    return index + 2, to_combo(literal) % 8

def bdv(literal, index):
    print("bdv")
    combo = to_combo(literal)
    denominator = math.pow(2, combo)
    result = registers[0] / denominator
    registers[1] = int(result)
    return index + 2, None

def cdv(literal, index):
    print("cdv")
    combo = to_combo(literal)
    denominator = math.pow(2, combo)
    result = registers[0] / denominator
    registers[2] = int(result)
    return index + 2, None



values = []
index = 0
while index < len(program) - 1:
    current_op = program[index]
    current_lit = program[index+1]
    print(index, registers, current_op, current_lit)
    new_value = None
    if current_op == 0:
        new_index, new_value = adv(current_lit, index)
    elif current_op == 1:
        new_index, new_value = bxl(current_lit, index)
    elif current_op == 2:
        new_index, new_value = bst(current_lit, index)
    elif current_op == 3:
        new_index, new_value = jnz(current_lit, index)
    elif current_op == 4:
        new_index, new_value = bxc(current_lit, index)
    elif current_op == 5:
        new_index, new_value = out(current_lit, index)
    elif current_op == 6:
        new_index, new_value = bdv(current_lit, index)
    elif current_op == 7:
        new_index, new_value = cdv(current_lit, index)
    if new_value is not None:
        values.append(new_value)

    index = new_index
print(index, registers, current_op, current_lit)
print(",".join(map(lambda x: str(x), values)))