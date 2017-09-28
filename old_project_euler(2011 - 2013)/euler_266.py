def pseudo_square_root(n):
    '''(int) -> List
    Returns the greatest divisor that is below the root(n).
    '''
    i = 1
    psr = 1

    while (i < int(n ** 0.5) + 1):
        if (int(float(n) / i) == (float(n) / i)):
           psr = i
        i += 1

    return psr

def is_prime_odd(n):
    '''Returns whehter n is a prime or not, assuming n is odd.
    '''
    for i in range(3, int(n ** 0.5) + 1, 2):
        if (int(float(n) / i) == (float(n) / i)):
            return False

    return True

def list_primes(n):
    '''Return all primes under n.'''
    primes = [2]
    for i in range(3, n + 1, 2):
        if is_prime_odd(i):
            primes.append(i)

    return primes

def product_items(list_a):
    '''Returns the product of all the items inside list_a.
    '''
    product = 1

    for item in list_a:
        product = product * item

    return product

#DOES NOT WORK XD -----------------------------------------------------------------------------------------------------------------------------------------------[

#Idea: if we keep multiplying the primes under 190, we will eventually get a divisor, as all divisors will be constructed from prime decomposition in primes
#in other words, keep multiplying the largest until it is greater than the square root
def psr(primes, number):
    '''Assuming that number is composed of primes in primes decomposition, let us try to find the psr by
    1. Find the closest divisor composed of only the biggest prime. (that is still under the root(n)
    2. Take that number found in 1 and keep multiplying it by primes right under the largest prime
    3. Repeat it (go from largest prime to smallest prime)'''
    pseudo_sr = 1
    square_root = int(number ** 0.5) + 1
    
    for i in range(len(primes) - 1, -1, -1):
        prime = primes[i]

        #Multiply
        while pseudo_sr <= square_root:
            pseudo_sr = pseudo_sr * prime

            if pseudo_sr > square_root:
                pseudo_sr = pseudo_sr / prime
                break

    return pseudo_sr
        
#DOES NOT WORK XD -----------------------------------------------------------------------------------------------------------------------------------------------]

if (__name__ == "__main__"):
    primes = list_primes(190)
    print primes
    product = product_items(primes)
    print product

    pseudo = psr(primes, product)

    print product ** 0.5
    mod = pseudo % (10 ** 16)

    print mod
