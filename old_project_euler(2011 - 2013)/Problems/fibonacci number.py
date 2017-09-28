#Author: Dickson Wong
#NOTE: PYTHON 3.0 and above.
#------------------------------------------------------------------------------

#Fibonnaci number
'''
The Fibonacci sequence is defined by the recurrence relation:
 
Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.
 
Hence the first 12 terms will be:
 
F1 = 1
 F2 = 1
 F3 = 2
 F4 = 3
 F5 = 5
 F6 = 8
 F7 = 13
 F8 = 21
 F9 = 34
 F10 = 55
 F11 = 89
 F12 = 144
 
The 12th term, F12, is the first term to contain three digits.
 
What is the first term in the Fibonacci sequence to contain 1000 digits?
'''

#Not really needed
def num_digits(number):
    '''Returns the number of digits the string representation of the number has.
    '''
    return len(str(number))

if __name__ == "__main__":
    current_num = 1
    next_num = 1
    third_num = current_num + next_num
    count = 3 #Keeps track of which fib we're on
    
    #Note: first number to have 1000 digits is 10 ^ 999
    check = 10 ** 999
    while(third_num < (check)):
        current_num = next_num
        next_num = third_num
        third_num = current_num + next_num
        count += 1
    
    print ("the first term is: ", count)