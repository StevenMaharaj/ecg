import numpy as np

def LCG_alogorithm(a,b,m,seed = 2,iterations=20):
    """"
    Implements the LCG alogrithm 
    Outputs: an array of random numbers of size iterations x 1
    """
    x = np.zeros(iterations)
    x[0] = seed

    for i in range(1,iterations):
        x[i] = (a*x[i-1] + b)%m
    return x

def check_valid(x,m):
    """Checks if a sequence x is vaild
    
    Inputs: x - sequence
            m 
            
    Output : True if valid
             False if not valid"""
    n_non_repeating = np.argwhere(x[0] == x).flatten()[1] 
    if n_non_repeating==m-1:
        vaild = True
    else:
        vaild = False

    return vaild
    


def prob_of_two_sixs(x):
    """" Computes the empirical probablity of rolling two_sixs
    Inputs : x n x 1 numpy array of dice rolls 

    Outputs : empirical probablity of rolling two_sixs
    """

    sum_x_pair = x + np.roll(x,1)
    occurences = len(sum_x_pair[sum_x_pair==12])

    return occurences/len(x)




