#Project Euler Problem 20
import re
import media

def factorial(n, facts):
    '''(int, dict) -> int
    Return n!, using facts, a dictionary of factorials'''
    try:
        return facts[n]
    except(KeyError):
        
        #Then find it.
        if n == 0:
            return 1;
        else:
            return n * factorial(n - 1, facts);
            

def sum_of_digits(n):
    '''int -> int
    Return the sum of all the digits occuring in n.
    '''
    string_n = str(n);
    sum = 0;
    for char in string_n:
        sum += int(char);
    
    return sum;

def problem_20(facts):
    '''n! means n  (n  1)  ...  3  2  1

    For example, 10! = 10  9  ...  3  2  1 = 3628800,
    and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

    Find the sum of the digits in the number 100!'''
    print sum_of_digits(factorial(100, facts));
    
def combination (n, r, facts):
    '''Returns nCr, given a dictionary facts of factorials'''
    n_fact = factorial(n, facts);
    facts[n] = n_fact
    r_fact = factorial(r, facts);
    facts[r] = r_fact
    sub_fact = factorial(n - r, facts);
    facts[n - r] = sub_fact
    
    return n_fact / r_fact / sub_fact
    
def problem_53(facts):
    '''How many, not necessarily distinct, values of  nCr, for 1  n  100, are greater than one-million?
    recall nCr = n! / (r!(n-r)!)
    '''
    count = 0
    for n in range (1, 101):
        for r in range(1, n + 1):
            if combination(n, r, facts) > 1000000:
                count += 1
    print count
    
    
def sum_of_digits_facts(n, facts):
    '''Adds up the sum of the factorials of the digits of a number n.
    '''
    sum = 0
    for char in str(n):
        sum += facts[int(char)]
    return sum

def problem_34(facts):
    '''145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.'''

    #Adds some base elements:
    for i in range(0, 10):
        facts[i] = factorial(i, facts)
        
    curious = list()
    #Guess: numbers over 5000 000 have no chance of being a curious number
    for i in range(10, 50000):
        if i == sum_of_digits_facts(i, facts):
            curious.append(i)
            print i
            
    sum = 0
    for number in curious:
        sum += number
        
    print sum
    
def problem_63():
    '''The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
'''
    #idea: instead of checking each integer, go the other way around; take every 10th power or so of a number
    numbers = list()
    
    #Once we go over 10, its ridiculous
    for i in range(1, 10):
        #Check say 25 powers
        for j in range(1, 25):
            if (len(str(i**j)) == j):
                if (i**j not in numbers):
                    numbers.append(i**j)
            
    print numbers
    print len(numbers)
    
def build_nine_digit_number(number):
    '''Given an integer, puts placeholder zeroes at the front and returns
    a string that is now nine digits'''
    return ("0" * (9 - len(number))) + number

def problem_206_2():
    '''Concealed Square: Find the unique positive integer whose square has the 
    form 1_2_3_4_5_6_7_8_9_0,
    where each “_” is a single digit.'''
    #This time, try instead to iterate through the possible choices of the 
    #digits and see if the square of the number is an integer.
    
    #First, we build a list of possible "replacement digits" (9 placements)
    numbers = range(0, 999999999)
    
def problem_206_1():
    '''Concealed Square: Find the unique positive integer whose square has the 
    form 1_2_3_4_5_6_7_8_9_0,
    where each “_” is a single digit.'''
    pattern = re.compile("1\d2\d3\d4\d5\d6\d7\d8\d9\d0\d")
    
    #First, we can figure the range of the numbers:
    #At the very least, the square will be 1020304050607080900
    #and at the very most, the square will be 1929394959697989990
    #this will reduce our range of numbers to be the square root of those.
    min_number = 1020304050607080900 ** 0.5
    max_number = 1929394959697989990 ** 0.5
    
    #Of course, we only want to check integers, so we have to check
    #1929394959697989990 ** 0.5 - 1020304050607080900 ** 0.5 = 378925613 numbers
    #Note: almost 400 million numbers
    
    #But because the last digit is a 0, then we know that for sure, the 
    #integer itself has to end with a 0 -ie. its a multiple of 10
    
    #Because the first digit is a 1, my guess is that the number also starts
    #with a 1
    
    #Well, this reduces alot :D
    i = int(min_number)
    while i < 2000000001:
        if pattern.match(str(i**2)):
            print i
            break
        
        #Because the last digit is a 10
        i = i + 10

def find_divisors(n):
    '''Returns a list of all the divisors of n'''
    divisors = list()
    #If the number is even:
    if n % 2 == 0:
        for i in range(1, n + 1):
            if n % i == 0:
                divisors.append(i)
    else:
        for i in range(1, n + 1, 2):
            if n % i == 0:
                divisors.append(i)
    return divisors

def sum_of_list(L):
    '''Returns the sum of all the values in L'''
    sum = 0
    for number in L:
        sum += number
    return sum

def sum_proper_divisors(n, proper_dict):
    '''Takes the sum of all the proper divisors of n (divisors that are less than
    n'''
    divisors = find_divisors(n)
    proper_divisors = divisors[0: len(divisors) - 1]
    proper_dict[n] = sum_of_list(proper_divisors)
    
def problem_21(sum_of_proper):
    '''Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''
    sum_of_proper = dict()
    sum_of_amicable = 0
    for i in range(1, 10000):
        #a = i
        #b = sum_of_proper[i]
        sum_proper_divisors(i, sum_of_proper)
        sum_proper_divisors(sum_of_proper[i], sum_of_proper)
        
        #d(a)
        sum_pd_1 = sum_of_proper[i]
        
        #d(b)
        sum_pd_2 = sum_of_proper[sum_of_proper[i]]

        #Checks to see if the sum of the proper divisors are the same
        if i == sum_pd_2: 
            if sum_pd_1 == sum_of_proper[i]:
                if i != sum_of_proper[i]:
                    print i
                    print sum_of_proper[i]
                    sum_of_amicable += i 
                    sum_of_amicable += sum_of_proper[i]
    sum_of_amicable = sum_of_amicable / 2
    print sum_of_amicable
    
def calculate_name_score_letter(name, score):
    '''Returns the "name score" of a name based on the position of the alphabet.
    Note that this doesn't consider position that the name is on the list of 
    all the name; but rather, it only considers the
    individual letters in the name.'''
    sum = 0
    
    #Adds to sum
    for char in name:
        sum += score[char]
    
    return sum

def remove_quotes(name):
    '''If name is in format "NAME", returns only NAME'''
    return name[1: len(name) - 1]

def words_in_file(filename):
    '''Takes in a filename and returns a list of words inside that file,
    where the format of the file is:
    "WORD","WORD","WORD",...,"WORD"'''
    f = open(filename, "r")
    text = f.read()
    f.close()

    #Note: unsorted list
    words = text.split(",")
    
    return words
    
def sort_names(filename):
    '''Takes a file of names inside a text and returns a sorted list''' 
    #Gets a list of unsorted names
    unsorted_names = words_in_file(filename)
    
    sorted_names = []
    sorted_names.append(remove_quotes(unsorted_names.pop()))
    
    while unsorted_names != []:
        name = remove_quotes(unsorted_names.pop())
        
        #Binary sort(?)
        low = 0
        high = len(sorted_names) - 1
        
        #If the new name belongs in the first index
        if name < sorted_names[low]:
            sorted_names.insert(low, name)
        
        #If the new name belongs in the last index
        elif name > sorted_names[high]:
            sorted_names.append(name)
            
        #Somewhere in the middle
        else:
            added = False
            while not added:
                mid = (low + high) / 2
                
                #Checks to see if it belongs after or before mid
                if name < sorted_names[mid]:
                    
                    #Checks if it is directly to the left of mid
                    if name > sorted_names[mid - 1]:
                        sorted_names.insert(mid, name)
                        added = True
                    else:
                        high = mid
                        
                #It belongs after mid
                else:
                    
                    #Checks if it is directly to the right of mid
                    if name < sorted_names[mid + 1]:
                        sorted_names.insert(mid + 1, name)
                        added = True
                    else:
                        low = mid
    return sorted_names
    
def problem_22(score):
    '''Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938  53 = 49714.

What is the total of all the name scores in the file?'''
    filename = media.choose_file()
    names = sort_names(filename)
    
    total_scores = 0
    
    #Remember that the score of a name is (position of name in score) x (letter_score)
    for i in range(1, len(names) + 1):
        total_scores += (i * calculate_name_score_letter(names[i - 1], score))
        
    print total_scores
    
    
def problem_23(sum_of_proper):
    #Abundant Sums
    '''A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''
    abundant_nums = list()
    for i in range(0, 28123 + 1):
        sum_proper_divisors(i, sum_of_proper)
        if sum_of_proper[i] > i:
            abundant_nums.append(i)
    print abundant_nums
        
def digital_sum(number):
    '''Takes in integer number and returns the digital sum (sum of all the digits)
    '''
    digits = str(number)
    sum = 0
    
    #adds up all of the digits in the number
    for char in digits:
        sum += int(char)
        
    return sum

def problem_56():
    '''A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b  100, what is the maximum digital sum?'''
    largest = 0
    for a in range(1, 100):
        for b in range(1, 100):
            number = digital_sum(a ** b)
            if number > largest:
                largest = number
    print largest

def concatenate_number(current, list_of_numbers, list_of_digits):
    '''If list_of_digits has only one element left, add the number to list_of_numbers.
    Otherwise, create a new string for every possible character in list_of_digits
    '''
    if len(list_of_digits) == 1:
        list_of_numbers.append(current + str(list_of_digits[0]))
    else:
        for char in list_of_digits:
            new_list = list_of_digits[:]
            new_list.remove(char)
            concatenate_number(current + str(char), list_of_numbers, new_list)
    
#Explanation:
'''Because we are only using only digits from 1 to n, and n is the maximum
number of digits, then it is only possible to use 1 to n as digits, hence,
the list_of_digits.'''

def pandigital_numbers(num_digits):
    '''Returns a list of all the pandigital(problem 41) numbers given the number
    of digits involved.'''
    list_of_digits = range(1, num_digits + 1)
    list_of_numbers = []
    concatenate_number("", list_of_numbers, list_of_digits[:])
    return list_of_numbers
    
def is_prime(number):
    '''Returns whether the number is prime or not'''
    #If the number is even, then no - unless the number is 2
    #But let's assume the number is not two -
    if number > 2:
        
        if number % 2 == 0:
            return False
        
        else:
            #Check all the numbers up till the square root
            #Recall: rational: suppose number = a*b - then one of a and b must be less than the square root
            #Hence, we will always find both factors a and b even if we check numbers less than the square root
            #Remember: if the square root is float, then just round down
            for factor in range(3, int(number ** 0.5) + 1, 2):
                if number % factor == 0:
                    return False
            return True
        
    else:
        if number == 2:
            return True
        
        #If it is 1 or less, then it must not be prime
        else:
            return False
            
            
def problem_41():
    '''We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?'''
    largest = 0
    #Check each pandigital prime to see if it is a prime
    for num_digits in range(9, 0, -1):
        list_of_numbers = pandigital_numbers(num_digits)
        
        #Sort it first with python first(obv - use python XD)
        list_of_numbers.sort()
        
        #Now start from the end:
        for i in range(len(list_of_numbers) - 1, 0, -1):
            if is_prime(int(list_of_numbers[i])):
                largest = list_of_numbers[i]
                print largest
                break
            
        #If we found the number
        if largest != 0:
            break
        
def quadratic_solutions(a, b, c):
    '''Returns solution to ax^2 + bx + c'''
    #Check discriminant b^2 - 4ac
    discriminant = b ** 2 - 4*a*c
    
    #If there are no solutions
    if discriminant < 0:
        return []
    
    #Otherwise:
    else:
        return [((-1) * (b) + discriminant ** 0.5) / (2.0 * a), 
                ((-1) * (b) - discriminant ** 0.5) / (2.0 * a)]
    
def solutions_triangle(number):
    '''Returns the solutions to the equation .5(n)(n+1) = number.'''
    return quadratic_solutions(0.5, 0.5, -1 * number)

def is_triangle_word(word, letter_score):
    '''Returns whether a word is triangle or not
    A triangle word is a word such that: if we add the numberical values of
    all the letters, then the result is a triangle number: 0.5(n)(n+1) for some 
    natural number n.'''
    #Recall: letter_score is a dictionary that keys every alphabet letter to its
    #        "score" - position
    score = calculate_name_score_letter(word, letter_score)
    solutions = solutions_triangle(score)
    
    #If there were no solutions, then it couldn't have been a triangle number
    if solutions == []:
        return False
    else:
        
        #Check to see if we have natural number solution
        if (int(solutions[0]) == solutions[0]) or (int(solutions[1]) == solutions[1]):
            return True
        else:
            return False
        
def problem_42(score):
    '''The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?'''
    words = words_in_file(media.choose_file())
    
    #Counts the number of triangle words in the file
    count = 0
    for word in words:
        if is_triangle_word(remove_quotes(word), score):
            count += 1
    print count
    
def create_primes(number_iterations):
    '''Creates a list of primes that checks the first (number_itaerations) odd
    numbers'''
    primes = [2, 3]
    i = 5
    
    #Iterates to find primes
    while i < number_iterations:
        
        #Checks to see if i is a prime or not
        if is_prime(i):
            primes.append(5)
        i += 2
    
def quadratic_value(a, b, c, x):
    '''Return ax^2 + bx + c'''
    return (a * (x ** 2)) + (b * x) + c

def number_of_consecutive_primes(b, c):
    '''Returns the number of primes that can be generated by the equation
    x^2 + bx + c; for example, n^2 + n + 41 would return 40, as primes are
    generated by values x = 0 to x = 39'''
    #Iterates through x
    x = 0
    count = 0
    
    #While we have prime numbers
    while(is_prime(quadratic_value(1, b, c, x))):
        count += 1
        x += 1
        
    return count

def problem_27():
    '''Euler published the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

Using computers, the incredible formula  n²  79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

n² + an + b, where |a|  1000 and |b|  1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.'''
    #Keep track of the values of a and b that create the largest number of primes
    largest_a = 0
    largest_b = 0
    largest_num_primes = 0
    
    #goes through each combination of |a| < 1000 and |b| < 1000
    for a in range(-999, 1000):
        for b in range(-999, 1000):
            num_primes = number_of_consecutive_primes(a, b)
            
            #Checks to see if we have more primes than the largest currently
            if num_primes > largest_num_primes:
                largest_a = a
                largest_b = b
                largest_num_primes = num_primes
    
    print "a: ", largest_a
    print "b: ", largest_b
    print "primes: ", largest_num_primes
    print "axb: ", largest_a * largest_b
    
def problem_29():
    '''Consider all integer combinations of ab for 2  a  5 and 2  b  5:

22=4, 23=8, 24=16, 25=32
32=9, 33=27, 34=81, 35=243
42=16, 43=64, 44=256, 45=1024
52=25, 53=125, 54=625, 55=3125
If they are then placed in numerical order, with any repeats removed, we get the following sequence of 15 distinct terms:

4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

How many distinct terms are in the sequence generated by ab for 2  a  100 and 2  b  100?'''
    list_of_terms = list()
    
    #Goes through each a from 2 to 100
    for a in range(2, 101):
        
        #Goes through each b from 2 to 100
        for b in range(2, 101):
            
            num = a ** b
            if not (num in list_of_terms):
                list_of_terms.append(num)
                
    print "Terms: ", len(list_of_terms)

def fifth_power_sums(number):
    '''Adds up the fifth powers of all the digits of a number'''
    sum = 0

    #Adds up all the fifth powers
    for char in str(number):
        sum += int(char) ** 5
        
    return sum
        
def problem_30():
    '''Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.'''
    #Checks each number to see if they can be written as a sum of the fifth powers of their digits
    #Idea: the maximum power is going to be 9^5 - which is 59049.
    #Well, we will not have to check numbers that are more than 300000, as
    #  6 times 59049 is already 300000
    numbers = list()
    for number in range(10, 300000):
       
        #Check to see if the fifth power sums is the number
        if number == fifth_power_sums(number):
            numbers.append(number)
            
    print "Sum of numbers: ", sum_of_list(numbers)
    
def construct_fractional_part_irrational(iterations):
    '''Create the irrational decimal fraction up to (iterations) digits in the
    fractional part of the number'''
    number = ""
    
    #Iterate through each integer and concatenate to the number
    for i in range(1, iterations):
        number += str(i)
        
    return number


def problem_40():
    '''An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1x  d10 x d100 x d1000x d10000xd100000x  d1000000'''
    fractional_part = construct_fractional_part_irrational(200000)
    count = 1
    number = 1
    
    #Multiply number seven times and interate count
    for i in range(0, 7):
        number = number * int(fractional_part[count - 1])
        count = count * 10
        
    print number
    
def problem_24():
    '''A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?'''
    
    
def construct_rows_triangle(filename):
    '''Given the triangle defined in "filename", construct a list that contains
    each row in the proper order given.  The first row has 1 terms.  The next 
    row has 2 terms, etc.'''
    rows = []
    
    #This is the filename - triangle
    f = open(filename, "r")
    numbers_text = f.read()
    f.close()
    
    #parse the numbers
    numbers = numbers_text.split()
    
    #Construct the rows
    row_size = 1
    numbers_index = 0
    
    while(true):
        current_elements = 0
        new_row = list()
        
        #Construct each row
        while row_size != current_elements:
            new_row.append(numbers_index)
            numbers_index += 1
            current_elements += 1
            
        rows.append(new_row)
        row_size += 1
        
    return rows

def problem_18():
    '''By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

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

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)'''
    filename = "triangle_18.txt"
    rows = construct_rows_triangle(filename)
    
    sum = 0
    index = 0
    
    #Idea: as we have to find the maximum path, we should just keep track of the index
    #      and then add the largest adjacent number in the next row
    #Note: this assumes that the max number in a row will not appear adjacently
def floor(number):
    '''Takes the floor of a number (integer that is smaller or = to the number
    right beside it)'''
    #int(number) functions the same as floor(number)
    return int(number)

def ceiling(number):
    '''Returns the ceiling of the number (integer that is equal or greater than
    the number right beside it)'''
    #Equal case
    if int(number) == number:
        return number
    
    #Round up case
    else:
        return int(number) + 1
    
def is_prime_list(number, primes):
    '''Does the same thing as is_prime, but checks the list given first.'''
    #Check list, otherwise check numbers up till root(number)
    if number in primes:
        return True
    else:
        return is_prime(number)
    
def is_prime_faster(number):
    '''Returns whether the number is prime or not.  This method is essentially
    the same as is_prime, except that it assumes that the number is greater than
    2 and it is odd.'''
    #Note: This is the most efficient of all the is_prime methods so far, as
    #it makes all the assumptions possible (at least most efficient of checking
    #up till the square roots method
    
    
    #Check all the numbers up till the square root
    #Recall: rational: suppose number = a*b - then one of a and b must be less than the square root
    #Hence, we will always find both factors a and b even if we check numbers less than the square root
    #Remember: if the square root is float, then just round down
    for factor in range(3, int(number ** 0.5) + 1, 2):
        if number % factor == 0:
            return False
        
    return True

def sum_prime_square_check(number, squares, primes):
    '''Given a list of squares and primes, see if number can be written
    as twice of some square in squares and some prime in primes.'''
    #Iterate through each square
    for square in squares:
        
        twice_square = 2 * square
        #Because we are assuming that squares is ordered, then we have not found a proper sum
        if twice_square > number:
            break
        else:
            possible_prime = number - twice_square
            
            #Check if we have a prime
            if possible_prime in primes:
                return True
            
    #We went through all the squares and did not find a proper sum
    return False
            
def problem_46():
    '''It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 212
15 = 7 + 222
21 = 3 + 232
25 = 7 + 232
27 = 19 + 222
33 = 31 + 212

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?'''
    #Creates a list of squares up till 1 million
    squares = list()
    for i in range(1, 1001):
        squares.append(i ** 2)
        
    #Algorithm:
    #1. Iterate through each composite number (until we find the one we want)
    #2. For each number, subtract twice of each square to check every time if we get a prime or not
        #If for one square, we get a prime, then it can be written as prime + 2 (square)

    primes = [2, 3, 5]
    number = 7
    while(True):
        
        #If the number is a prime number, then add it to the list of primes
        if is_prime_faster(number):
            primes.append(number)
            
        else:
            #If it is not, then we check the squares
            if not sum_prime_square_check(number, squares, primes):
                print primes
                print squares
                print number
                break
            
        number += 2
        
def reverse(string):
    '''Takes a string and returns a reversed version of that string.'''
    reversed = ""
    
    #Go through each letter in reverse order (of string)
    for i in range(len(string) - 1, -1, -1):
        reversed += string[i]
        
    return reversed
    

def is_palindrome(string):
    '''Returns whether a string is a palindrome or not
    Note: a string is a palindrome if it is the same as its reverse.
    '''
    return reverse(string) == string


def is_lychrel_number(number):
    '''Returns whether a number is a Lychrel number or not.  For our purposes,
    (problem 55), a Lychrel number is a number that does not become a palindrome
    in less than fifty iterations of adding itself with its reverse.'''
    
    #49 iterations at most
    for i in range(1, 50):
        
        #Check to see if the sum of a number and its reverse is palindromic
        sum = number + int(reverse(str(number)))
        if is_palindrome(str(sum)):
            return False
        
        #Repeat the same process, but use the sum as the new number
        number = int(sum)
        
    #We've gone through 49 iterations, so it is Lychrel number
    return True

def list_of_divisors(number):
    '''Return a list of divisors for a number.
    '''
    divisors = list()
    
    #The algorithm is similar to that of checking if it is a prime number or not
    for factor in range(1, int(number ** 0.5) + 1):
        
        #Check if divisible
        if number % factor == 0:
            divisors.append(factor)
            divisors.append(number / factor)
            
    return divisors

def problem_12():
    '''The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

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

What is the value of the first triangle number to have over five hundred divisors?'''
    #Go through each triangle number by iterating the next natural number
    triangle = 1 #current Triangle number
    current = 2 #Current natural number
    divisors = [1] #current list of divisors
    
    #Find the first triangle number with over 500 divisors
    while len(divisors) <= 500:
        triangle += current
        current += 1
        divisors = list_of_divisors(triangle)
        
    print "The first triangle number with over 500 divisiors is: ", triangle, " with ", len(divisors), " divisors."
        


def problem_55():
    '''If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. A number that never forms a palindrome through the reverse and add process is called a Lychrel number. Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise. In addition you are given that for every number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome. In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).

Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.

How many Lychrel numbers are there below ten-thousand?

NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature of Lychrel numbers.'''
    count = 0
    
    #Check all the numbers from 0 to 9999
    for i in range(0, 10000):
        
        #check if the number is Lychrel
        if is_lychrel_number(i):
            count += 1
            
    print "There are: ", count, " Lychrel numbers under 10000."
    
    
def last_ten_digits(number):
    '''Return an integer representation of the last ten digits of a number.
    '''
    string = str(number)
    
    #Check to see if the string is already less than 10 digits
    if len(string) <= 10:
        return number

    #Shave off the front part
    else:
        return int(string[len(string) - 10: len(string)])
    
    
def problem_97():
    '''The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne prime of the form 269725931; it contains exactly 2,098,960 digits. Subsequently other Mersenne primes, of the form 2p1, have been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433 x 2^7830457 + 1.

Find the last ten digits of this prime number.'''
    #Large non-Mersenne prime
    
    #Idea: only the last 10 digits matter anyway
    number = 28433
    count = 7830457 #Number of times that we need to multiply by 2
    
    #Find the first number that is 10 digits
    while len(str(number)) < 10:
        number = number * 2
        count -= 1
        
    digits = number
    #From now on, only keep the first 10 digits
    #Idea: shave off the front part as they don't matter anyway
    while count > 0:
        digits = digits * 2
        count -= 1
        digits = last_ten_digits(digits)
        
    digits += 1
    
    print "Last ten digits: ", digits

def problem_28():
    '''Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?'''
    #Idea is this: We add the numbers only on the edges; 
    #Notice that in the 3x3 square, we add numbers that have a distance of 2 from each other
    #Notice that in the 5xt square, we add numbers that have a distance of 4 together;
    #If you draw out the remaining spirals, you will notice that the distance increases by 2 every time
    #Thus, we need to keep track of our distance until the size is bigger than 1001
    #ie. we add (1) -> (3 + 5 + 7 + 9) -> (13, 17, 21, 25) -> ...
    #Also keep in mind that we only add 4 numbers
    
    #Algorithm:
    #1.Keep track of which square, how many numbers we have added, and the current natural number
    #2.Add until we have finished the 1001 square
    current_square = 3 #size of square (ie m x m)
    current_natural = 1
    sum = 1
    distance = 2 #distance between each number in square to add
    
    #Keep summing
    while(current_square <= 1001):
        to_add = 4 #Number of numbers to add in the square
        
        #Add 4 numbers in each square
        while(to_add > 0):
            current_natural += distance
            sum += current_natural
            to_add -= 1
            
        distance += 2
        current_square += 2 #Goes by 2s
        
    print "The sum is: ", sum
    
if __name__ == "__main__":
    f_dict = dict()
    sum_of_proper = dict()
    #problem_34(f_dict)
    #problem_63()
    #problem_206_1()
    #problem_21(sum_of_proper)
    #problem_23(sum_of_proper)
    
    #For problem 22: creates a dictionary that matches each letter to a score
    letter_score = range(1, 27) 
    score = dict()
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for j in letter_score:
        score[letters[j - 1]] = j
        
    #problem_22(score)
    
    #problem_56()
    #problem_41()
    #problem_42(score)
    #problem_27()
    #problem_29()
    #problem_30()
    #problem_40()
    
    #problem_46()
    #problem_55()
    #problem_12()
    #problem_97()
    problem_28()