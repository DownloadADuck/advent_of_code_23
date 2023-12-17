import re

# bool return if we have a part number or a special char
def is_part_number(char):
    return char.isdigit() or char in {'*', '+', '#', '%', '$', '/', '@', \
            '=', '-', '&'}

# return adjacent numbers for a coodrinate of the grid
def get_adjacent_numbers(grid, row, col):
    adjacent_numbers = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), \
            (1, -1), (1, 1)]

    # looks at every possible directions
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
            match = re.findall(r'(-?\d+)', grid[new_row][new_col])
            # if we have a number and not a special char we add it
            for num in match:
                adjacent_numbers.append(int(num))

    return adjacent_numbers

# main function
def sum_part_numbers(filename):
    with open(filename, 'r') as file:
        # vector of lines
        grid = [line.strip() for line in file]
        print("grid: ", grid)
    
    total_sum = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if is_part_number(grid[row][col]):
                match = re.findall(r'(-?\d+)', grid[row][col])
                for num in match:
                    total_sum += int(num)
                
                adjacent_numbers = get_adjacent_numbers(grid, row, col)
                print("adjacent numbers:", adjacent_numbers)
                total_sum += sum(adjacent_numbers)

    return total_sum

if __name__ == "__main__":
    input_filename = "test.txt"
    result = sum_part_numbers(input_filename)
    print("Sum of the part numbers:", result)
