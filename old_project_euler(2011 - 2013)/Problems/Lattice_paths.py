#Author: Dickson Wong
#NOTE: PYTHON 3.0 and above.
#------------------------------------------------------------------------------

'''Starting in the top left corner of a 22 grid, there are 6 routes (without backtracking) to the bottom right corner.
How many routes are there through a 20 x 20 grid?
'''
#We need something to keep track of how many times we have moved
#In the end, we need to move right 20 times and down 20 times
#So we need something to recurse the paths and make sure we move down once
#every time

#Data Type: Person
#Will keep track of how many times we have moved up or down
#Will keep track of how many times we need to move?

def move(num_paths, number_left):
        #checks to see if we need to move any further right
        if number_left[0] > 0:
            new_number_left = number_left[:]
            new_number_left[0] = new_number_left[0] - 1
            move(num_paths, new_number_left)
            
        elif number_left[1] == 0:
                num_paths[0] = num_paths[0] + 1

        #checks to see if we need to move any further down
        if number_left[1] > 0:
            new_number_left = number_left[:]
            new_number_left[1] = new_number_left[1] - 1
            move(num_paths, new_number_left)
        elif number_left[0] == 0:
                num_paths[0] = num_paths[0] + 1
                        
if __name__ == "__main__":
    num_paths = [0] #Keeps track of how many paths there are
    size = 12 #Size of square
    number_left = [size, size] #first tracks right, second tracks down
    move(num_paths, number_left)
    print ("the number of paths is: ", num_paths[0])
    
#we need a more efficient algorithm that encompasses this idea.
