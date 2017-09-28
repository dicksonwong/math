#Double Base Palindromes - Euler 36
#Dickson Wong
#Python 3.2.3
#------------------------------------------------------------------------------
def convert_from_base_ten(base, number):
    '''Converts a number in base ten and returns the number in the new base,
    base.'''
    new_number = ""
    quotient = 1
    
    #Uses the general algorithm to convert from base 10`
    while(quotient != 0):
        quotient = number / base
        remainder = number - quotient * base
        new_number = str(remainder) + new_number
        number = quotient
    
    return int(new_number)
    
def reverse(string):
    '''Return the reverse of a string.
    '''
    new_string = ""
    
    #Iterate through characters in string backwards
    for i in range(len(string) - 1, -1, -1):
        new_string += string[i]
        
    return new_string

def is_palindromic(number):
    '''Given a number, return whether or not that number is palindromic.
    Note that the question defines a palindromic number such that the last 
    digit of then number cannot be 0.
    '''
    str_number = str(number)
    
    #If the last digit is 0, then not palindromic
    if str_number[len(str_number) - 1] == "0":
        return False
    else:
        return (reverse(str_number) == str(number))
    
if __name__ == "__main__":
    num_palin = 0
    sum_nums = 0
    
    for i in range(0, 1000000):
    
        #check in palindromic in both bases
        if is_palindromic(i):
            if is_palindromic(convert_from_base_ten(2, i)):
                sum_nums += i
                
    print "The sum of all palindromic numbers in both bases is: ", sum_nums