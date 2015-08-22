from operator import *



#----------------------------------------------------------------------------------------------------------------------
'''
Problem 1: Multiples of three and five
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

def multiples_of_three_and_five(an_integer):
    '''
    :param an_integer: an integer
    :return: sum of all multiples of 3 or 5 less than an_integer
    '''
    sum_multiples = 0
    for each_int in range(an_integer):
        if each_int % 3 == 0 or each_int % 5 == 0:
            sum_multiples += each_int
    return sum_multiples


#----------------------------------------------------------------------------------------------------------------------
'''
Problem 2: Even Fibonacci Numbers
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''

def fib(n):
    '''
    on second thought, not using this b/c max recursion depth is exceeded when calculating this problem
    recursive fibonnaci function
    :param n: an integer > 0
    :return: the (n+1)th fibonacci term (if sequence begins with 0)
    '''
    if n < 0:
        return None
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fib(n - 1) + fib(n - 2)


def sum_even_fibonacci_rec(n):
    '''
    :param n: an integer
    :return: the sum of even-valued terms <= n in Fibonacci sequence
    '''
    sum_fib = 0
    i = 0
    fib_num = 0
    while fib_num <= n:
        fib_num = fib(i)
        i += 1
        if fib_num % 2 == 0:
            sum_fib += fib_num
    return sum_fib


def sum_even_fibonacci_it(n):
    '''
    replacing the recursive version b/c max recursion depth was exceeded
    :param n: an integer
    :return: sum of even-valued terms <= n in Fibonnaci sequence
    '''
    sum_fib = 0
    fib_num = 0
    one_previous = 1
    two_previous = 0
    while fib_num <= n:
        fib_num = one_previous + two_previous
        two_previous = one_previous
        one_previous = fib_num
        if fib_num % 2 == 0:
            sum_fib += fib_num
    return sum_fib

#----------------------------------------------------------------------------------------------------------------------

'''
Problem 3: Largest Prime Factor
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

def largest_prime_factor(n):
    factor = 2
    factored = n
    n_factors = []
    n_factors.append(1)
    while reduce(mul, n_factors) < n:
        #print n_factors, reduce(mul, n_factors), factored
        if factored % factor == 0:
            n_factors.append(factor)
            factored = factored / factor
        else:
            factor += 1
    return max(n_factors)

#----------------------------------------------------------------------------------------------------------------------


'''
Problem 4: Largest Palindrome Product
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

def is_palindrome_it(digits):
    digits_copy = list(digits)
    while len(digits_copy) > 1:
        if digits_copy[0] == digits_copy[-1]:
            digits_copy.pop(0)
            digits_copy.pop(-1)
        else:
            return False
    return True



def is_palindrome(digits):
    digits_copy = list(digits)
    if len(digits_copy) <= 1:
        return True
    else:
        first = digits_copy.pop(0)
        last = digits_copy.pop(-1)
        if first == last:
            if is_palindrome(digits_copy):
                return True
            else:
                return False
        else:
            return False



def largest_palindrome_product(lowerbound, upperbound):
    '''
    return the largest palindrome product of numbers in range lowerbound - upperbound
    :param: lowerbound - lower bound of range
    :param: upperbound - upper bound of range
    :return: largest palindromic product of two three-digit numbers
    '''
    maxproduct = 0
    result = {}
    for i in range(lowerbound, upperbound):
        for j in range(lowerbound, upperbound):
            product = i * j
            digits = map(int, str(product))
            if product > maxproduct:
                if is_palindrome_it(digits):
                    maxproduct = product
                    result['maxproduct'] = maxproduct
                    result['factor1'] = i
                    result['factor2'] = j
    return result




#----------------------------------------------------------------------------------------------------------------------












#----------------------------------------------------------------------------------------------------------------------

def main():
    # Problem 1:
    n = 1000
    multsum = multiples_of_three_and_five(n)
    print 'sum of multiples of three and five below {}: {}'.format(n, multsum)
    # Problem 2:
    n = 4000000
    fibs = sum_even_fibonacci_it(n)
    print 'sum of even fibonnaci numbers less than {}: {}'.format(n, fibs)
    # Problem 3:
    n = 600851475143
    largest_prime = largest_prime_factor(n)
    print 'largest prime factor of {}: {}'.format(n, largest_prime)
    lower = 100
    upper = 1000
    result = largest_palindrome_product(lower, upper)
    print 'largest palindrome product of factors between {} and {} is: {} x {} = {}'.format(lower, upper, result['factor1'], result['factor2'], result['maxproduct'])






if __name__=='__main__':
    main()