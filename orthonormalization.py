from vec import Vec
from orthogonalization import orthogonalize
from orthogonalization import aug_orthogonalize
from vecutil import list2vec
from math import sqrt
from mat import transpose
from matutil import coldict2mat, mat2coldict

def orthonormalize(L):
    '''
    Input: a list L of linearly independent Vecs
    Output: A list T of orthonormal Vecs such that for all i in [1, len(L)],
            Span L[:i] == Span T[:i]

    list1 = [[4, 3, 1, 2], [8, 9, -5, -5], [10, 1, -1, 5]]
    for i in list1:
        list2vec(i)
>>> L = [Vec({0, 1, 2, 3},{0: 4, 1: 3, 2: 1, 3: 2}),Vec({0, 1, 2, 3},{0: 8, 1: 9, 2: -5, 3: -5}),  Vec({0, 1, 2, 3},{0: 10, 1: 1, 2: -1, 3: 5}) ]

>>> from vecutil import *
>>> v1 = list2vec([1,2,3,4])
>>> v2 = list2vec([2,3,4,5])
>>> print(test_format(orthonormalization.orthonormalize([v1, v2])))
[Vec({0.000000, 1.000000, 2.000000, 3.000000}, {0.000000: 0.182574, 1.000000: 0.365148, 2.000000: 0.547723, 3.000000: 0.730297}), Vec({0.000000, 1.000000, 2.000000, 3.000000}, {0.000000: 0.816497, 1.000000: 0.408248, 3.000000: -0.408248})]
>>> v1 = list2vec([1,2,1])
>>> v2 = list2vec([2,2,2])
>>> print(test_format(orthonormalization.orthonormalize([v1, v2])))
[Vec({0.000000, 1.000000, 2.000000}, {0.000000: 0.408248, 1.000000: 0.816497, 2.000000: 0.408248}), Vec({0.000000, 1.000000, 2.000000}, {0.000000: 0.577350, 1.000000: -0.577350, 2.000000: 0.577350})]
>>> v1 = list2vec([.2, .4, .1, .9])
>>> v2 = list2vec([12, 144, 91, 0])
>>> v3 = list2vec([1, 1, 1, 1])
>>> v4 = list2vec([0, 12, 0, 0])
>>> print(test_format(orthonormalization.orthonormalize([v1, v2, v3, v4])))
[Vec({0.000000, 1.000000, 2.000000, 3.000000}, {0.000000: 0.198030, 1.000000: 0.396059, 2.000000: 0.099015, 3.000000: 0.891133}), Vec({0.000000, 1.000000, 2.000000, 3.000000}, {0.000000: -0.009900, 1.000000: 0.747167, 2.000000: 0.538319, 3.000000: -0.389687}), Vec({0.000000, 1.000000, 2.000000, 3.000000}, {0.000000: 0.827563, 1.000000: -0.344536, 2.000000: 0.436070, 3.000000: -0.079228}), Vec({0.000000, 1.000000, 2.000000, 3.000000}, {0.000000: 0.525190, 1.000000: 0.407644, 2.000000: -0.714319, 3.000000: -0.218515})]
    '''
    Ortho_L = orthogonalize(L)

    list1 = []
    for i in Ortho_L:
        list1.append(sqrt(i*i))
    return [v/vnorm for v, vnorm in zip(Ortho_L, list1)]
    


def aug_orthonormalize(L):
    '''
    Input:
        - L: a list of Vecs
    Output:
        - A pair Qlist, Rlist such that:
            * coldict2mat(L) == coldict2mat(Qlist) * coldict2mat(Rlist)
            * Qlist = orthonormalize(L)

    >>> L = [list2vec(v) for v in [[4,3,1,2], [8,9,-5,-5],[10,1,-1,5]] ]
>>> L
[Vec({0, 1, 2, 3},{0: 4, 1: 3, 2: 1, 3: 2}), Vec({0, 1, 2, 3},{0: 8, 1: 9, 2: -5, 3: -5}), Vec({0, 1, 2, 3},{0: 10, 1: 1, 2: -1, 3: 5})]
    '''
    Qlist = orthonormalize(L)
 
    Rsub = transpose(coldict2mat(Qlist)) * coldict2mat(L)
    x = mat2coldict(Rsub)
    Rlist  = []
    for i in x:
        Rlist.append(x[i])
    return  Qlist,  Rlist
    
    
