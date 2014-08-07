## Task 1
minutes_in_week = 60*24*7

## Task 2
remainder_without_mod = 2304811-47*(2304811//47)

## Task 3
divisible_by_3 = (673 + 909)%3 == 0

## Task 4
x = -9
y = 1/2
statement_val = 1

## Task 5
#first_five_squares = { ... for _ in {1,2,3,4,5} }
first_five_squares = {x**2 for x in {1,2,3,4,5} }

## Task 6
#first_five_pows_two = { ... for _ in {0,1,2,3,4} }
first_five_pows_two = {2**x for x in {0,1,2,3,4} }

## Task 7: enter in the two new sets
X1 = {4,5,6}
Y1 = {7,8,9}
#{X1*Y1 for X1 in {4,5,6} for Y1 in {7,8,9}}

## Task 8: enter in the two new sets
X2 = {0,20,4}
Y2 = {1,5,25}
#{X2*Y2 for X2 in {0,20,4} for Y2 in {1,5,25}}

## Task 9
base = 10
digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
three_digits_set = {a*10**2 + b*10**1 + c*10**0 for a in range(len(digits)) for b in range(len(digits)) for c in range(len(digits))}

## Task 10
S = {1, 2, 3, 4}
T = {3, 4, 5, 6}
S_intersect_T = {x for x in S if x in T}

## Task 11
L_average = sum([20,10,15,75])/4 # average of: [20, 10, 15, 75]

## Task 12
LofL = [[.25, .75, .1], [-1, 0], [4, 4, 4, 4]]
LofL_sum = LofL_sum = sum([sum(x) for x in LofL])# use form: sum([sum(...) ... ])

## Task 13
cartesian_product = [[x,y] for x in {'A','B','C'} for y in {1,2,3} ] # use form: [ ... {'A','B','C'} ... {1,2,3} ... ]

## Task 14
S = {-4, -2, 1, 2, 5, 0}
zero_sum_list = [(i,j,k) for i in S for j in S for k in S if i+j+k==0]

## Task 15
exclude_zero_list = [(i,j,k) for i in S for j in S for k in S if i+j+k==0 if (i,j,k)!=(0,0,0)]

## Task 16
first_of_tuples_list = [(i,j,k) for i in S for j in S for k in S if i+j+k==0 if (i,j,k)!=(0,0,0)][0]

## Task 17
L1 = [1, 2, 3, 4, 5, 5] # <-- want len(L1) != len(list(set(L1)))
L2 = [1,'a',3, 'z'] # <-- same len(L2) == len(list(set(L2))) but L2 != list(set(L2))

## Task 18
odd_num_list_range = {x for x in range(1,100,2)}

## Task 19
L = ['A','B','C','D','E']
range_and_zip = list(zip(range(len(L)),L))

## Task 20
list_sum_zip = [(x+y) for (x,y) in zip([10,25,40],[1,15,20])]

## Task 21
dlist = [{'James':'Sean', 'director':'Terence'}, {'James':'Roger', 'director':'Lewis'}, {'James':'Pierce', 'director':'Roger'}]
k = 'James'
value_list = [dlist[i][k] for i in range(len(dlist))]

## Task 22
dlist = [{'Bilbo':'Ian','Frodo':'Elijah'},{'Bilbo':'Martin','Thorin':'Richard'}]
k = 'Bilbo'
value_list_modified_1 = [dlist[i][k] if k in dlist[i]  else 'NOT PRESENT' for i in range(len(dlist))] # <-- Use the same expression here
k = 'Frodo'
value_list_modified_2 = [dlist[i][k] if k in dlist[i]  else 'NOT PRESENT' for i in range(len(dlist))] # <-- as you do here

## Task 23
square_dict = {i:i*i for i in range(0,100)}

## Task 24
D = {'red','white','blue'}
identity_dict = {k:k for k in D}

## Task 25
base = 10
digits = set(range(10))
representation_dict = {x:[x // (base**2),(x%100// (base**1)), (x%10 // (base**0))]  for x in three_digits_set}

## Task 26
d = {0:1000.0, 1:1200.50, 2:990}
L = ['Larry', 'Curly', 'Moe']
listdict2dict = dict(zip([key for key in L],[value for value in d.values()]))

## Task 27
def nextInts(L): return [i+1 for i in L]

## Task 28
def cubes(L): return [i**3 for i in L] 

## Task 29
def dict2list(dct, keylist): return [dct[keylist[i]] for i in range(0,len(keylist))]

## Task 30 
def list2dict(L, keylist): return {keylist[i]:L[i] for i in range(0,len(L))}

