word = "XMAS"

# does not work, cannot change direction
def find_xmas_occ(grid, y_index, x_index, index_letter):
    result = 0

    if index_letter == len(word): # we are at the end of the word
        return 1

    if y_index > 0 and word[index_letter] == grid[y_index-1][x_index] :
        result += find_xmas_occ(grid, y_index-1, x_index, index_letter+1)

    if y_index > 0 and x_index > 0  and word[index_letter] == grid[y_index-1][x_index-1]:
        result += find_xmas_occ(grid, y_index-1, x_index-1, index_letter+1)

    if  y_index > 0 and x_index < len(grid[0])-1 and word[index_letter] == grid[y_index-1][x_index+1]:
        result += find_xmas_occ(grid, y_index-1, x_index+1, index_letter+1)

    if x_index < len(grid[0])-1 and word[index_letter] == grid[y_index][x_index+1]:
        result += find_xmas_occ(grid, y_index-1, x_index+1, index_letter+1)

    if  x_index > 0 and word[index_letter] == grid[y_index][x_index-1]:
        result += find_xmas_occ(grid, y_index, x_index-1, index_letter+1)

    if y_index < len(grid)-1 and word[index_letter] == grid[y_index+1][x_index] :
        result += find_xmas_occ(grid, y_index+1, x_index, index_letter+1)

    if y_index < len(grid)-1 and x_index > 0 and word[index_letter] == grid[y_index+1][x_index-1]:
        result += find_xmas_occ(grid, y_index+1, x_index-1, index_letter+1)

    if y_index < len(grid)-1 and x_index < len(grid[0])-1 and word[index_letter] == grid[y_index+1][x_index+1] :
        result += find_xmas_occ(grid, y_index+1, x_index+1, index_letter+1)

    return result

def find_left(grid, y_index, x_index, index_letter):
    if index_letter == len(word): # we are at the end of the word
        return 1
    if x_index > 0:
        if grid[y_index][x_index-1] == word[index_letter]:
            return find_left(grid, y_index, x_index - 1, index_letter + 1)
        #elif grid[y_index][x_index - 1] == word[index_letter-1]:
        #    return find_left(grid, y_index, x_index - 1, index_letter)
        else:
            return 0
    else:
        return 0

def find_right(grid, y_index, x_index, index_letter):
    if index_letter == len(word): # we are at the end of the word
        return 1
    if x_index < len(grid[0])-1:
        if grid[y_index][x_index+1] == word[index_letter]:
            return find_right(grid, y_index, x_index + 1, index_letter + 1)
        #elif grid[y_index][x_index+1] == word[index_letter-1]:
        #    return find_right(grid, y_index, x_index + 1, index_letter)
        else:
            return 0
    else:
        return 0

def find_up(grid, y_index, x_index, index_letter):
    if index_letter == len(word): # we are at the end of the word
        return 1
    if y_index > 0:
        if grid[y_index-1][x_index] == word[index_letter]:
            return find_up(grid, y_index-1, x_index, index_letter+1)
        #elif grid[y_index-1][x_index] == word[index_letter-1]:
        #    return find_up(grid, y_index - 1, x_index, index_letter)
        else:
            return 0
    else:
        return 0

def find_down(grid, y_index, x_index, index_letter):
    if index_letter == len(word): # we are at the end of the word
        return 1
    if y_index < len(grid)-1:
        if grid[y_index+1][x_index] == word[index_letter]:
            return find_down(grid, y_index+1, x_index, index_letter+1)
        #elif grid[y_index+1][x_index] == word[index_letter-1]:
        #    return find_down(grid, y_index + 1, x_index, index_letter)
        else:
            return 0
    else:
        return 0

def find_top_right(grid, y_index, x_index, index_letter):
    if index_letter == len(word): # we are at the end of the word
        return 1
    if x_index < len(grid[0])-1 and y_index > 0:
        if grid[y_index-1][x_index+1] == word[index_letter]:
            return find_top_right(grid, y_index-1, x_index+1, index_letter+1)
        #elif grid[y_index-1][x_index+1] == word[index_letter-1]:
        #    return find_top_right(grid, y_index-1, x_index+1, index_letter)
        else:
            return 0
    else:
        return 0

def find_down_right(grid, y_index, x_index, index_letter):
    if index_letter == len(word): # we are at the end of the word
        return 1
    if x_index < len(grid[0])-1 and y_index < len(grid)-1:
        if grid[y_index+1][x_index+1] == word[index_letter]:
            return find_down_right(grid, y_index+1, x_index+1, index_letter+1)
        #elif grid[y_index+1][x_index+1] == word[index_letter-1]:
        #    return find_down_right(grid, y_index + 1, x_index + 1, index_letter)
        else:
            return 0
    else:
        return 0

def find_down_left(grid, y_index, x_index, index_letter):
    if index_letter == len(word): # we are at the end of the word
        return 1
    if x_index > 0 and y_index < len(grid)-1:
        if grid[y_index+1][x_index-1] == word[index_letter]:
            return find_down_left(grid, y_index+1, x_index-1, index_letter+1)
        #elif grid[y_index+1][x_index-1] == word[index_letter-1]:
        #    return find_down_left(grid, y_index + 1, x_index - 1, index_letter)
        else:
            return 0
    else:
        return 0

def find_top_left(grid, y_index, x_index, index_letter):
    if index_letter == len(word): # we are at the end of the word
        return 1
    if x_index > 0 and y_index > 0:
        if grid[y_index-1][x_index-1] == word[index_letter]:
            return find_top_left(grid, y_index-1, x_index-1, index_letter+1)
        #elif grid[y_index-1][x_index-1] == word[index_letter-1]:
        #    return find_top_left(grid, y_index-1, x_index-1, index_letter)
        else:
            return 0
    else:
        return 0

with open("input.txt", 'r') as f:
    input_data = f.readlines()

grid=[]
for line in input_data:
    grid.append(line.strip())

global_result = 0
for j in range(len(input_data)):
    for i in range(len(grid[j])):
        if grid[j][i] == word[0]:
            result = 0
            result += find_right(grid, j, i, 1)
            result += find_left(grid, j, i, 1)
            result += find_up(grid, j, i, 1)
            result += find_down(grid, j, i, 1)
            result += find_top_right(grid, j, i, 1)
            result += find_down_right(grid, j, i, 1)
            result += find_down_left(grid, j, i, 1)
            result += find_top_left(grid, j, i, 1)
            global_result += result

print(global_result)