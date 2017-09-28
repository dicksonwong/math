#Project Euler Problems

#Problem 1
def problem_1():
    '''Add all the natural numbers below one thousand that are multiples of 3 or 5.
    '''
    
    sum = 0
    
    for i in range(0,1000):
        if i % 5 == 0 or i % 3 == 0:
            sum = sum + i
            
    print sum

#Problem 2
def problem_2():
    '''By considering the terms in the Fibonacci sequence whose values do not exceed four million,
    find the sum of the even-valued terms.
    '''
    fib_seq = [1, 1]
    sum = 0
    
    #Appends values to the fibonnaci sequence as long as the last element is less than or equal to 4000000
    while fib_seq[-1] <= 4000000:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        
        #Checks to see if the last number in the sequence is even
        if fib_seq[-1] % 2 == 0:
            sum = sum + fib_seq[-1]
            
    print sum
        
#Problem 3
def break_down_number(n):
    '''Breaks down the number by creating a list of factors.  Returns a list of factors found.
    '''
    
    list_of_factors = []
    compare_n = n
    
    while n != 1:
        lowest = 1
        highest = lowest + 1000000
        
        #Goes through each number from lowest to highest to check if there are numbers that are primes of n
        for i in range(lowest, highest):
            
            #If i is a factor of n
            if n % i == 0:
                    list_of_factors.append(i)
                    n = n / i
            
    return [list_of_factors, n]
            
def is_prime(n):
    '''Returns a boolean stating if a number if prime or not
    '''
    
    #We'll divide our number by the smallest factors, since it will be faster that way; 
    # if we checked the smallest factors, it won't be divisible by the larger numbers anyway
    
    #We won't check 1 and n, because any number is divisible by 1 and itself
    for i in range(2, n):
        if n % i == 0:
            return False
        
    return True
    
def problem_3():
    '''Find the largest prime factor of a composite number - 600851475143.
    '''
    
    #Note that the solution for this is very iffy - break_down_number is questionable and probably will 
    # not work for all numbers
    really_big_number = 600851475143
    print break_down_number(really_big_number)
    
#Problem 4
def is_palindrome(n):
    '''Return True if an integer n is a palindrome
    '''
    
    string_n = str(n)
    
    #While the length of the string is still greater than 1
    while len(string_n) > 1:
        
        #Checks to see if the first letter is the same as the last letter
        if string_n[0] == string_n[-1]:
            string_n = string_n[1:-1]
        
        else:
            return False
        
    return True

#Problem 4    
def problem_4():
    '''Find the largest palindrome made from the product of two 3-digit numbers.
    '''
    
    list_palindromes = []
                     
    multiplier_1 = 999
    multiplier_2 = 999 
    
    #While we are still checking all the products of the changing multiplier_2 and changing multiplier_1
    while len(str(multiplier_1)) > 2:
        
        #While we are checking for all the products of the changing multiplier_2 and multiplier_1
        while len(str(multiplier_2)) > 2:
            
            #Checks to see if the product of the two multipliers is a palindrome or not
            if is_palindrome(multiplier_1 * multiplier_2) == True:
                list_palindromes.append(multiplier_1 * multiplier_2)
                
            multiplier_2 = multiplier_2 - 1
            
        multiplier_1 = multiplier_1 - 1
        
        #We want to do this so we don't multiply the same numbers again
        #To understand this, imagine a 2-d array of integers
        #Now if we checked 999 x 999, we would also check 999 x 998... 999 x 100
        #Meaning if we changed the first number to 998, it would be okay if we checked 998 x 998 ... 998 x 100
        #In other words, we cut diagonally across the square of the 2-d array
        multiplier_2 = multiplier_1
        
    list_palindromes.sort()
    list_palindromes.reverse()
    
    return list_palindromes[0]
    
#Problem 5
def check_remainderzero_two_to_nineteen(n):
    
    #Goes through each of the numbers from 2 through 19 to see if n is evenly divisible by them
    
    #Note: Changed range from (1, 21) to (190, 2, -1) - Everything is evenly divisible by 1 and its faster if we checked the larger numbers first
    #Note note: Change (20, 2, -1) to (19, 10, -1) - All the numbers we divide by 11 to 19 means we can already divide by every from 2 to 10
    #  This is because the factors we find from the numbers in 11 to 19 already include the factors of 2 to 10
    
    #Another note: we'll start with 19 since we are adding by 20 every time anyway
    for i in range(19, 10, -1):
        
        #Checks to see if n is evenly divisible by i
        if n % i != 0:
            return False
        
    return True
        
def problem_5():
    '''What is the smallest number divisible by each of the numbers 1 to 20?
    '''
    
    #For efficiency reasons, let's start at 20
    smallest_integer = 20
    
    #Check all the numbers
    while 1:
        
        #Checks to see if we have found the number
        if check_remainderzero_two_to_nineteen(smallest_integer) == True:
            return smallest_integer
        
        #For efficiency reasons, we will also add 20 every time
        smallest_integer = smallest_integer + 20

#Problem 6
def problem_6():
    '''What is the difference between the sum of the squares and the square of the sums?
    Find the difference between the sum of the squares of the first one hundred natural 
    numbers and the square of the sum.
    '''
    
    sum_of_squares = 0
    
    #Sorry, going to cheat a bit here -> n(n+1)/2
    square_of_sum = (100 * (100 + 1) * 0.5) ** 2

    #Goes through each of the natural numbers from 1 to 100 
    for i in range(1, 101):
        sum_of_squares += i ** 2
        
    print sum_of_squares
    print square_of_sum
    
    print "The difference is: ", sum_of_squares - square_of_sum
    return sum_of_squares - square_of_sum
    
#Problem 7
def is_prime_number_with_list(n, prime_numbers):
    '''Returns true iff n is not evenly divisible by all the numbers in the list
    prime_numbers
    '''

    #Very efficient compared to dividing all the natural numbers up to n;
    # This works because all numbers are created with prime numbers
    
    #Goes through each of the numbers is prime_numbers
    for item in prime_numbers:
        
        #checks to see if n is evenly divisible by item
        if n % item == 0:
            return False
        
    return True

def problem_7():
    '''What is the 10 001st prime number?
    '''
    
    list_of_primes = [2, 3, 5, 7, 11, 13]
    list_of_primes_without_two = [3, 5, 7 ,11, 13]
    
    number_to_check = 15
    
    #Adds more primes to the list if we still haven't found 10001 of them
    while len(list_of_primes_without_two) < 10000: 
    
        #Checks to see if number_to_check is a prime number
        if is_prime_number_with_list(number_to_check, list_of_primes_without_two) == True:
            
            list_of_primes_without_two.append(number_to_check)
            
        #for efficiency reasons, we'll add 2 instead of 1, since all even numbers are not prime
        number_to_check += 2
            
            
    return list_of_primes_without_two[-1]
    
#Problem 8
def product_of_digits(str_dig):
    '''Returns the product of all the digits in str_dig
    '''
    
    product = 1
    
    #Return 0 as soon as we know it will be 0
    if "0" in str_dig == True:
        return 0
            
    #Goes through each char in str_dig
    for char in str_dig:
        
        product = product * int(char)

    return product

def problem_8():
    '''Find the greatest product of five consecutive digits in the 1000-digit number.

73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450

'''
    
    list_of_products = []
    
    really_really_big = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
    
    #Goes through all the digits while the length is still 4
    while len(really_really_big) > 4:
        
        list_of_products.append(product_of_digits(really_really_big[0:5]))
        really_really_big = really_really_big[1:]
        
    list_of_products.sort()
    
    return list_of_products[-1]
        
#Problem 9
def problem_9():
    '''
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
    
    #We'll just assume we're working with natural numbers here -> there's probably a reason
    # why we must use them for pythagorean theorem - I'm not sure about the reason for this
    a = 1
    b = 2
    
    triplet = [0, 0, 0]
    
    #While we haven't found out what the triplet is
    while triplet == [0, 0, 0]:
        
        #While the relationship that a + b + c = 1000 is possible
        while a + b <= 1000 - a:
            
            #Figure out what c has to be if a, b, and c is a pythagorean triplet
            square_c = a ** 2 + b ** 2
            c = square_c ** 0.5
        
            #If we find out that the number of digits is greater than 3; in other words, if 
            # the total number of characters in the string c is greater than 5, then there's no way that c 
            # can be a natural number
            if len(str(c)) <= 5:
                
                #Check to see if a + b + c = 1000
                if a + b + c == 1000 :
                    triplet = [a, b, c]
                
            b = b + 1
            
        a = a + 1
        b = a + 1
        
    return triplet[0] * triplet[1] * triplet[2]
            
#Problem 10 - Oh god...
def problem_10():
    '''
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.
    '''
            
    #Note: Most of this code was compied from problem 7, as a result - is_prime_number_with_list is borrowed
    
    list_of_primes = [2, 3, 5, 7, 11, 13]
    list_of_primes_without_two = [3, 5, 7 ,11, 13]
    
    #We don't want to check 2 or 5 for efficiency reasons
    list_of_primes_no_five_two = [3, 7 ,11, 13]
    
    number_to_check = 15
    
    #Adds more primes to the list if we still haven't found all the ones less than two million
    while list_of_primes_no_five_two[-1] < 2000000: 
    
        #since 5 is common, it reduces our time to run
        if number_to_check % 5 !=0:
                
            #Checks to see if number_to_check is a prime number
            if is_prime_number_with_list(number_to_check, list_of_primes_no_five_two) == True:
            
                list_of_primes_no_five_two.append(number_to_check)
            
        #for efficiency reasons, we'll add 2 instead of 1, since all even numbers are not prime
        number_to_check += 2
            
    if list_of_primes_no_five_two[-1] > 2000000:
        list_of_primes.pop(-1)
            
    return sum(list_of_primes_without_two) + 2 + 5
    
    