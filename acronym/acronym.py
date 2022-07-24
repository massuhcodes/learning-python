# Convert a phrase to its acronym

import re

def abbreviate(words):
    """
    Convert a phrase to its acronym
    
    :param words: str - a phrase to convert
    :return acronym: str - a abbreivated form of the phrase
    """
    words = re.sub(r'[^a-zA-Z\']', ' ', words).split(' ')
    # as long as there are empty spaces, remove them
    while '' in words:
        words.remove('')
    acronym = ''.join([word[0].upper() for word in words])
    return acronym
