from mat import *
from vec import *
from cancer_data import *
import matutil
from matutil import listlist2mat
from vec import scalar_mul
## Task 1 ##
def signum(u):
    '''
    Input:
        - u: Vec
    Output:
        - v: Vec such that:
            if u[d] >= 0, then v[d] =  1
            if u[d] <  0, then v[d] = -1
    Example:
        >>> signum(Vec({1,2,3},{1:2, 2:-1})) == Vec({1,2,3},{1:1,2:-1,3:1})
        True
    '''
    v = u
    for d in v.D:       
        if u[d] >= 0:
            v[d] = 1
        else:
            v[d] = -1
    return v

## Task 2 ##
def fraction_wrong(A, b, w):
    '''
    Input:
        - A: a Mat with rows as feature vectors
        - b: a Vec of actual diagnoses
        - w: hypothesis Vec
    Output:
        - Fraction (as a decimal in [0,1]) of vectors incorrectly
          classified by w
          b = [1,1,1,1,1]
    '''
    
    result = signum(A*w)
    numerator = [result.f[i] == b[i] for i in result.f].count(False)
    answer = numerator/len(b.D)
    return answer
'''
>>> A = listlist2mat([[10, 7, 11, 10, 14], [1, 1, 13, 3, 2], [6, 13, 3, 2, 6], [10, 10, 12, 1, 2], [2, 1, 5, 7, 10]])
>>> A
Mat(({0, 1, 2, 3, 4}, {0, 1, 2, 3, 4}), {(1, 2): 13, (3, 2): 12, (0, 0): 10, (3, 0): 10, (0, 4): 14, (1, 4): 2, (1, 3): 3, (2, 3): 2, (2, 1): 13, (2, 4): 6, (4, 2): 5, (1, 0): 1, (0, 3): 10, (4, 0): 2, (0, 1): 7, (3, 3): 1, (4, 1): 1, (3, 1): 10, (4, 4): 10, (0, 2): 11, (2, 0): 6, (4, 3): 7, (2, 2): 3, (3, 4): 2, (1, 1): 1})
>>> b = list2vec([1, 1, -1, -1, 1])
>>> b
Vec({0, 1, 2, 3, 4},{0: 1, 1: 1, 2: -1, 3: -1, 4: 1})
>>> w = list2vec([-1, -1, 1, 1, 1])
>>> w
Vec({0, 1, 2, 3, 4},{0: -1, 1: -1, 2: 1, 3: 1, 4: 1})
'''


## Task 3 ##
def loss(A, b, w):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
    Output:
        - Value of loss function at w for training data
    '''
    return (A*w-b)*(A*w-b)

## Task 4 ##
def find_grad(A, b, w):
    return 2*(A*w-b)*A
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
    Output:
        - Value of the gradient function at w
'''
 #   list1 = []
#    for i in A.D[0]:
#        list1.append(2*((list2vec([A.f[i,j] for j in A.D[1]]))*w - b[i])*list2vec([A.f[i,j] for j in A.D[1]]))
#    return sum(list1)

    
	
## Task 5 ##
def gradient_descent_step(A, b, w, sigma):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
        - sigma: step size
    Output:
        - The vector w' resulting from 1 iteration of gradient descent
          starting from w and moving sigma.
    '''
    hypothesis_vec = find_grad(A,b,w)
    x = scalar_mul(hypothesis_vec,sigma)
    next_w = w - x
    return next_w

