'''A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.'''

def distinct_combine(list_a, list_b):
    '''(list, list) -> list
    Takes all the distinct elements in both lists and returns a new list.
    '''
    new_list = []

    for element in list_a:
        new_list.append(element)

    for element in list_b:
        if element not in new_list:
            new_list.append(element)

    return new_list

def analyze_number(number):
    '''(str) -> list
    Takes a number and returns a list that describes for each number before it,
    what values can go before it.'''
    descriptions = list()

    #Parse the string
    for i in range(0, 3):

        description = [number[i]]
        characters_before = list()
        for j in range(0, i):
            characters_before.append(number[j])
        description.append(characters_before)
        descriptions.append(description)

    return descriptions

def analyze_digits(filename):
    '''(str) -> dict<int, list>
    Return a dict, key values that describe what numbers can go before
    it in a sequence (as the characters are always asked for in increasing order.
    '''
    digits_descriptions = dict()
    
    f = open(filename, "r")

    #Read the file and analyze number
    for line in f:
        descriptions = analyze_number(line)

        #Update descriptions to digits_descriptions
        for description in descriptions:

            num = description[0]
            defs = description[1]
            
            try:
                defs = distinct_combine(digits_descriptions[num], defs)
            except:
                digits_descriptions[num] = defs
            finally:
                digits_descriptions[num] = defs

    f.close()

    return digits_descriptions

def find_passcode(definitions):
    '''(list) -> string
    Finds the passcode, given the definitions based on the number of elements that can come before each digit.
    '''
    defs = definitions[:]

    passcode = ""
    
    current_min = len(defs[0][1])
    current_index = 0 

    print defs
    while(defs != []):

        #Find the number with the least number of characters that can come before it and append to passcode
        for i in range(0, len(defs)):
            description = defs[i]
            if (len(description[1]) < current_min):
                current_min = len(description[1])
                current_index = i

        passcode += defs[current_index][0]
        defs.pop(current_index)

        current_min = 1000
        current_index = 0

    return passcode
        
if __name__ == "__main__":
    descriptions = analyze_digits("keylog.txt")

    #Idea: assuming that each number has a distinct number of characters that can come before it,
    #then ie. we can put the characters in order of how many different characters can come before it.
    #That order will describe what passcode we need

    defs = descriptions.items()

    print "The passcode is: ", find_passcode(defs)
        
