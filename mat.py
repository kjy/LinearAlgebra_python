import vec
from vec import Vec
from vec import dot
import vecutil
from vecutil import list2vec

def getitem(M, k):
    "Returns the value of entry k in M.  The value of k should be a pair."
    assert k[0] in M.D[0] and k[1] in M.D[1]
    if k in M.f:
        return M.f[k]
    else:
        return 0

def setitem(M, k, val):
    "Sets the element of v with label k to be val.  The value of k should be a pair"
    assert k[0] in M.D[0] and k[1] in M.D[1]
    M.f[k]=val

def add(A, B):
    "Returns the sum of A and B"
    assert A.D == B.D
        
    list_rc_A = [(r,c) for r in A.D[0] for c in A.D[1] ]       
    for d1,d2 in list_rc_A:
        if not ((d1,d2) in A.f):
            A.f[d1,d2]=0
        else:
            pass
    list_rc_B = [(r,c) for r in B.D[0] for c in B.D[1] ]       
    for d1,d2 in list_rc_B:
        if not ((d1,d2) in B.f):
            B.f[d1,d2]=0
        else:
            pass
        
    dict1 = {}
    for k in A.f:
        dict1[k]=B.f[k] + A.f[k]
    return Mat(B.D,dict1)
          

def scalar_mul(M, alpha):
    "Returns the product of scalar alpha with M" 
    dict2 = {}
    for key in M.f:
        dict2[key]= alpha*M.f[key]
    return Mat(M.D, dict2)

def equal(A, B):
    "Returns true iff A is equal to B"
    assert A.D == B.D
    
    list_rc_A = [(r,c) for r in A.D[0] for c in A.D[1] ]
    for (d1,d2) in list_rc_A:
        if not ((d1,d2) in A.f):
            A.f[d1,d2]=0
        else:
            pass
    list_rc_B = [(r,c) for r in B.D[0] for c in B.D[1] ]       
    for d1,d2 in list_rc_B:
        if not ((d1,d2) in B.f):
            B.f[d1,d2]=0
        else:
            pass

    if A.f == B.f:
        return True
    else:
        return False



def transpose(M):
    "Returns the transpose of M"
    list_values = []
    for value in M.f.values():
        list_values.append(value)
        
    list_keys = []
    for key in M.f.keys():
        list_keys.append(key)
        
    list2_keys = []
    for i in list_keys:
        x = list(reversed(i))
        list2_keys.append(x)
        
    list3_keys = []
    for i in list2_keys:
        list3_keys.append(tuple(i))
        
    new_col = M.D[0]
    new_row = M.D[1]

    Transpose_matrix = Mat((new_row,new_col), {k:v for (k,v) in zip(list3_keys,list_values)})

    return Transpose_matrix

def extract_row(M, row):
    """
    Takes a matrix, M and a row key from that matrix and returns a vector
    representing that row.
    """
    assert row in M.D[0]
    v = Vec(M.D[1], {})
    for column in M.D[1]:
        key = (row, column)
        if key in M.f:
            v.f[column] = M.f[key]
    return v

def extract_col(M, column):
    '''
    Takes a matrix, M and a col key from that matrix and returns a vector
    representing that col.
    '''
    
    list_rc_M = [(r,c) for r in M.D[0] for c in M.D[1] ]
    for (d1,d2) in list_rc_M:
        if not ((d1,d2) in M.f):
            M.f[d1,d2]=0
        else:
            pass
    #assert column in M.D[1]
    v = Vec(M.D[0], {})
    for row in M.D[0]:
        key = (row, column)
        if key in M.f:
            v.f[row] = M.f[key]
    return v

def mat2rowdict(A):
  """Given a matrix, return a dictionary mapping row labels of A to rows of A
	 e.g.:
	 
     >>> M = Mat(({0, 1, 2}, {0, 1}), {(0, 1): 1, (2, 0): 8, (1, 0): 4, (0, 0): 3, (2, 1): -2})
	 >>> mat2rowdict(M)
	 {0: Vec({0, 1},{0: 3, 1: 1}), 1: Vec({0, 1},{0: 4, 1: 0}), 2: Vec({0, 1},{0: 8, 1: -2})}
	 >>> mat2rowdict(Mat(({0,1},{0,1}),{}))
	 {0: Vec({0, 1},{0: 0, 1: 0}), 1: Vec({0, 1},{0: 0, 1: 0})}
	 """
  return {row:Vec(A.D[1], {col:A[row,col] for col in A.D[1]}) for row in A.D[0]}
def mat2coldict(A):
  """Given a matrix, return a dictionary mapping column labels of A to columns of A
	 e.g.:
	 >>> M = Mat(({0, 1, 2}, {0, 1}), {(0, 1): 1, (2, 0): 8, (1, 0): 4, (0, 0): 3, (2, 1): -2})
	 >>> mat2coldict(M)
	 {0: Vec({0, 1, 2},{0: 3, 1: 4, 2: 8}), 1: Vec({0, 1, 2},{0: 1, 1: 0, 2: -2})}
	 >>> mat2coldict(Mat(({0,1},{0,1}),{}))
	 {0: Vec({0, 1},{0: 0, 1: 0}), 1: Vec({0, 1},{0: 0, 1: 0})}
"""	 
  return {col:Vec(A.D[0], {row:A[row,col] for row in A.D[0]}) for col in A.D[1]}


def vector_matrix_mul(v, M):
    "Returns the product of vector v and matrix M"
    assert M.D[0] == v.D
    MM = mat2coldict(M)
    col = M.D[1]
    row = v.D
    list_rc = [(r,c) for r in row for c in col]
    dict1 = {}
    for i in MM:
        dict1[i] = dot(MM[i],v)
    return Vec(M.D[1], dict1)
'''
>>> v1 = Vec({1, 2, 3}, {1: 1, 2: 8})
>>> M1 = Mat(({1, 2, 3}, {1, 2, 3}), {(1, 2): 2, (2, 1):-1, (3, 1): 1, (3, 3): 7})
>>> v1*M1 == Vec({1, 2, 3},{1: -8, 2: 2, 3: 0})
True
>>> v1 == Vec({1, 2, 3}, {1: 1, 2: 8})
True
>>> M1 == Mat(({1, 2, 3}, {1, 2, 3}), {(1, 2): 2, (2, 1):-1, (3, 1): 1, (3, 3): 7})
True
>>> v2 = Vec({'a','b'}, {})
>>> M2 = Mat(({'a','b'}, {0, 2, 4, 6, 7}), {})
>>> v2*M2 == Vec({0, 2, 4, 6, 7},{})
True
'''

def matrix_vector_mul(M, v):
    "Returns the product of matrix M and vector v"
    assert M.D[1] == v.D
    MM = mat2rowdict(M)
    row = M.D[0]
    col = v.D
    list_rc = [(r,c) for r in row for c in col]
    dict1 = {}
    for i in MM:
        dict1[i] = dot(MM[i],v)
    return Vec(M.D[0], dict1)
'''
>>> N1 = Mat(({1, 3, 5, 7}, {'a', 'b'}), {(1, 'a'): -1, (1, 'b'): 2, (3, 'a'): 1, (3, 'b'):4, (7, 'a'): 3, (5, 'b'):-1})
>>> u1 = Vec({'a', 'b'}, {'a': 1, 'b': 2})
>>> N1*u1 == Vec({1, 3, 5, 7},{1: 3, 3: 9, 5: -2, 7: 3})
True
>>> N1 == Mat(({1, 3, 5, 7}, {'a', 'b'}), {(1, 'a'): -1, (1, 'b'): 2, (3, 'a'): 1, (3, 'b'):4, (7, 'a'): 3, (5, 'b'):-1})
True
>>> u1 == Vec({'a', 'b'}, {'a': 1, 'b': 2})
True
>>> N2 = Mat(({('a', 'b'), ('c', 'd')}, {1, 2, 3, 5, 8}), {})
>>> u2 = Vec({1, 2, 3, 5, 8}, {})
>>> N2*u2 == Vec({('a', 'b'), ('c', 'd')},{})
True
'''

def matrix_matrix_mul(A, B):
    "Returns the product of A and B"
    assert A.D[1] == B.D[0]
    AA = mat2rowdict(A)
    BB = mat2coldict(B)
    row = A.D[0]
    col = B.D[1]
    list_rc = [(r,c) for r in row for c in col]
    dict1 = {}
    for i,j in list_rc:
        dict1[(i,j)]=dot(AA[i],BB[j])
    result = Mat((A.D[0], B.D[1]), dict1)
    return Mat((A.D[0],B.D[1]), {(r,c):result.f[r,c] for r in A.D[0] for c in B.D[1] if result.f[r,c] !=0})
'''    	
>>> A = Mat(({0,1,2}, {0,1,2}), {(1,1):4, (0,0):0, (1,2):1, (1,0):5, (0,1):3, (0,2):2})
>>> B = Mat(({0,1,2}, {0,1,2}), {(1,0):5, (2,1):3, (1,1):2, (2,0):0, (0,0):1, (0,1):4})
>>> A*B == Mat(({0,1,2}, {0,1,2}), {(0,0):15, (0,1):12, (1,0):25, (1,1):31})
True
>>> C = Mat(({0,1,2}, {'a','b'}), {(0,'a'):4, (0,'b'):-3, (1,'a'):1, (2,'a'):1, (2,'b'):-2}) 
>>> D = Mat(({'a','b'}, {'x','y'}), {('a','x'):3, ('a','y'):-2, ('b','x'):4, ('b','y'):-1})
>>> C*D == Mat(({0,1,2}, {'x','y'}), {(0,'y'):-5, (1,'x'):3, (1,'y'):-2, (2,'x'):-5})
True
>>> M = Mat(({0, 1}, {'a', 'c', 'b'}), {})
>>> N = Mat(({'a', 'c', 'b'}, {(1, 1), (2, 2)}), {})
>>> M*N == Mat(({0,1}, {(1,1), (2,2)}), {})
True    
'''
    
################################################################################

class Mat:
    def __init__(self, labels, function):
        self.D = labels
        self.f = function

    __getitem__ = getitem
    __setitem__ = setitem
    transpose = transpose

    def __neg__(self):
        return (-1)*self

    def __mul__(self,other):
        if Mat == type(other):
            return matrix_matrix_mul(self,other)
        elif Vec == type(other):
            return matrix_vector_mul(self,other)
        else:
            return scalar_mul(self,other)
            #this will only be used if other is scalar (or not-supported). mat and vec both have __mul__ implemented

    def __rmul__(self, other):
        if Vec == type(other):
            return vector_matrix_mul(other, self)
        else:  # Assume scalar
            return scalar_mul(self, other)

    __add__ = add

    def __sub__(a,b):
        return a+(-b)

    __eq__ = equal

    def copy(self):
        return Mat(self.D, self.f.copy())

    def __str__(M, rows=None, cols=None):
        "string representation for print()"
        if rows == None:
            try:
                rows = sorted(M.D[0])
            except TypeError:
                rows = sorted(M.D[0], key=hash)
        if cols == None:
            try:
                cols = sorted(M.D[1])
            except TypeError:
                cols = sorted(M.D[1], key=hash)
        separator = ' | '
        numdec = 3
        pre = 1+max([len(str(r)) for r in rows])
        colw = {col:(1+max([len(str(col))] + [len('{0:.{1}G}'.format(M[row,col],numdec)) if isinstance(M[row,col], int) or isinstance(M[row,col], float) else len(str(M[row,col])) for row in rows])) for col in cols}
        s1 = ' '*(1+ pre + len(separator))
        s2 = ''.join(['{0:>{1}}'.format(c,colw[c]) for c in cols])
        s3 = ' '*(pre+len(separator)) + '-'*(sum(list(colw.values())) + 1)
        s4 = ''.join(['{0:>{1}} {2}'.format(r, pre,separator)+''.join(['{0:>{1}.{2}G}'.format(M[r,c],colw[c],numdec) if isinstance(M[r,c], int) or isinstance(M[r,c], float) else '{0:>{1}}'.format(M[r,c], colw[c]) for c in cols])+'\n' for r in rows])
        return '\n' + s1 + s2 + '\n' + s3 + '\n' + s4

    def pp(self, rows, cols):
        print(self.__str__(rows, cols))

    def __repr__(self):
        "evaluatable representation"
        return "Mat(" + str(self.D) +", " + str(self.f) + ")"
