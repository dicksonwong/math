#Lexigraphic Permutations - Euler 24
#Dickson Wong
#Python 3.2.3
#------------------------------------------------------------------------------
def permutate(current, digits, all_numbers):
    '''Adds a new term to all if digits is empty; else iterate more permuations.'''
    
    #Add to all
    if (digits == []):
        all_numbers.append(current)
    else:
        
        #Iterate permutations
        for digit in digits:
            new_current = current
            new_current += digit
            new_digits = digits[:]
            new_digits.remove(digit)
            permutate(new_current, new_digits, all_numbers)
    
if __name__ == "__main__":
    int_digits = range(0, 10)
    digits = list()
    
    #Change to string (so we can permutate digits)
    for digit in int_digits:
        digits.append(str(digit))
        
    all_numbers = list()
    permutate("", digits, all_numbers)
    all_numbers.sort()
    print ("The millionth permutation is: ", all_numbers[999999])
        