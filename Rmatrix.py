row1 = [one, 0, one, 0, one, 0, 0]
row2 = [one, 0, one, 0, one, one, one]
row3 = [one, 0, one, 0, 0, 0, one]
row4 = [one,one, one, 0,one,one,0]

R = [[one, 0, one, 0, one, 0, 0], [one, 0, one, 0, one, one, one], [one, 0, one, 0, 0, 0, one],[one,one, one, 0,one,one,0]]
G = [[1,0,1,1],[1,1,0,1],[0,0,0,1],[1,1,1,0],[0,0,1,0],[0,1,0,0],[1,0,0,0]]

>>> listlist2mat(R)
Mat(({0, 1, 2, 3}, {0, 1, 2, 3, 4, 5, 6}), {(1, 2): one, (3, 2): one, (0, 0): one, (3, 0): one, (0, 4): one,
                                            (1, 4): one, (2, 6): one, (0, 5): 0, (2, 1): 0, (2, 5): 0, (2, 0): one, (1, 0): one, (3, 5): one, (0, 1): 0, (0, 2): one, (3, 3): 0,
                                            (0, 6): 0, (3, 4): one, (3, 1): one, (1, 6): one, (1, 1): 0, (1, 5): one, (3, 6): 0, (2, 2): one, (1, 3): 0, (2, 3): 0, (0, 3): 0, (2, 4): 0})
>>> x = listlist2mat(rmatrix)
>>> transpose(x)
Mat(({0, 1, 2, 3, 4, 5, 6}, {0, 1, 2, 3}), {(0, 1): one, (3, 2): one, (0, 0): one, (4, 3): 0, (3, 0): 0, (6, 0): one, (2, 1): one, (6, 2): one, (2, 3): one, (4, 2): one, (5, 1): one, (1, 0): one, (0, 3): one, (5, 3): 0, (1, 2): one, (3, 3): one, (5, 2): 0, (6, 1): one, (3, 1): 0, (0, 2): one, (6, 3): one, (2, 0): 0, (5, 0): one, (2, 2): 0, (1, 3): one, (4, 0): one, (4, 1): one, (1, 1): 0})
>>> Rfinal = transpose(x)
>>> Rfinal
Mat(({0, 1, 2, 3, 4, 5, 6}, {0, 1, 2, 3}), {(0, 1): one, (3, 2): one, (0, 0): one, (4, 3): 0, (3, 0): 0, (6, 0): one, (2, 1): one, (6, 2): one, (2, 3): one,
                                            (4, 2): one, (5, 1): one, (1, 0): one, (0, 3): one, (5, 3): 0, (1, 2): one, (3, 3): one, (5, 2): 0, (6, 1): one, (3, 1): 0, (0, 2): one, (6, 3):
                                            one, (2, 0): 0, (5, 0): one, (2, 2): 0, (1, 3): one, (4, 0): one, (4, 1): one, (1, 1): 0})


>>> col1
[one, one, 0, one, 0, 0, one]
>>> col2
[0, one, 0, one, 0, one, 0]
>>> col3
[one, 0, 0, one, one, 0, 0]
>>> col4
[one, one, one, 0, 0, 0, 0]
>>> Gmat = [[one, one, 0, one, 0, 0, one],[0, one, 0, one, 0, one, 0],[one, 0, 0, one, one, 0, 0],[one, one, one, 0, 0, 0, 0]]
>>> Gsub = listlist2mat(Gmat)
>>> Gsub
Mat(({0, 1, 2, 3}, {0, 1, 2, 3, 4, 5, 6}), {(1, 2): 0, (3, 2): one, (0, 0): one, (3, 0): one, (0, 4): 0, (1, 4): 0, (2, 6): 0, (0, 5): 0, (2, 1): 0, (2, 5): 0, (2, 0): one, (1, 0): 0, (3, 5): 0, (0, 1): one, (0, 2): 0, (3, 3): 0, (0, 6): one, (3, 4): 0, (3, 1): one, (1, 6): 0, (1, 1): one, (1, 5): one, (3, 6): 0, (2, 2): 0, (1, 3): one, (2, 3): one, (0, 3): one, (2, 4): one})
>>> >>> G
Mat(({0, 1, 2, 3, 4, 5, 6}, {0, 1, 2, 3}), {(0, 1): 0, (3, 2): one, (0, 0): one, (4, 3): 0, (3, 0): one, (6, 0): one, (2, 1): 0, (6, 2): 0, (2, 3): one, (4, 2): one, (5, 1): one, (1, 0): one, (0, 3): one, (5, 3): 0, (1, 2): 0, (3, 3): 0, (5, 2): 0, (6, 1): 0, (3, 1): one, (0, 2): one, (6, 3): 0, (2, 0): 0, (5, 0): 0, (2, 2): 0, (1, 3): one, (4, 0): 0, (4, 1): 0, (1, 1): one})

>>> row1
[one, one, 0, 0, one, one, one]
>>> col1
[one, one, 0, one, 0, 0, one]
>>> [x*y for (x,y) in zip(row1,col1)]
[one, one, 0, 0, 0, 0, one]
>>> sum([x*y for (x,y) in zip(row1,col1)])
one
>>> sum([x*y for (x,y) in zip(row1,col2)])
0
>>> sum([x*y for (x,y) in zip(row1,col3)])
0
>>> sum([x*y for (x,y) in zip(row1,col4)])
0
>>> row2
[one, 0, one, 0, one, one, one]
>>> sum([x*y for (x,y) in zip(row2,col1)])
0
>>> sum([x*y for (x,y) in zip(row2,col2)])
one
>>> sum([x*y for (x,y) in zip(row2,col3)])
0
>>> sum([x*y for (x,y) in zip(row2,col4)])
0
>>> row3
[one, one, 0, one, one, 0, one]
>>> sum([x*y for (x,y) in zip(row3,col1)])
0
>>> sum([x*y for (x,y) in zip(row3,col2)])
0
>>> sum([x*y for (x,y) in zip(row3,col3)])
one
>>> sum([x*y for (x,y) in zip(row3,col4)])
0
>>> row4
[one, one, one, one, 0, 0, one]
>>> sum([x*y for (x,y) in zip(row4,col1)])
0
>>> sum([x*y for (x,y) in zip(row4,col2)])
0
>>> sum([x*y for (x,y) in zip(row4,col3)])
0
>>> sum([x*y for (x,y) in zip(row4,col4)])
one
>>> R*G



>>> from GF2 import one
>>> G = Mat(({0, 1, 2, 3, 4, 5, 6}, {0, 1, 2, 3}), {(1, 2): 0, (3, 2): one, (0, 0): one, (4, 3): 0, (3, 0): one,
        (6, 0): one, (2, 1): 0, (1, 3): one, (2, 3): one, (5, 1): one, (4, 2): one, (1, 0): one, (0, 3): one,
        (4, 0): 0, (0, 1): 0, (3, 3): 0, (5, 2): 0, (6, 1): 0, (3, 1): one, (0, 2): one, (6, 3): 0, (2, 0): 0,
        (6, 2): 0, (5, 0): 0, (2, 2): 0, (5, 3): 0, (4, 1): 0, (1, 1): one})
>>> R = Mat(({0, 1, 2, 3}, {0, 1, 2, 3, 4, 5, 6}), {(1, 2): 0, (3, 2): one, (0, 0): 0, (3, 0): 0, (0, 4): 0, (1, 4): 0, (2, 6): 0, (0, 5): 0, (2, 1): 0,
    (2, 5): 0, (2, 0): 0, (1, 0): 0, (3, 5): 0, (0, 1): 0, (0, 2): 0, (3, 3): 0, (0, 6): one, (3, 4): 0, (3, 1): 0, (1, 6): 0, (1, 1): 0, (1, 5): one,
    (3, 6): 0, (2, 2): 0, (1, 3): 0, (2, 3): 0, (0, 3): 0, (2, 4): one})
>>> R*G
Mat(({0, 1, 2, 3}, {0, 1, 2, 3}), {(0, 1): 0, (1, 2): 0, (3, 2): 0, (0, 0): one, (3, 3): one, (3, 0): 0, (3, 1): 0, (1, 1): one, (2, 1): 0, (0, 2): 0, (2, 0): 0, (1, 3): 0, (2, 3): 0, (2, 2): one, (1, 0): 0, (0, 3): 0})




>>> print (R)

       0 1   2 3   4   5   6
     -----------------------
 0  |  0 0   0 0   0   0 one
 1  |  0 0   0 0   0 one   0
 2  |  0 0   0 0 one   0   0
 3  |  0 0 one 0   0   0   0

>>> print (G)

         0   1   2   3
     -----------------
 0  |  one   0 one one
 1  |  one one   0 one
 2  |    0   0   0 one
 3  |  one one one   0
 4  |    0   0 one   0
 5  |    0 one   0   0
 6  |  one   0   0   0

>>> print (R*G)

         0   1   2   3
     -----------------
 0  |  one   0   0   0
 1  |    0 one   0   0
 2  |    0   0 one   0
 3  |    0   0   0 one
