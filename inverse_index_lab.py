from random import randint
from dictutil import *

## Task 1
def movie_review(name):
    """
    Input: the name of a movie
    Output: a string (one of the review options), selected at random using randint
    """
    review_options = ["See it!", "A gem!", "Ideological claptrap!"]
    return review_options[randint(0,2)]

## Tasks 2 and 3 are in dictutil.py

## Task 4    
def makeInverseIndex(strlist):
    T={i:s for (i,s) in enumerate(strlist)}
    keys = T.keys()
    values=T.values()

    values2=[]
    for i in values:
        values2.append(set(i.split()))

    keys2=[]
    for i in range(len(values2)):
        keys2.append(i)    
        
    dictionary = dict(zip(keys2,values2))
    
    iterlist = []
    for i in strlist:
        iterlist = iterlist + i.split()
        
    word=set(iterlist) 

    finaldict={}
    for item in word:
        for index in range(len(dictionary)):
            if item in dictionary[index]:
                if not (item in finaldict):
                    finaldict[item]= {index}
                else:
                    finaldict[item].update({index})
            else:
                pass

    return finaldict 
    """
    Input: a list of documents as strings
    Output: a dictionary that maps each word in any document to the set consisting of the
            document ids (ie, the index in the strlist) for all documents containing the word.

    Note that to test your function, you are welcome to use the files stories_small.txt
      or stories_big.txt included in the download.
    """
    return ...

## Task 5
S=set()
def orSearch(inverseIndex, query):
    for word in query:
        if word in inverseIndex:
            S.update(inverseIndex[word])
    return S        
            
            
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query, query  = ['now','a']
    >>> inverse_index = {'should': {3}, 'first': {0}, 'now': {4}, 'fourth': {3}, 'document': {0, 1, 2, 3}, 'is': {0, 1, 2, 4}, 'a': {2, 3, 4}, 'this': {0, 1, 2}, 'there': {3, 4}, 'second': {1}, 'third': {2}, 'and': {2, 4}, 'fifth': {4}, 'be': {3}, 'the': {0, 1}, 'perhaps': {3}, 'too': {4}}
    Output: the set of document ids that contain _any_ of the specified words
    {2,3,4}
    """


## Task 6

def andSearch(inverseIndex, query):
    L=[]
    for word in query:
        if word in inverseIndex:
            L.append(inverseIndex[word])
        else:
            pass
    result = set.intersection(*L)
    return result

    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query,  query  = ['now','a']
    >>> inverse_index = {'should': {3}, 'first': {0}, 'now': {4}, 'fourth': {3}, 'document': {0, 1, 2, 3}, 'is': {0, 1, 2, 4}, 'a': {2, 3, 4}, 'this': {0, 1, 2}, 'there': {3, 4}, 'second': {1}, 'third': {2}, 'and': {2, 4}, 'fifth': {4}, 'be': {3}, 'the': {0, 1}, 'perhaps': {3}, 'too': {4}}
    Output: the set of all document ids that contain _all_ of the specified words
    {4}
    """

