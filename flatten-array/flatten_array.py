# Take a nested list and return a single flattened list
# with all values except nil/null

def flatten(iterable):
    """
    Takes a list and flattens it through recursion
    
    :param iterable: [Any] - an array that may contain
    non-iterable or iterable items
    
    :return: [Any] - a flattened array
    """
    newList = []
    for item in iterable:
        if type(item) == list:
            # the call will return a list so just concatenate (don't append because you will be appending a list to newList)
            newList += flatten(item)
        elif item == None:
            continue
        else:
            newList.append(item)
    return newList