#! /usr/bin/env python
#encoding:UTF-8

'''Problem 47'''
'''Distinct primes factors'''

import time

def is_prime_odd(number):
    '''Returns whether an number is a prime or not. This assumes that number is an odd number'''

    for factor in range(3, int(number ** 0.5) + 1, 2):
        result = float(number) / factor
        if result == int(result):
            return False

    return True

def prime_decomposition(number, primes):
    '''Returns a list of prime factors of a number given a list of primes.  Note
    that the list returns a list of lists that each contain the prime factor, and
    the number of times the factors occurs.'''

    factors = list()
    current = number

    #If the number itself is a prime number
    if number in primes:
        return [[number, 1]]
    
    #Finds the prime factors of number
    while (current != 1):

        #goes through the list of primes
        for prime in primes:

            result = float(current) / prime
            #If current is divisible by prime
            if int(result) == result:

                in_list = False
                
                #Checks all the factors in prime
                for factor in factors:
                    
                    #If we find the factor
                    if (factor[0] == prime):
                        factor[1] += 1
                        in_list = True
                        break
                
                #If the factor is not in the list
                if not in_list:
                    factors.append([prime, 1])
            

                current = current / prime

    return factors
        
def prime_decomposition_dict(number, primes):
    '''Same as prime_decomposition, but uses a dictionary to keep track
    of the factors.'''
    factors = dict()
    current = number

    #If the number itself is a prime number
    if number in primes:
        return [[number, 1]]
    
    #Finds the prime factors of number
    while (current != 1):

        #goes through the list of primes
        for prime in primes:

            result = float(current) / prime
            #If current is divisible by prime
            if int(result) == result:

                #In the dict
                if prime in factors:
                    factors[prime] += 1
                else:
                    factors[prime] = 1
  
                current = current / prime

    return factors.items()

def is_a_factor_of(number, factor):
    '''Returns whether factor is a factor of number.  ie. Whether factors divides
    perfectly into factor.'''
    result = float(number) / factor
    #Checks if it divides into it
    if result == int(result):
        return True
    else:
        return False
    
def prime_decomposition_dict_smart_decomp(number, primes):
    '''Same as prime_decomposition, but uses a dictionary to keep track
    of the factors.  The decomposition used only goes through each prime once
    and ensures all the number of times are found.'''
    #If the number itself is a prime number
    if number in primes:
        return [[number, 1]]
    
    factors = dict()
    
    i = 0 #keeps track of which prime to check
    
    #Finds the prime factors of number
    while (number != 1):

        prime = primes[i]
        
        #Checks if it divides into it once
        if is_a_factor_of(number, prime):
            factors[prime] = 1
            number = number / prime
            
            #Finds the number of times prime divides into number after the first time
            while(is_a_factor_of(number, prime)):
                factors[prime] += 1
                number = number / prime
            
        i += 1
            
    return factors.items()

def is_distinct(list_a, list_b):
    '''Returns whether or not list_a has distinct elements in list_b'''
    #Goes through each item in list_a
    for item in list_a:

        #checks to see if item is in list_b
        if item in list_b:
            return False

    return True

def has_distinct_elements(lists):
    '''Returns the number of distinct elements in all the lists combined.'''
    added = list()
    distinct = 0
    
    #Go through each list
    for decomposition in lists:
        for factors in decomposition:
            
            #checks to see if we have counted the number already
            if not factors in added:
                added.append(factors)
                distinct += 1
                
    return distinct

def first_n_primes(n):
    '''Returns a list of all the primes up to n.'''
    primes = [2]
    current = 3

    #Finds the first n primes
    while(current <= n + 1):

        #checks to see if current is a prime or not
        if is_prime_odd(current):
            primes.append(current)

        current += 2
        
    return primes

'''Problem:
The first two consecutive numbers to have two distinct prime factors are:

14 = 2  7
15 = 3  5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2 ^ 2  7  23
645 = 3  5  43
646 = 2  17  19.

Find the first four consecutive integers to have four distinct primes factors. What is the first of these numbers?
'''

if __name__ == "__main__":
    #--------------------------[
    #Testing for TOTAL time and FIRST_N_PRIME
    total_time = 0
    #--------------------------]
    
    real_start_time = time.clock()
    
    prime_start = time.clock()
    numbers = 200000
    primes = first_n_primes(numbers)
    prime_end = time.clock()
    
    #Tracker
    first = 2
    current = first

    #--------------------------[
    #Testing for DECOMP
    decomp_time = 0
    #--------------------------]
    
    
    start_time = time.clock()
    while(current < numbers):
        
        #Check to see if the first list even has 4 primes in its decomposition
        a = time.clock()
        current_factors = prime_decomposition_dict_smart_decomp(current, primes)
        b = time.clock()
        decomp_time += (b-a)
        
        if len(current_factors) == 4:
             
            a = time.clock()
            #check the next number
            next_factors_a = prime_decomposition_dict_smart_decomp(current + 1, primes)
            b = time.clock()
            decomp_time += (b-a)
        
            if len(next_factors_a) == 4:
                
                a = time.clock()
                #check the next number
                next_factors_b = prime_decomposition_dict_smart_decomp(current + 2, primes)
                b = time.clock()
                decomp_time += (b-a)
                                
                if len(next_factors_b) == 4:
                    
                    a = time.clock()
                    #check the last number
                    next_factors_c = prime_decomposition_dict_smart_decomp(current + 3, primes)
                    b = time.clock()
                    decomp_time += (b-a)
                    
                    print current + 3, next_factors_c
                    if len(next_factors_c) == 4:
                        all_factors = []
                        all_factors.append(current_factors)
                        all_factors.append(next_factors_a)
                        all_factors.append(next_factors_b)
                        all_factors.append(next_factors_c)
                        print all_factors
                    
                        #Need to check if each list has 4 distinct factors
                        if has_distinct_elements(all_factors):
                            print "The first number is: ", current
                            break
                    #The last 4 does not contain what we wanted
                    else:
                        current += 4
                
                #The last 3 did not contain what we wanted
                else:
                    current += 3
                    
            #The last 2 did not contain what we wanted
            else:
                current += 2
            
        #The last did not contain what we wanted
        else:
            current += 1
        
    end_time = time.clock()
    real_end_time = time.clock()
    
    print "Process completed; everything took: ", real_end_time - real_start_time
    print "Decomp check finished. This took (seconds): ", end_time - start_time
    print "We checked numbers from: ", first, " to ", numbers
    print "Finding primes took: ", prime_end - prime_start
    print "Decomposition time taking: ", decomp_time
    
#Speed checks: for 2 - 20000
#1: Normal List decomp: 62 seconds
#2: Dictionary decomp: 56 seconds
#3: Dictionary decomp + skipping indices (no overlap in checks (current in the main)): 54s
#4: dictionary decomp + skipping indices + decomp check: 53s
#5: Dictionary Decomp (smart method) + skipping indices + decomp check: 6.7s

#Findings:
#the time.clock() doesn't really seem to affect the speed at all -> good job, python developers
#ie. the testing isn't affecting the performance at all
#The smart method I is way faster.

#I will not include the things that don't include much (decomp check, skipping indices)
#Speed checks: for 2 - 60000
#1. Dictionary Decomp(smart I) - 47.7s
#2. Same as one, but moved the while check over (only keep dividing if it is a factor in the first place) - 29.8s
