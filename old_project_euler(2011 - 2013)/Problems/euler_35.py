#Circular Primes - Euler 35
#Dickson Wong
#Python 2.7.2
#------------------------------------------------------------------------------
#Goal: Find the most efficient algorithm for finding primes

def is_factor_of(number, factor):
    '''Returns whether factor really is factor of number or not.
    '''
    result = float(number) / factor
    return (int(result) == result)

#The following uses a list of already existing primes to help determine whether this is a prime or not
def is_prime(number, primes):
    '''Returns whether number is a prime number or not, depending on the list
    of primes given.  We assume that primes is really the list of all primes
    less than number.
    '''
    #Iterate through numbers in primes
    for i in range(0, len(primes) - 1):
        
        #Check to see if it is necessary to check
        if (primes[i] <= int(number ** 0.5) + 1):
            if is_factor_of(number, primes[i]):
                return False
        else:
            break

    return True

def list_primes(n):
    '''Return a list of all primes from 2 to n inclusive.
    '''
    primes = [2]
    
    current = 3
    
    #Find all primes less than or equal to n
    while (current <= n):
        if is_prime(current, primes):
            primes.append(current)
        current += 2
            
    return primes
    
if __name__ == "__main__":
    primes = list_primes()
    print primes[len(primes) - 1]