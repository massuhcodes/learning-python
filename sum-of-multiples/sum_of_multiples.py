# Given a number, find the sum of all the unique multiples
# of particular numbers up to but not including that
# number

# useful for it reduce tool
import functools

def sum_of_multiples(limit, multiples):
    """
    Given a number, find the sum of all the unique
    multiples of particular numbers up to but not
    including that number.
    
    :param limit: int - the excluded endpoint
    :param multiples: list(int) - a list of integers to
    be tested on
    :return: int - the sum of passed multiples
    """    
    multiples_set = set()
    for multiple in multiples:
        if multiple < limit and multiple > 0:
            multiples_set.update(range(multiple, limit, multiple))
    return functools.reduce(lambda a,b: a+b, multiples_set) if multiples_set else 0