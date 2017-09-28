#Square digit Chains:
#Euler 92
#------------------------------
'''A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44  32  13  10  1  1
85  89  145  42  20  4  16  37  58  89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?'''

def square_of_digits(number):
    '''(int) -> int
    Returns the square of all the digits of a number.'''
    num = str(number)
    digits_sum = 0

    for char in num:
        digits_sum += (int(char)) ** 2
        
    return digits_sum

def find_chain(number):
    '''(int) -> int
    Returns the whether the number chain will go to 1 or 89.
    '''
    current = number

    while((current != 1) and (current != 89)):
        current = square_of_digits(current)

    return current

if __name__ == "__main__":

    numbers = 1000000
    
    count = 0
    current = 1
    while(current < numbers):
        if (find_chain(current) == 89):
            count += 1

        current += 1

    print "The number of numbers under ", numbers, " that go to 89 is: ", count


