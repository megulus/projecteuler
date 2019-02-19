'''
Gathering some of the functions that will be generally useful to solving the Project Euler problems.
'''

# read in a file line by line
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


def is_nonprime(anumber):
    '''
    because get_prime_factors is costly, this does a quick and dirty screen for NON-primeness before confirming that a number is truly prime. Most numbers will be pretty easily screened out, significantly lowering the number of candidates that need to be fully tested for primeness
    :param anumber: integer
    :return True or False
    '''
    for each in range(2, 14):
        if each != anumber:
            if anumber % each == 0:
                return True
    return False


# prime factors
def get_prime_factors(n):
    factor = 2
    factored = n
    n_factors = []
    n_factors.append(1)
    while reduce(mul, n_factors) < n:
        if factored % factor == 0:
            n_factors.append(factor)
            factored = factored / factor
        else:
            factor += 1
    return n_factors



# determine whether a number is prime
def is_prime(n):
    factors = get_prime_factors(n)
    if len(factors) == 2:
        return True
    else:
        return False


# find the Nth prime number
def find_nth_prime(n):
    primes = []
    current = 1
    while len(primes) < n:
        if is_prime(current):
            primes.append(current)
        current += 1
    return primes[-1]


# determine whether 3 numbers constitute a Pythagorean triple
def is_pythagorean(a, b, c):
    if (a < b and b < c) and (a**2 + b**2 == c**2):
        return True
    else:
        return False


