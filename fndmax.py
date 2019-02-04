#function findMaxLenSet.
def findMaxLenSet(lst):
    """(list) -> number
    returns the length of the biggest set found in
    an arbitrarily nested list.

    >>> val = findMaxLenSet([])
    >>> val
    0
    """
    #if list is empty, return 0.
    if(len(lst) == 0):
        return 0
    for item in lst:
        if(type(item) == set):
            print(item)
    

    
