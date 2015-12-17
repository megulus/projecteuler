# coding=utf-8
import sys
import math
#----------------------------------------------------------------------------------------------------------------------
"""
Problem 11: Largest product in a grid
In the 20 * 20 grid below, four numbers along a diagonal line have been marked in red.

08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

The product of these numbers is 26 * 63 * 78 * 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the
20 * 20 grid?
"""
def get_file_lines(filename):
    lines = []
    try:
        with open(filename, 'r') as my_file:
            for line in my_file:
                lines.append(line.rstrip())
        return lines
    except IOError:
        print "Unable to open file {}".format(filename)
        sys.exit()

def make_grid_dict(lines):
    row = -1
    grid_dict = {}
    for line in lines:
        row += 1
        line = line.split(' ')
        for index, item in enumerate(line):
            grid_dict[str(row)+str(index)] = int(item)
    return grid_dict

def get_grid_size(lines):
    grid_rows = len(lines)
    grid_cols = len(lines[0].split(' '))
    return grid_rows, grid_cols


def find_horizontal_testsets(numrows, numcols, grid_dict):
    horizontal = []
    for i in range(numrows):
        for j in range(numcols):
            if j <= numcols - 4:
                testset = [grid_dict[str(i)+str(j)], grid_dict[str(i)+str(j + 1)], grid_dict[str(i)+str(j + 2)], grid_dict[str(i)+str(j + 3)]]
                horizontal.append(testset)
    return horizontal

def find_vertical_testsets(numrows, numcols, grid_dict):
    vertical = []
    for i in range(numrows):
        for j in range(numcols):
            if i <= numrows - 4:
                testset = [grid_dict[str(i)+str(j)], grid_dict[str(i + 1)+str(j)], grid_dict[str(i + 2)+str(j)], grid_dict[str(i + 3)+str(j)]]
                vertical.append(testset)
    return vertical

def find_diagonal_downwards_testsets(numrows, numcols, grid_dict):
    diagonal = []
    for i in range(numrows):
        for j in range(numcols):
            if (i <= numrows - 4 and j <= numcols - 4):
                testset = [grid_dict[str(i)+str(j)], grid_dict[str(i + 1)+str(j + 1)], grid_dict[str(i + 2)+str(j + 2)], grid_dict[str(i + 3)+str(j + 3)]]
                diagonal.append(testset)
    return diagonal


def find_diagonal_upwards_testsets(numrows, numcols, grid_dict):
    diagonal = []
    for i in range(numrows):
        for j in range(numcols):
            if (i >= 3 and j <= numcols - 4):
                testset = [grid_dict[str(i)+str(j)], grid_dict[str(i - 1)+str(j + 1)], grid_dict[str(i - 2)+str(j + 2)], grid_dict[str(i - 3)+str(j + 3)]]
                diagonal.append(testset)
    return diagonal


def find_largest_product(filename):
    lines = get_file_lines(filename)
    grid_dict = make_grid_dict(lines)
    numrows, numcols = get_grid_size(lines)
    largest_product = 0
    answer = {}
    all_testsets = []
    horizontal = find_horizontal_testsets(numrows, numcols, grid_dict)
    all_testsets.extend(horizontal)
    vertical = find_vertical_testsets(numrows, numcols, grid_dict)
    all_testsets.extend(vertical)
    diagonal = find_diagonal_downwards_testsets(numrows, numcols, grid_dict)
    all_testsets.extend(diagonal)
    diagonal_up = find_diagonal_upwards_testsets(numrows, numcols, grid_dict)
    all_testsets.extend(diagonal_up)
    for each in all_testsets:
        answer, largest_product = evaluate_product(each, largest_product, answer)
    return answer



def evaluate_product(operand_list, largest_product, answer_dict):
    if len(operand_list) == 4:
        product = operand_list[0] * operand_list[1] * operand_list[2] * operand_list[3]
        if product > largest_product:
            largest_product = product
            answer_dict['operands'] = operand_list
            answer_dict['product'] = largest_product
            return answer_dict, largest_product
    return answer_dict, largest_product


#----------------------------------------------------------------------------------------------------------------------
'''
Problem 12: Highly divisible triangular number
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''

def count_factors(number):
    sqroot = math.sqrt(number)
    count = 0
    for i in xrange(1, int(math.floor(sqroot))):
        if number % i == 0:
            if number / i != i:
                count += 2
            else:
                count += 1
    return count

def get_triangle(n):
    return (n * (n + 1)) / 2


def find_highly_divisible_triangle(target):
    num_factors = 0
    n = 1
    while num_factors < target:
        triangle = get_triangle(n)
        num_factors = count_factors(triangle)
        if num_factors == target:
            print "The first triangle with {} factors is {}.".format(target, triangle)
        elif num_factors > target:
            print "The first triangle with more than {} factors is {}, with {} factors.".format(target, triangle, num_factors)
        else:
            n += 1


#----------------------------------------------------------------------------------------------------------------------
'''
Problem 13: Large Sum
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
[see 'large_number_problem_13.txt']
'''
def get_fifty_digit_numbers(lines):
    all_numbers = []
    number = ''
    for line in lines:
        for char in line:
            if len(number) == 50:
                all_numbers.append(int(number))
                number = ''
            number += char
    all_numbers.append(int(number))
    return all_numbers

def large_sum(filename):
    lines = get_file_lines(filename)
    numbers = get_fifty_digit_numbers(lines)
    sum_numbers = sum(numbers)
    first_ten = str(sum_numbers)[0:10]
    print "The first 10 digits of the sum are {}".format(first_ten)

#----------------------------------------------------------------------------------------------------------------------
'''
Problem 14: Longest Collatz Sequence

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been
proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

def get_next_collatz(n):
    if n % 2 == 0:
        return n / 2
    else:
        return (3 * n) + 1

def get_collatz_seq_length(start):
    count = 1
    term = start
    #print term, count
    while term > 1:
        term = get_next_collatz(term)
        count += 1
        #print term, count
    return count

def print_collatz_answer(ceiling, seq_start, seq_length):
    print "The longest Collatz sequence (starting under {}) starts with {} and has {} terms.".format(ceiling + 1, seq_start, seq_length)

def find_longest_collatz_seq(ceiling):
    longest = 0
    seq_start = 0
    for i in range(ceiling, 0, -1):
        seq_length = get_collatz_seq_length(i)
        if seq_length > longest:
            longest = seq_length
            seq_start = i
    print_collatz_answer(ceiling, seq_start, longest)

#----------------------------------------------------------------------------------------------------------------------
'''
Problem 15: Lattice Paths - Solution 1 (recursion - works, but time cost increases exponentially)

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly
6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
'''

def get_neighbor_vertices(vertex, max_x, max_y):
    # return the possible next vertices, allowing only across and down moves in the grid
    neighbors = []
    if vertex[0] + 1 <= max_x:
        neighbors.append([vertex[0] + 1, vertex[1]])
    if vertex[1] + 1 <= max_y:
        neighbors.append([vertex[0], vertex[1] + 1])
    #print neighbors
    return neighbors

def get_paths(all_paths, path_so_far, vertex, max_x, max_y):
    neighbors = get_neighbor_vertices(vertex, max_x, max_y)
    if len(neighbors) > 0:
        for neighbor in neighbors:
            path = path_so_far + [neighbor]
            if len(path) == max_x + max_y:
                all_paths.append(path)
            get_paths(all_paths, path, neighbor, max_x, max_y)
    else:
        #print all_paths
        return all_paths

def print_paths_answer(all_paths, max_x, max_y):
    print "There are {} possible routes to the bottom right corner of a {} x {} grid.".format(all_paths, max_x, max_y)

def count_grid_paths(max_x, max_y):
    all_paths = []
    path_so_far = [[0,0]]
    get_paths(all_paths, path_so_far, [0, 0], max_x, max_y)
    print_paths_answer(len(all_paths), max_x, max_y)

'''
Problem 15: Solution 2: dynamic programming

Using the fact that any position (vertex) in grid can only be reached from 1 left or 1 above

e.g.,

1  1  1  1
1  2  3  4
1  3  6  10
1  4  10 20

Each vertex is the sum of the vertex one above and one to the left.

'''

def initialize_paths(dict, x, y):
    for i in range(x + 1):
        line = ''
        for j in range(y + 1):
            dict[str(i) + str(j)] = 1
            line += '1 '
        #print line
    return dict

def calculate_paths(dict, x, y):
    for i in range(x + 1):
        line = ''
        for j in range(y + 1):
            if i - 1 < 0 or j - 1 < 0:
                num_paths = 1
            else:
                num_paths = dict[str(i-1) + str(j)] + dict[str(i) + str(j-1)]
            line += '  ' + str(num_paths)
            dict[str(i) + str(j)] = num_paths
        print line
    return dict


def count_paths(x, y):
    grid = {}
    grid = initialize_paths(grid, x, y)
    grid = calculate_paths(grid, x, y)
    total = grid[str(x) + str(y)]
    print_paths_answer(total, x, y)

#----------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------
def main():
    '''
    answer = find_largest_product('grid.txt')
    operands = answer['operands']
    product = answer['product']
    print "The largest product is {} * {} * {} * {} = {}".format(operands[0], operands[1], operands[2], operands[3], product)
    find_highly_divisible_triangle(500)
    large_sum('large_number_problem_13.txt')
    find_longest_collatz_seq(999999)
    '''
    count_paths(20, 20)


if __name__ == '__main__':
    main()







