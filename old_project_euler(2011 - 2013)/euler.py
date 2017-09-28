def is_prime_odd(number):
    '''Returns whether an number is a prime or not. This assumes that number is an odd number'''

    for factor in range(3, number ** 0.5 + 1, 2):
        if (number / factor) == int(number / factor):
            return False

    return True

def prime_decomposition(number, primes):
    '''Returns a list of prime factors of a number given a list of primes.'''

    factors = list()
    current = number

    #Finds the prime factors of number
    while (current != 1):

        #goes through the list of primes
        for prime in primes:

            #If current is divisible by prime
            if (current / prime) == int (current / prime):

                #Adds prime to the list if it is already not there
                if prime not in factors:
                    factors.append(prime)

                current = current / prime

    return factors
        
def is_distinct(list_a, list_b):
    '''Returns whether or not list_a has distinct elements in list_b'''
    #Goes through each item in list_a
    for item in list_a:

        #checks to see if item is in list_b
        if item in list_b:
            return False

    return True

def first_n_primes(n):
    '''Returns a list of the first n primes'''
    primes = [2]
    n = n - 1
    current = 3

    #Finds the first n primes
    while(n > 0):

        #checks to see if current is a prime or not
        if is_prime_odd(current):
            primes.append(current)
            n = n - 1

        current += 2
        
    return primes

def main():
    primes = first_n_primes(1000)

    #Tracker
    current = 647
    current_factors = prime_decomposition(current, primes)

    consecutive = 1

    while(consecutive < 4):

        next_factors = prime_decomposition(current + 1, primes)

        #Checks to see if they are consecutively distinct factors
        if is_distinct(current_factors, next_factors):

            #Checks to see if consecutive is 1 (is this the first number)
            if consecutive == 1:
                first = current
                
            consecutive += 1

        #Not distinct - reset
        else:
            consecutive = 1

        current += 1

        if (current > 1000):
            break

        current_factors = next_factors

    #The answer:
    print "the first number is: ", current
            
