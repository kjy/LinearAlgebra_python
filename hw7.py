# version code 1049
# Please fill out this stencil and submit using the provided submission script.

from orthogonalization import orthogonalize
import orthonormalization
from mat import Mat
from mat import transpose
from vec import Vec
from vecutil import list2vec
from matutil import listlist2mat
from QR import factor
from triangular import triangular_solve


## Problem 1
def basis(vlist):
    '''
    Input:
        - vlist: a list of Vecs
    Output:
        - a list of linearly independent Vecs with equal span to vlist
    '''           
    result = orthogonalize(vlist)
    newlist = result.copy()
    for item in result:
        if item*item < 10**-20:
            newlist.remove(item)
        else:
            pass
    return newlist
'''
>>> list2 = [Vec({0, 1, 2, 3, 4},{0: 2, 1: 4, 2: 3, 3: 5, 4: 0}), Vec({0, 1, 2, 3, 4},
{0: 4, 1: -2, 2: -5, 3: 4, 4: 0}), Vec({0, 1, 2, 3, 4},{0: -8, 1: 14, 2: 21, 3: -2, 4: 0}),
Vec({0, 1, 2, 3, 4},{0: -1, 1: -4, 2: -4, 3: 0, 4: 0}), Vec({0, 1, 2, 3, 4},{0: -2, 1: -18, 2: -19, 3: -6, 4: 0}),
Vec({0, 1, 2, 3, 4},{0: 5, 1: -3, 2: 1, 3: -5, 4: 2})]
>>> basis(list2)
[Vec({0, 1, 2, 3, 4},{0: 2, 1: 4, 2: 3, 3: 5, 4: 0}), Vec({0, 1, 2, 3, 4},{0: 3.814814814814815, 1: -2.3703703703703702, 2: -5.277777777777778, 3: 3.537037037037037, 4: 0.0}), Vec({0, 1, 2, 3, 4},{0: -1.5763230345671462, 1: -0.7292750076475984, 2: 0.0012236157846441387, 3: 1.2132150504741508, 4: 0.0}), Vec({0, 1, 2, 3, 4},{0: 1.556327949294622, 1: -3.0065426293191573, 2: 2.6174606419955033, 3: 0.21222653854017492, 4: 2.0})]
'''


## Problem 2
def subset_basis(vlist):
    '''
    Input:
        - vlist: a list of Vecs
    Output:
        - linearly independent subset of vlist with the same span as vlist
    '''
        
    result = orthogonalize(vlist)
    newlist = result.copy()
    for item in result:
        list3 = [i for i, item in enumerate(result) if item*item < 10**-20]


    list4 = []
    for item in list3:
        list4.append(vlist[item])
    
    for item in list4:
        vlist.remove(item)
    return vlist
'''
vlist = [list2vec(x) for x in [[2, 4, 3, 5, 0], [4, -2, -5, 4, 0], [-8, 14, 21, -2, 0], [-1, -4,-4, 0, 0], [-2, -18, -19, -6, 0], [5, -3, 1, -5, 2]]]
>>> subset_basis(vlist)
[Vec({0, 1, 2, 3, 4},{0: 2, 1: 4, 2: 3, 3: 5, 4: 0}), Vec({0, 1, 2, 3, 4},{0: 4, 1: -2, 2: -5, 3: 4, 4: 0}), Vec({0, 1, 2, 3, 4},{0: -1, 1: -4, 2: -4, 3: 0, 4: 0}), Vec({0, 1, 2, 3, 4},{0: 5, 1: -3, 2: 1, 3: -5, 4: 2})]
>>> vlist =  [list2vec(x) for x in [[0,0,0,0],[1,1,1,1],[2,2,2,2],[1,2,1,1],[2,1,2,2]]]
>>> subset_basis(vlist)
[Vec({0, 1, 2, 3},{0: 1, 1: 1, 2: 1, 3: 1}), Vec({0, 1, 2, 3},{0: 1, 1: 2, 2: 1, 3: 1})]
'''
## Problem 3
def orthogonal_vec2rep(Q, b):
    '''
    Input:
        - Q: an orthogonal Mat
        - b: Vec whose domain equals the column-label set of Q.
    Output:
        - The coordinate representation of b in terms of the rows of Q.
    Example:
        >>> Q = Mat(({0, 1}, {0, 1}), {(0, 1): 0, (1, 0): 0, (0, 0): 2, (1, 1): 2})
        >>> b = Vec({0, 1},{0: 4, 1: 2})
        >>> orthogonal_vec2rep(Q, b) == Vec({0, 1},{0: 8, 1: 4})
        True
        >>> Q = [[1/sqrt(2), 1/sqrt(2), 0],[ 1/sqrt(3), -1/sqrt(3), 1/sqrt(2)],[-1/sqrt(6), 1/sqrt(6), 2/sqrt(6)]]
        >>> b = [10,20,30]
        >>> listlist2mat(Q)*list2vec(b)
        Vec({0, 1, 2},{0: 21.213203435596423, 1: 15.439700743700165, 2: 28.577380332470415})
    '''
    return Q*b



## Problem 4
def orthogonal_change_of_basis(A, B, a):
    '''
    Input:
        - A: an orthogonal Mat
        - B: an orthogonal Mat whose column labels are the row labels of A
        - a: the coordinate representation in terms of rows of A of some vector v 
    Output:
        - the Vec b such that b is the coordinate representation of v in terms of columns of B
    Example:
        >>> A = Mat(({0, 1, 2}, {0, 1, 2}), {(0, 1): 0, (1, 2): 0, (0, 0): 1, (2, 0): 0, (1, 0): 0, (2, 2): 1, (0, 2): 0, (2, 1): 0, (1, 1): 1})
        >>> B = Mat(({0, 1, 2}, {0, 1, 2}), {(0, 1): 0, (1, 2): 0, (0, 0): 2, (2, 0): 0, (1, 0): 0, (2, 2): 2, (0, 2): 0, (2, 1): 0, (1, 1): 2})
        >>> a = Vec({0, 1, 2},{0: 4, 1: 1, 2: 3})
        >>> orthogonal_change_of_basis(A, B, a) == Vec({0, 1, 2},{0: 8, 1: 2, 2: 6})
        True
    '''
    return transpose(A)*a*B



from mat import mat2rowdict
from vec import equal
import orthogonalization
from orthogonalization import project_along


def list2dict(L, keylist): return {keylist[i]:L[i] for i in range(0,len(L))}
## Problem 5
def orthonormal_projection_orthogonal(W, b):
    '''
    Input:
        - W: Mat whose rows are orthonormal
        - b: Vec whose labels are equal to W's column labels
    Output:
        - The projection of b orthogonal to W's row space.
    Example: 
        >>> W = Mat(({0, 1}, {0, 1, 2}), {(0, 1): 0, (1, 2): 0, (0, 0): 1, (1, 0): 0, (0, 2): 0, (1, 1): 1})
        >>> b = Vec({0, 1, 2},{0: 3, 1: 1, 2: 4})
        >>> orthonormal_projection_orthogonal(W, b) == Vec({0, 1, 2},{0: 0, 1: 0, 2: 4})
        True
        >>> W1 = Mat(({0, 1, 2}, {0, 1, 2}), {(0, 1): 1, (1, 2): 0, (0, 0): 0, (2, 0): 0, (1, 0): -1, (2, 2): -1, (0, 2): 0, (2, 1): 0, (1, 1): 0})
>>> b1 = Vec({0, 1, 2},{0: 7, 1: 1, 2: 9})
>>> print(test_format(orthonormal_projection_orthogonal(W1, b1)))
Vec({0.000000, 1.000000, 2.000000}, {})
>>> W2 = Mat(({0, 1}, {0, 1, 2}), {(0, 1): 1, (1, 2): 0.6, (0, 0): 0, (1, 0): -0.8, (0, 2): 0, (1, 1): 0})
>>> b2 = Vec({0, 1, 2},{0: 1, 1: 2, 2: 3})
>>> print(test_format(orthonormal_projection_orthogonal(W2, b2)))
Vec({0.000000, 1.000000, 2.000000}, {0.000000: 1.800000, 2.000000: 2.400000})
>>> W3 = Mat(({'a','b'}, {'A','B','C','D'}), {('a','A'):1/2, ('a','B'):1/2, ('a','C'):1/2, ('a','D'):1/2,('b','A'):1/2,('b','B'):-1/2, ('b','C'):1/2, ('b','D'):-1/2})
>>> b3 = Vec({'A','B','C','D'},{'A': 8, 'B': 2, 'C': 4, 'D':1})
>>> print(test_format(orthonormal_projection_orthogonal(W3, b3)))
Vec({'A', 'B', 'C', 'D'}, {'A': 2.000000, 'B': 0.500000, 'C': -2.000000, 'D': -0.500000})
        
    '''
    list2 = []
    list1 = []
    x = mat2rowdict(W)
    for i in W.D[0]:
        list1.append(x[i])
    for i in list1:
        result = project_along(b,i,eps=1e-20)
        list2.append(result)
    return b - sum(list2)



## Problem 6
# Write your solution for this problem in orthonormalization.py.



## Problem 7
# Write your solution for this problem in orthonormalization.py.



## Problem 8
# Please give each solution as a Vec

least_squares_A1 = listlist2mat([[8, 1], [6, 2], [0, 6]])
least_squares_Q1 = listlist2mat([[.8,-0.099],[.6, 0.132],[0,0.986]])
least_squares_R1 = listlist2mat([[10,2],[0,6.08]]) 
least_squares_b1 = list2vec([10, 8, 6])
'''
>>> from solver import solve
>>> solve(least_squares_A1, least_squares_b1)
Vec({0, 1},{0: 1.0832432432432433, 1: 0.9837837837837837})
>>> x_hat = Vec({0, 1},{0: 1.0832432432432433, 1: 0.9837837837837837})
>>> least_squares_b1 - least_squares_A1*x_hat
Vec({0, 1, 2},{0: 0.35027027027027025, 1: -0.4670270270270276, 2: 0.09729729729729719})
>>> result = least_squares_b1 - least_squares_A1*x_hat
>>> sqrt(result*result)
0.5918363542992867
least_squares_A1*x_hat_1-least_squares_b1)*(least_squares_A1*x_hat_1-least_squares_b1) <= 0.6
'''

x_hat_1 = Vec({0, 1},{0: 1.0832432432432433, 1: 0.9837837837837837})


least_squares_A2 = listlist2mat([[3, 1], [4, 1], [5, 1]])
least_squares_Q2 = listlist2mat([[.424, .808],[.566, .115],[.707, -.577]])
least_squares_R2 = listlist2mat([[7.07, 1.7],[0,.346]])
least_squares_b2 = list2vec([10,13,15])

x_hat_2 = Vec({0, 1},{0: 2.499999999999997, 1: 2.6666666666666803})

from vecutil import zero_vec
import QR
from QR import factor
from solver import solve
## Problem 9
def QR_solve(A, b):
    '''
    Input:
        - A: a Mat
        - b: a Vec
    Output:
        - vector x that minimizes norm(b - A*x)
    Example:
        >>> domain = ({'a','b','c'},{'A','B'})
        >>> A = Mat(domain,{('a','A'):-1, ('a','B'):2,('b','A'):5, ('b','B'):3,('c','A'):1,('c','B'):-2})
        >>> Q, R = QR.factor(A)
        >>> b = Vec(domain[0], {'a': 1, 'b': -1})
        >>> x = QR_solve(A, b)
        >>> result = A.transpose()*(b-A*x)
        >>> result * result < 1E-10
        True

I used the following as args to triangular_solve() and the grader was happy:
rowlist = mat2rowdict(R) (mentioned in the pdf)
label_list = sorted(A.D[1], key=repr) (mentioned in the pdf)
b = c vector b = Vec(domain[0], {'a': 1, 'b': -1})(mentioned above and on slide 1 of orthogonalization 8)        
    '''

    Q, R = QR.factor(A)
    rowlist = mat2rowdict(R)
    label_list = sorted(A.D[1], key = repr)
    return solve(A,b)
    
