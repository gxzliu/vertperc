# *******************************************************
# vertperc
# george liu
# date: 4.3.16
# functions read/write matrices, generate flow matrices,
# return bool if percolates, randomly generate matrices
# *******************************************************

import numpy as np

def read_file(infile):
    """
    Create a site vacancy matrix represented as a numpy array 
    from a text file with the name infile_name.
    """
    invalue = open(infile, 'r')
    #read the first line, which contains # of col/rows
    dimension = int(invalue.readline())
    listvalue = []
    
    #reads the content, cleans, and appends to listvalue
    content = invalue.read().rstrip('\n').split()
    listvalue.append(content)  
    
    #strips each values of the quotations surrounding them
    cleanvalue = [[int(i) for i in l] for l in listvalue]
    
    #adds cleavalue to array and shapes array
    a = np.array(cleanvalue)
    a.shape = (dimension, dimension)
        
    return a
 
 
def write_file(outfile,sites):
    """
    Write a site vacancy matrix from the numpy array sites 
    to a file of name outfile. 
    """
    
    outval = open(outfile, 'w')
    #prints out # of col/rows first
    print(sites.shape[0], file = outval)

    #go thru each row in matrix
    for row in range(sites.shape[0]):
        content = ""
        #go thru each value in each row and add to string
        content = ' '.join([str(int(i)) for i in sites[row]]) + ' '
        print(content, file = outval)
    outval.close()


def vert_flow(sites):
    """
    Returns a flow matrix of vacant/full sites (1=full, 0=vacant) 
    generated through vertical percolation based on the 
    site vacancy matrix in the numpy array sites.
    """
    dimension = len(sites)
    
    content = []
    
    #first line will always be the same so add to list
    for line in sites[0:1]:        
        content.append(line)

    #goes through the rest of the rows
    for row in range(dimension-1):
        flow = []
        reached = False
        #goes through column values within the rows
        for col in range(dimension):
            #flows thru if, along w value below, has same value 1
            if (content[row][col] == sites[row + 1][col]):
                if (content[row][col] == 1):
                    reached = True
                else: 
                    reached = False
            else:
                reached = False
            
            #if reached, add 1 to the flow list
            if reached:
                flow.append(1)
            else:
                flow.append(0)
        content.append(flow)
    
    #create array from list
    sol = np.array(content)
    sol.shape = (dimension,dimension)
    return sol


def percolate(matrix):
    """ 
    Returns a boolean if the matrix numpy array exhibits percolation
    """
    #looks at last row to see if there are ones
    #if there are then returns true
    sol = False
    n = len(matrix)
    sol = bool(sum(matrix[n-1])>0)
    return(sol)
          
    
def make_matrix(n,p):
    """
    Returns an numpy array representing an nxn site vacancy 
    matrix w/ site vacancy prob p
    """
    
    #creates a random array with n*n dimensions
    matrix = np.random.rand(n*n)
    matrix.shape = (n,n)
    matrix = matrix < p
    #makes sure matrix is 0/1 not T/F
    matrix = matrix.astype(int)
    
    return matrix


    

    
    
