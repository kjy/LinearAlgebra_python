voting_data = list(open("/Users/karenyang/Desktop/matrix/voting_record_dump109.txt"))

## Task 1
def create_voting_dict():
    """
    Input: None (use voting_data above)
    Output: A dictionary that maps the last name of a senator
            to a list of numbers representing the senator's voting
            record.
    Example: 
        >>> create_voting_dict()['Clinton']
        [-1, 1, 1, 1, 0, 0, -1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1]

    This procedure should return a dictionary that maps the last name
    of a senator to a list of numbers representing that senator's
    voting record, using the list of strings from the dump file (strlist). You
    will need to use the built-in procedure int() to convert a string
    representation of an integer (e.g. '1') to the actual integer
    (e.g. 1).

    You can use the split() procedure to split each line of the
    strlist into a list; the first element of the list will be the senator's
    name, the second will be his/her party affiliation (R or D), the
    third will be his/her home state, and the remaining elements of
    the list will be that senator's voting record on a collection of bills.
    A "1" represents a 'yea' vote, a "-1" a 'nay', and a "0" an abstention.

    The lists for each senator should preserve the order listed in voting data. 
    """
    mylist = list(voting_data)
    listlines=[]
    for line in mylist:
        listlines.append(line.split())


        
    names = []
    for i in range(len(listlines)):
        names.append(listlines[i][0])


    voting_record = []
    for i in range(len(listlines)):
        voting_record.append(listlines[i][3: ])

    voting = []
    for item in voting_record:
        voting.append([int(v) for v in item])

        
    d1= dict(zip(names, voting))
   
    return d1  
    

## Task 2

def policy_compare(sen_a, sen_b, voting_dict):
    """
    Input: last names of sen_a and sen_b, and a voting dictionary mapping senator
           names to lists representing their voting records.
    Output: the dot-product (as a number) representing the degree of similarity
            between two senators' voting policies
    Example:
        >>> voting_dict = {'Fox-Epstein':[-1,-1,-1,1],'Ravella':[1,1,1,1]}
        >>> policy_compare('Fox-Epstein','Ravella', voting_dict)
        -2
    """

    result = sum([i*j for (i,j) in zip(voting_dict[sen_a],voting_dict[sen_b])])
    return result


## Task 3

def most_similar(sen, voting_dict):
    list2=[]
    list1=[]
    for item in voting_dict.keys():
        if item == sen:
            pass
        else:
            score = (sum([i*j for (i,j) in zip(voting_dict[sen],voting_dict[item])]))
            list1.append(score)
            list2.append(item)

    indices = [i for i, x in enumerate(list1) if x == max(list1)]
    
    for element in indices:
        return list2[element]
    
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is most
            like the input senator (excluding, of course, the input senator
            him/herself). Resolve ties arbitrarily.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> most_similar('Klein', vd)
        'Fox-Epstein'

    Note that you can (and are encouraged to) re-use you policy_compare procedure.
    """
    

    

## Task 4

def least_similar(sen, voting_dict):
    dict1={}
    list1=[]
    list2=[]
    for item in voting_dict.keys():
        if item == sen:
            pass
        else:
   
            score = (sum([i*j for (i,j) in zip(voting_dict[sen],voting_dict[item])]))
            dict1[item]=score
            list1.append(score)
            list2.append(item)

    indices = [i for i, x in enumerate(list1) if x == min(list1)]

    
    for element in indices:
        return list2[element]
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is least like the input
            senator.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> least_similar('Klein', vd)
        'Ravella'
    """
   
    
    

## Task 5

most_like_chafee    = 'Jeffords'
least_like_santorum = 'Feingold' 



# Task 6

def find_average_similarity(sen, sen_set, voting_dict):
    list_sen = list(sen_set)
    accum = 0
    for i in range(len(list_sen)):
        result = sum([i*j for (i,j) in zip(voting_dict[sen],voting_dict[list_sen[i]])])
        accum = accum + result
    return accum/len(list(sen_set)) 
    """
    Input: the name of a senator, a set of senator names, and a voting dictionary.
    Output: the average dot-product between sen and those in sen_set.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> find_average_similarity('Klein', {'Fox-Epstein','Ravella'}, vd)
        -0.5
        
    hint: use most_similar('ave_dem_record',vd2)

    vd2 = the big list plus the key:value entry for "ave_dem_record found in Task 7.
    
    """

most_average_Democrat = 'Biden'





# Task 7

def find_average_record(sen_set, voting_dict):
    list_sen = list(sen_set)
    accumlist=[]
    for item in list_sen:
        accumlist.append(voting_dict[item])

    [sum(x)/len(list_sen) for x in zip(*accumlist)]

    return [sum(x)/len(list_sen) for x in zip(*accumlist)]
    """
    Input: a set of last names, a voting dictionary
    Output: a vector containing the average components of the voting records
            of the senators in the input set
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> find_average_record({'Fox-Epstein','Ravella'}, voting_dict)
        [-0.5, -0.5, 0.0]
    """
   
average_Democrat_record = [-0.16279069767441862, -0.23255813953488372, 1.0, 0.8372093023255814,
                           0.9767441860465116, -0.13953488372093023, -0.9534883720930233, 0.813953488372093,
                           0.9767441860465116, 0.9767441860465116, 0.9069767441860465, 0.7674418604651163,
                           0.6744186046511628, 0.9767441860465116, -0.5116279069767442, 0.9302325581395349,
                           0.9534883720930233, 0.9767441860465116, -0.3953488372093023, 0.9767441860465116,
                           1.0, 1.0, 1.0, 0.9534883720930233, -0.4883720930232558, 1.0, -0.32558139534883723,
                           -0.06976744186046512, 0.9767441860465116, 0.8604651162790697, 0.9767441860465116,
                           0.9767441860465116, 1.0, 1.0, 0.9767441860465116, -0.3488372093023256, 0.9767441860465116,
                           -0.4883720930232558, 0.23255813953488372, 0.8837209302325582, 0.4418604651162791,
                           0.9069767441860465, -0.9069767441860465, 1.0, 0.9069767441860465, -0.3023255813953488]


# Task 8

def bitter_rivals(voting_dict):
    key = voting_dict.keys()
    names = list(key)
    names.sort()

    import itertools

    combo_list = list(itertools.combinations(names,2))

    empty_list = []
    for (i,j) in combo_list:
        empty_list.append(policy_compare(i,j,voting_dict))

    x = min(empty_list)
    index_num = empty_list.index(x)

    return combo_list[index_num]
    
    """
    Input: a dictionary mapping senator names to lists representing
           their voting records
    Output: a tuple containing the two senators who most strongly
            disagree with one another.
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> bitter_rivals(voting_dict)
        ('Fox-Epstein', 'Ravella')
    """
  

