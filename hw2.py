# version code 761
# Please fill out this stencil and submit using the provided submission script.

from vec import Vec



## Problem 1
def vec_select(veclist, k): return ([i for i in veclist if i[k] == 0])
"""
    >>> D = {'a','b','c'}
    >>> v1 = Vec(D, {'a': 1})
    >>> v2 = Vec(D, {'a': 0, 'b': 1})
    >>> v3 = Vec(D, {        'b': 2})
    >>> v4 = Vec(D, {'a': 10, 'b': 10})
    >>> vec_select([v1, v2, v3, v4], 'a') == [Vec(D,{'b': 1}), Vec(D,{'b': 2})]
    True
    """
    

def vec_sum(veclist, D):return sum(veclist,(Vec(D, {'a':0,'b':0,'c':0})))
'''
    >>> D = {'a','b','c'}
    >>> v1 = Vec(D, {'a': 1})
    >>> v2 = Vec(D, {'a': 0, 'b': 1})
    >>> v3 = Vec(D, {        'b': 2})
    >>> v4 = Vec(D, {'a': 10, 'b': 10})
    >>> vec_sum([v1, v2, v3, v4], D) == Vec(D, {'b': 13, 'a': 11})
    True
    '''
    

def vec_select_sum(veclist, k, D): return sum([i for i in veclist if i[k] == 0], Vec(D, {'a':0,'b':0,'c':0}))
'''
    >>> D = {'a','b','c'}
    >>> v1 = Vec(D, {'a': 1})
    >>> v2 = Vec(D, {'a': 0, 'b': 1})
    >>> v3 = Vec(D, {        'b': 2})
    >>> v4 = Vec(D, {'a': 10, 'b': 10})
    >>> vec_select_sum([v1, v2, v3, v4], 'a', D) == Vec(D, {'b': 3})
    True
    '''




## Problem 2
def scale_vecs(vecdict): return [1/key*vector for (key, vector) in zip(vecdict.keys(),vecdict.values())]
'''
    >>> v1 = Vec({1,2,3}, {2: 9})
    >>> v2 = Vec({1,2,4}, {1: 1, 2: 2, 4: 8})
    >>> scale_vecs({3: v1, 5: v2}) == [Vec({1,2,3},{2: 3.0}), Vec({1,2,4},{1: 0.2, 2: 0.4, 4: 1.6})]
    True
    '''
import itertools    

from GF2 import one
D = {'a', 'b', 'c'}
L = [Vec(D, {'a': one, 'c': one}), Vec(D, {'b': one})]
#Vec({0, 1},{0: Vec({'c', 'b', 'a'},{'c': one, 'b': 0, 'a': one}), 1: Vec({'c', 'b', 'a'},{'c': 0, 'b': one, 'a': 0})})
x = [0,one]
n=len(L)
scalars = [p for p in itertools.product(x,repeat=2)]
  #scalars = [(one, one), (one, 0), (0, one), (0, 0)]   
## Problem 3
def GF2_span(D, L): return [e[0]*L[0] + e[1]*L[1] for e in scalars ]
 #   list1 = []
#    for e in scalars:
#        result = e[0]*L[0] + e[1]*L[1]
#        list1.append(result)
#    return list1   
'''
    >>> from GF2 import one
    >>> D = {'a', 'b', 'c'}
    >>> L = [Vec(D, {'a': one, 'c': one}), Vec(D, {'b': one})]
    output:
    >>> GF2_span(D, L)==[Vec({'b', 'c', 'a'},{'c': 0, 'a': 0}), Vec({'b', 'c', 'a'},{'c': one, 'a': one}),
    Vec({'b', 'c', 'a'},{'b': one, 'c': 0, 'a': 0}), Vec({'b', 'c', 'a'},{'b': one, 'c': one, 'a': one})]
    >>> len(GF2_span(D, L))
    4
    >>> Vec(D, {}) in GF2_span(D, L)
    True
    >>> Vec(D, {'b': one}) in GF2_span(D, L)
    True
    >>> Vec(D, {'a':one, 'c':one}) in GF2_span(D, L)
    True
    >>> Vec(D, {x:one for x in D}) in GF2_span(D, L)
    True
    '''
 



## Problem 4
# Answer with a boolean, please.

is_it_a_vector_space_1 = True
is_it_a_vector_space_2 = False



## Problem 5
is_it_a_vector_space_3 = True
is_it_a_vector_space_4 = False


## Problem 6

is_it_a_vector_space_5 = True
is_it_a_vector_space_6 = False
