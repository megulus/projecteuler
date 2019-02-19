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
'''
Problem 16: Power Digit Sum
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?
'''

def get_digits(number):
    return map(int, str(number))

def power_sum(base, exp):
    power = base**exp
    digits = get_digits(power)
    print_power_sum(base, exp, sum(digits))

def print_power_sum(base, exp, power_sum):
    print "The sum of the digits of {}^{} is {}.".format(base, exp, power_sum)

'''
Problem 17: Number Letter Counts
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and
115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with
British usage.

NOTE: This solution will only find number letter counts up to 9,999
'''

def word_dict():
    return { 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred', 1000: 'thousand' }


def word_builder(number):
    words = word_dict()
    word = ''
    if number <= 20:
        word += words[number]
    elif number > 20 and number < 100:
        tens = (number / 10) * 10
        word += words[tens]
        if number % 10 != 0:
            word += word_builder(int(str(number)[1:]))
    elif number >= 100 and number < 1000:
        hundreds = number / 100
        word += words[hundreds] + words[100]
        if number % 100 != 0:
            word += 'and' + word_builder(int(str(number)[1:]))
    elif number >= 1000 and number < 10000:
        thousands = number / 1000
        word += words[thousands] + words[1000]
        if number % 1000 != 0:
            word += word_builder(int(str(number)[1:]))
    #print number, word
    return word


def number_letter_counts(end_number):
    words = word_dict()
    count = 0
    for i in range(1, end_number + 1):
        count += len(word_builder(i))
        #print count
    print "There are {} total letters in the spelled-out numbers {} through {}".format(count, 'one', end_number)

#----------------------------------------------------------------------------------------------------------------------
'''
Problem 18: Maximum Path Sum 1

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from
top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

              75
             95 64
            17 47 82
           18 35 87 10
          20 04 82 47 65
         19 01 23 75 03 34
        88 02 77 73 07 63 67
       99 65 04 28 06 16 70 92
      41 41 26 56 83 40 80 70 33
     41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
   70 11 33 28 77 73 17 78 39 68 17 57
  91 71 52 38 17 14 91 43 58 50 27 29 48
 63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67,
is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a
clever method! ;o)
'''

class Node:
    def __init__(self, number, child1=None, child2=None):
        self.value = number
        self.child1 = child1
        self.child2 = child2
    def get_children(self):
        if self.child1 != None and self.child2 != None:
            return [self.child1, self.child2]
        else:
            return []

class Pseudotree:
    def __init__(self, list_of_lists):
        list_of_node_lists = []
        for each_list in list_of_lists:
            nodelist = [Node(item) for item in each_list]
            list_of_node_lists.append(nodelist)
        self.head = list_of_node_lists[0][0]
        for i in range(len(list_of_node_lists)):
            if i + 1 <= len(list_of_node_lists) - 1:
                parents = list_of_node_lists[i]
                children = list_of_node_lists[i + 1]
            for j in range(len(parents)):
                parent_node = parents[j]
                parent_node.child1 = children[j]
                parent_node.child2 = children[j + 1]



def make_list_of_lists(filename):
    lines = get_file_lines(filename)
    list_of_lists = []
    for line in lines:
        line = line.split(' ')
        line = [int(x) for x in line if x != '']
        list_of_lists.append(line)
    return list_of_lists



def extend_paths(node, all_sums_dict, addends_list):
    if node.get_children() != []:
        children = node.get_children()
        for child in children:
            new_addends_list = list(addends_list)
            new_sum = sum(new_addends_list)
            all_sums_dict[new_sum] = new_addends_list.append(child.value)
            extend_paths(child, all_sums_dict, new_addends_list)
    else:
        new_addends_list = list(addends_list)
        new_sum = sum(new_addends_list)
        all_sums_dict[new_sum] = new_addends_list
        #path_sum_so_far



def get_sums(head):
    all_sums = {}
    path_sum = head.value
    addends = [head.value]
    extend_paths(head, all_sums, addends)
    return all_sums


def test_tree(head):
    print "head", head.value, "children", head.child1.value, head.child2.value
    print "child1", head.child1.value, "children", head.child1.child1.value, head.child1.child2.value
    print "child2", head.child2.value, "children", head.child2.child1.value, head.child2.child2.value
    print "child1.child1", head.child1.child1.value, "children", head.child1.child1.child1.value, head.child1.child1.child2.value
    print "child1.child2", head.child1.child2.value, "children", head.child1.child2.child1.value, head.child1.child2.child2.value
    print "child2.child1", head.child2.child1.value, "children", head.child2.child1.child1.value, head.child2.child1.child2.value
    print "child2.child2", head.child2.child2.value, "children", head.child2.child2.child1.value, head.child2.child2.child2.value



def find_maximum_path_sum(filename):
    list_of_lists = make_list_of_lists(filename)
    pseudotree = Pseudotree(list_of_lists)
    head = pseudotree.head
    all_sums_dict = get_sums(head)
    largest = max(all_sums_dict.keys())
    addends = all_sums_dict[largest]
    addend_string = str(addends.pop(0))
    for addend in addends:
        addend_string += ' + ' + str(addend)
    print 'The largest path sum is {} = {}'.format(addend_string, largest)

#----------------------------------------------------------------------------------------------------------------------
'''
Problem 19: Counting Sundays
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

def get_next_weekday(current_weekday):
    # 0 = Sunday, 6 = Saturday
    if current_weekday == 6:
        return 0
    else:
        return current_weekday + 1

def next_date(current_date):
    current_month = current_date[0]
    current_day = current_date[1]
    current_year = current_date[2]
    if current_month == 2:
        if (current_year % 4 == 0 and current_year % 100 != 0) or (current_year % 100 == 0 and current_year % 400 == 0):
            if current_day == 29:
                current_day = 1
                current_month += 1
            else:
                current_day += 1
        else:
            if current_day == 28:
                current_day = 1
                current_month += 1
            else:
                current_day += 1
    elif current_month in [4, 6, 9, 11]:
        if current_day == 30:
            current_day = 1
            current_month += 1
        else:
            current_day += 1
    else:
        if current_day == 31 and current_month != 12:
            current_day = 1
            current_month += 1
        elif current_day == 31 and current_month == 12:
            current_day = 1
            current_month = 1
            current_year += 1
        else:
            current_day += 1
    return (current_month, current_day, current_year)

def translate_date(month, date, year):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    return (months.index(month) + 1, date, year)

def translate_weekday(weekday):
    weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    if weekday in weekdays:
        return weekdays.index(weekday)
    if type(weekday) == int:
        return weekdays[weekday]

def first_month_sunday(current_weekday, current_date):
    if current_weekday == 0 and current_date[1] == 1:
        return True

def count_first_month_sundays(start_weekday, start_month, start_date, start_year, end_month, end_date, end_year):
    current_weekday = translate_weekday(start_weekday)
    current = translate_date(start_month, start_date, start_year)
    end = translate_date(end_month, end_date, end_year)
    first_sundays = 0
    if first_month_sunday(current_weekday, current):
        first_sundays += 1
    while current != end:
        current_weekday = get_next_weekday(current_weekday)
        current = next_date(current)
        print translate_weekday(current_weekday), current, end
        if first_month_sunday(current_weekday, current):
            first_sundays += 1
    print "Between {} {}, {} and {} {}, {}, {} Sunday(s) fell on the 1st day of the month.".format(start_month, start_date, start_year, end_month, end_date, end_year, first_sundays)




#----------------------------------------------------------------------------------------------------------------------
'''
Problem 20: Factorial Digit Sum
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

'''


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
    count_paths(20, 20)
    power_sum(2, 1000)
    number_letter_counts(1000)
    find_maximum_path_sum('triangle.txt')
    '''
    count_first_month_sundays('Tuesday', 'January', 1, 1901, 'December', 31, 2000)


if __name__ == '__main__':
    main()







