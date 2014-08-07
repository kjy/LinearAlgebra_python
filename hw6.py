# version code 988
# Please fill out this stencil and submit using the provided submission script.

from matutil import *
from GF2 import one



## Problem 1
# Write each matrix as a list of row lists

echelon_form_1 = [[1, 2, 0, 2, 0],
                  [0, 1, 0, 3, 4],
                  [0, 0, 2, 3, 4],
                  [0, 0, 0, 2, 0],
                  [0, 0, 0, 0, 4]]

echelon_form_2 = [[0, 4, 3, 4, 4],
                  [0, 0, 4, 2, 0],
                  [0, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0]]

echelon_form_3 = [[1, 0, 0, 1],
                  [0, 0, 0, 1],
                  [0, 0, 0, 0]]

echelon_form_4 = [[1, 0, 0, 0],
                  [0, 1, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0]]

def find_first_nonzero(A):
    list1 = []
    for row in range(len(A)):
        list1.append([x for x in A[row] if x != 0])
    list2 = []
    for i in range(len(list1)):
        list2.append(list1[i][0])

    list3 = [A[row].index(i) for row,i in zip(range(len(A)),list2) ]

	
    #[(i,j) for (i,j) in zip(range(len(list1)),list3) ]

    if list3 == sorted(list3):
        return True
    else:
        return False

## Problem 2
def is_echelon(A):
    
    
    if len(A) ==1 and A[0][0] !=0:
        return True
    else:
        pass
    if len(A) ==1 and A[0][0] ==0:
        return True
    else:
        pass
    
    if A[-1]==A[-2]:
        if sum(A[-1])== 0:
            return True
        else:
            return False
    else:
        pass
    if len (A) > 1 and A[0][0] !=0:
        return find_first_nonzero(A)
    else:
        pass

    list4 = []
    for outer in range(len(A)):
        for inner in range(len(A[outer])):
            A[outer][inner]
            list4.append(A[outer][inner])
            
    if len(list4) == list4.count(0):
        return True
    else:
        return False
    
    
 
    '''
    
    total = 0
    for i in range(len(A[0])):
        total = total + A[0][i]
    sum = 0
    for i in range(len(A[1])):
        sum = sum + A[1][i]
    if total == 0 and sum !=0:
        return False
    else:
        pass

''' 
    '''
    Input:
        - A: a list of row lists
    Output:
        - True if A is in echelon form
        - False otherwise
    Examples:
        >>> is_echelon([[1,1,1],[0,1,1],[0,0,1]])
        True
        >>> is_echelon([[0,1,1],[0,1,0],[0,0,1]])
        False
        >>> L1 = [[2,1,4],[0,-4,0],[0,0,1]]
        >>> is_echelon(L1)
        True
        >>> L2 = [[2,1,0],[-4,0,0],[0,0,1]]
        >>> is_echelon(L2)
        False
        >>> L3 = [[2,1,0],[0,3,0],[1,0,1]]
        >>> is_echelon(L3)
        False
        >>> L4 = [[1,1,1,1,1],[0,2,0,1,3],[0,0,0,5,3]]
        >>> is_echelon(L4)
        True
        >>> M1 = [[0,0,0],[0,0,0],[0,0,0]]
        True
        >>> M2 = [[1,0,0],[0,1,0],[0,1,0]]
        False
        >>> M3 = [[0]*4,[1]*4]
        False
        >>> M4 = [[1,0,0,0,0,0,0,0],
                  [0,1,1,1,1,1,1,1],
                  [0,0,1,1,1,0,1,0],
                  [0,0,0,0,0,1,1,0]]
        True
        >>> M5 = [[1]]
        True
        >>> M6 = [[0]]
        True
    '''



## Problem 3
# Give each answer as a list

echelon_form_vec_a = [1,0,3,0]
echelon_form_vec_b = [-3, 0, -2, 3]
echelon_form_vec_c = [-5,0,2,0,2]



## Problem 4
# If a solution exists, give it as a list vector.
# If no solution exists, provide "None".

solving_with_echelon_form_a = None
solving_with_echelon_form_b = [21, 0, 2, 0, 0]


## Problem 5
def echelon_solve(rowlist, label_list, b):
    '''
    Input:
        - rowlist: a list of Vecs
        - label_list: a list of labels establishing an order on the domain of
                      Vecs in rowlist
        - b: a vector (represented as a list)
    Output:
        - Vec x such that rowlist * x is b
    >>> D = {'A','B','C','D','E'}
    >>> U_rows = [Vec(D, {'A':one, 'E':one}), Vec(D, {'B':one, 'E':one}), Vec(D,{'C':one})] 
    >>> b_list = [one,0,one]>>> cols = ['A', 'B', 'C', 'D', 'E']
    >>> echelon_solve(U_rows, cols, b_list)
    Vec({'B', 'C', 'A', 'D', 'E'},{'B': 0, 'C': one, 'A': one})
    '''
def triangular_solve(rowlist, label_list, b):
    '''
    Solves an upper-triangular linear system.
    rowlist is a nonempty list of Vecs.  Let n = len(rowlist).
    b is an n-element list or a Vec over domain {0,1, ..., n-1}.
    The linear equations are:
       rowlist[0] * x = b[0]
                     ...
       rowlist[n-1] * x = b[n-1]
    label_list is a list consisting of the elements of D,
    where D is the domain of each of the vectors in rowlist.
    The system is triangular with respect to the ordering given
    by label_list.  That means rowlist[n-1][d] is zero for 
    every element d of D except for the last element of label_list,
    rowlist[n-2][d] is zero for every element d of D except for 
    the last two elements of label_list, and so on.
    
    This procedure assumes that rowlist[j][label_list[j]] != 0
    for j = 0,1, ..., n-1.
    
    The procedure returns the Vec x that is the unique solution
    to the linear system.
    '''
    D = rowlist[0].D
    x = zero_vec(D)
    for j in reversed(range(len(D))):
        c = label_list[j]
        row = rowlist[j]
        x[c] = (b[j] - x*row)/row[c]
    return x



## Problem 6
rowlist = [ ... ]    # Provide as a list of Vec instances
label_list = [ ... ] # Provide as a list
b = [ ... ]          # Provide as a list



## Problem 7
null_space_rows_a = {...} # Put the row numbers of M from the PDF



## Problem 8
null_space_rows_b = {...}



## Problem 9
# Write each vector as a list
closest_vector_1 = [1.6, 3.2]
closest_vector_2 = [0, 1, 0]
closest_vector_3 = [3, 2, 1, -4]



## Problem 10
# Write each vector as a list

project_onto_1 = [2,0]
projection_orthogonal_1 = [0,1] 

project_onto_2 = [-0.16666666666666666, -0.3333333333333333, 0.16666666666666666]
projection_orthogonal_2 =   [7/6, 4/3, 3.8333333333333335]

project_onto_3 = [1, 1, 4]
projection_orthogonal_3 = [0,0,0] 



## Problem 11
norm1 = 3
norm2 = 4
norm3 = 1
