# Please fill out this stencil and submit using the provided submission script.

from GF2 import one



## Problem 1
p1_u = [ 0, 4]
p1_v = [-1, 3]
p1_v_plus_u = [v + u for v,u in zip(p1_v,p1_u)]
p1_v_minus_u = [v - u for v,u in zip(p1_v,p1_u)]
p1_three_v_minus_two_u = [3*v -2*u for v,u in zip(p1_v,p1_u)]



## Problem 2
p2_u = [-1,  1, 1]
p2_v = [ 2, -1, 5]
p2_v_plus_u = [v + u for v,u in zip(p2_v,p2_u)]
p2_v_minus_u = [v - u for v,u in zip(p2_v,p2_u)]
p2_two_v_minus_u = [2*v - u for v,u in zip(p2_v,p2_u)]
p2_v_plus_two_u = [v + 2*u for v,u in zip(p2_v,p2_u)]



## Problem 3
# Write your answer using GF2's one instead of the number 1
v = [0, one, one]
u = [one, one, one]
p3_vector_sum_1 = [x + y for x,y in zip(v,u)]
p3_vector_sum_2 = [x + y + y for x,y in zip(v,u)]



## Problem 4
# Please express your solution as a set of the letters corresponding to the solutions.
# For example, {'a','b','c'} is the subset consisting of:
#   a (1100000), b (0110000), and c (0011000).
# Leave an empty set if it cannot be expressed in terms of the other vectors.

u_0010010 = {'c','d','e'}
u_0100010 = {'b','c','d','e'}



## Problem 5
# Use the same format as the previous problem

v_0010010 = {'c','d'}
v_0100010 = set()



## Problem 6  sum([i*j for (i,j) in zip(u,v)]) is dot product
uv_a = 5
uv_b = 6
uv_c = 16
uv_d = -1.0000000000000002



## Problem 7
# use 'one' instead of '1'
x_gf2 = [one, 0, 0, 0]



## Problem 8
v1 = [2,3,-4,1]
v2 = [1,-5,2,0]
v3 = [4,1,-1,-1]

