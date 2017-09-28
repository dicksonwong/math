#Maximum path sums
#Author Dickson Wong
#------------------------------------------------------------------------------
def form_triangle(filename):
    '''Takes a filename for some triangle an returns a list of rows.
    '''
    triangle = []
    
    f = open(filename, "r")
    
    #Go through each line
    for line in f:
        row = line.split() #Note that they are strings
        triangle.append(row)
        
    f.close()
    
    return triangle

def find_max_sum(triangle):
    '''Finds the maximum path by finding the largest number in each row (adjacent only).
    '''
    index = 0
    num_sum = 0

    #adds the largest adjacent number in each row
    for i in range(0, len(triangle)):
        row = triangle[i]
        
        try:
            left_num = int(row[index])
        except:
            left_num = 0
            
        try:
            right_num = int(row[index + 1])
        except:
            right_num = 0
            
        #If the left adjacent number is larger
        if (left_num > right_num):
            num_sum += left_num
            
        #The right adjacent is larger
        else:
            num_sum += right_num
            index += 1
            
            
    return num_sum
        
def problem_18():
    '''Simple Max Sum I'''
    triangle = form_triangle("triangle_18.txt")
    max_sum = find_max_sum(triangle)
    print "The max sum is: ", max_sum
    
def problem_67():
    '''Max Sum II'''
    triangle = form_triangle("triangle_67.txt")
    max_sum = find_max_sum(triangle)
    print "The max sum is: ", max_sum
    
if __name__ == "__main__":
    problem_18()
    problem_67()
    