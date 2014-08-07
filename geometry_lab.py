from mat import Mat
import math
from math import sin, cos, pi
import matutil
from matutil import listlist2mat

## Task 1
#labels = {'x','y','u'}
#labels = {'r','g','b'}
def identity(labels = {'x','y','u'}):
    
    '''
    In case you have never seen this notation for a parameter before,
    the way it works is that identity() now defaults to having labels 
    equal to {'x','y','u'}.  So you should write your procedure as if 
    it were defined 'def identity(labels):'.  However, if you want the labels of 
    your identity matrix to be {'x','y','u'}, you can just call 
    identity().  Additionally, if you want {'r','g','b'}, or another set, to be the
    labels of your matrix, you can call identity({'r','g','b'}).  
    '''
               
    return Mat((labels, labels), {(r,c):1 for r in labels for c in labels if r == c})

labels = {'x','y','u'}
#labels = {'r','g','b'}
## Task 2
def translation(x,y):
    Imatrix = identity(labels = {'x','y','u'})
    list_rc = [(r,c) for r in {'x','y','u'} for c in {'x','y','u'} ]
    dict1 = {}
    for (r,c) in list_rc:
        if (r,c) == ('x','u'):
            dict1['x','u']=x
        if (r,c ) == ('y','u'):
            dict1['y','u']=y
        else:
            pass

    T = Mat((labels,labels),dict1)
    result = Imatrix + T
    return Mat((labels, labels), {(r,c):result.f[r,c] for r in labels for c in labels if result.f[r,c] !=0})
    '''
    Input:  An x and y value by which to translate an image.
    Output:  Corresponding 3x3 translation matrix.
    '''
    pass

labels = {'x','y','u'}
## Task 3
def scale(a, b):
    Imatrix = identity(labels = {'x','y','u'})
    list_rc = [(r,c) for r in {'x','y','u'} for c in {'x','y','u'} ]
    dict1 = {}
    for (r,c) in list_rc:
        if (r,c) == ('x','x'):
            dict1['x','x']= a
        if (r,c ) == ('y','y'):
            dict1['y','y']=b
        if (r,c ) == ('u','u'):
            dict1['u','u']=1           
        else:
            pass
    T = Mat((labels,labels),dict1)
    result = Imatrix *T
    return Mat((labels, labels), {(r,c):result.f[r,c] for r in labels for c in labels if result.f[r,c] !=0})
    '''
    Input:  Scaling parameters for the x and y direction.
    Output:  Corresponding 3x3 scaling matrix.
    '''
    pass
labels = {'x','y','u'}
## Task 4
def rotation(angle):
    angle_degree = angle
    angle_matrix = [[1,0,0],[0, cos(angle_degree), sin(angle_degree)],[0, -sin(angle_degree), cos(angle_degree)]]
    Imatrix = identity(labels = {'x','y','u'})
    list_rc = [(r,c) for r in {'x','y','u'} for c in {'x','y','u'} ]
    mat_angle = listlist2mat(angle_matrix)
    result = Mat((labels, labels), {('u','u'):1, ('x','y'): -sin(angle_degree), ('y','x'): sin(angle_degree), ('x','x'):cos(angle_degree), ('y','y'): cos(angle_degree)})
    return result
    '''
    Input:  An angle in radians to rotate an image.
    Output:  Corresponding 3x3 rotation matrix.
    Note that the math module is imported.
    '''
    

## Task 5
def rotate_about(x,y,angle):

    result = translation(-x,-y)*rotation(angle)*translation(x,y)
        
    return Mat((result.D), {(i,j):result.f[i,j] for (i,j) in result.f if result.f[i,j] !=0})
    '''
    Input:  An x and y coordinate to rotate about, and an angle
    in radians to rotate about.
    Output:  Corresponding 3x3 rotation matrix.
    It might be helpful to use procedures you already wrote.
    >>> rotate_about(0, 90, -120)
Mat(({'x', 'y', 'u'}, {'x', 'y', 'u'}), {('y', 'u'): -16.723712652609436, ('y', 'x'): -0.5806111842123143, ('x', 'y'): 0.5806111842123143, ('y', 'y'): 0.8141809705265618, ('x', 'x'): 0.8141809705265618, ('x', 'u'): 52.25500657910828, ('u', 'u'): 1.0})
>>> rotate_about(20,-10,40)
Mat(({'x', 'y', 'u'}, {'x', 'y', 'u'}), {('y', 'u'): 31.571643826109597, ('y', 'x'): 0.7451131604793488, ('x', 'y'): -0.7451131604793488, ('y', 'y'): -0.6669380616522619, ('x', 'x'): -0.6669380616522619, ('x', 'u'): -25.88762962825175, ('u', 'u'): 1.0})
    >>> print (rotate_about(0, 90, -120))

           u      x     y
     --------------------
 u  |      1      0     0
 x  |   52.3  0.814 0.581
 y  |  -16.7 -0.581 0.814
 '''
   
labels = {'x','y','u'}
## Task 6
def reflect_y():
    '''
    Input:  None.
    Output:  3x3 Y-reflection matrix.
    '''
    Imatrix = identity(labels = {'x','y','u'})
    Imatrix['x','x'] = -1
    return Imatrix

## Task 7
def reflect_x():
    '''
    Inpute:  None.
    Output:  3x3 X-reflection matrix.
    '''
    Imatrix = identity(labels = {'x','y','u'})
    Imatrix['y','y'] = -1
    return Imatrix
    
## Task 8    
def scale_color(scale_r,scale_g,scale_b):
    '''
    Input:  3 scaling parameters for the colors of the image.
    Output:  Corresponding 3x3 color scaling matrix.
    '''
    pass

## Task 9
def grayscale():
    '''
    Input: None
    Output: 3x3 greyscale matrix.
    '''
    pass   

## Task 10
def reflect_about(p1,p2):
    '''
    Input: 2 points that define a line to reflect about.
    Output:  Corresponding 3x3 reflect about matrix.
    '''
    pass


