## Task 2



def dict2list(dct, keylist): return [dct[keylist[i]] for i in range(0,len(keylist))]

def list2dict(L, keylist): return {keylist[i]:L[i] for i in range(0,len(L))}


## Task 3

def listrange2dict(L): return {i:l for (i,l) in enumerate(L)}

