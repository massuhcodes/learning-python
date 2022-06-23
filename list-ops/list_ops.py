# Implement basic list operations without using existing functions

def append(list1, list2):
    """
    Given two lists, all all items in the second list
    to be the end of the first list
    
    :param list1,list2: [Any] - a list comprising of any data type
    
    :return: [Any] - an append list
    """
    return list1 + list2


def concat(lists):
    """
    Given a series of lists, combine all items in all lists
    into one flattened list
    
    :param lists: [[Any]] - a list of lists comprised of
    any data type
    
    :return: [Any] - a concatenated list
    """
    containingList = []
    for l in lists:
        containingList += l
    return containingList


def filter(predicate, list):
    """
    Given a predicate and a list, return the list of all
    items for which the predicate is true
    
    :param predicate: function - a function that takes in an item for filtering
    :param list: [Any] - a list comprising of any data type
    
    :return: [Any] - a list containing the filtered values
    """
    containingList = []
    for item in list:
        if predicate(item):
            containingList += [item]
    return containingList


def length(list):
    """
    Given a list, return the total number of items within it
    
    :param list: [Any] - a list comprising of any data type
    
    :return: int - a number representing the length of the list
    """
    total = 0
    for _ in list:
        total += 1
    return total


def map(function, list):
    """
    Given a function and a list, return the list of the
    results of applyting the predicate on all items
    
    :param function: function - a function that takes in an item for mapping
    
    :return: [Any] - a list containing the mapped values
    """
    containingList = []
    for item in list:
        containingList += [function(item)]
    return containingList


def foldl(function, list, initial):
    """
    Given a function and a list, and initial accumulator,
    fold (reduce) each item into the accumulator from the
    left using said function
    
    :param function: function - a function that takes in an accumulator and an item
    :param list: [Any] - a list comprising of any data type
    :param initial: Any - any data type that can be added to
    
    :return: the accumulated result
    """
    accumulator = initial
    for item in list:
        accumulator = function(accumulator, item)
    return accumulator


def foldr(function, list, initial):
    """
    Given a function and a list, and initial accumulator,
    fold (reduce) each item into the accumulator from the
    right using said function
    
    :param function: function - a function that takes in an item and an accumulator
    :param list: [Any] - a list comprising of any data type
    :param initial: Any - any data type that can be added to
    
    :return: the accumulated result
    """
    accumulator = initial
    for item in reverse(list):
        accumulator = function(item, accumulator)
    return accumulator


def reverse(list):
    return list[::-1]
