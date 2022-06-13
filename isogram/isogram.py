# Test whether a string is an isogram or not

from collections import Counter
from string import punctuation, whitespace

def is_isogram(string):
    """Test the given string to see whether or not it is an isogram
    :param string: str - the word in question
    :return: boolean - whether or not the given string is an isogram
    """
    unwantedChars = set(punctuation + whitespace)
    filteredString = "".join(["" if char in unwantedChars else char for char in string.lower()])
    counter = Counter(filteredString)
    return all([True if occurences == 1 else False for occurences in list(counter.values())])