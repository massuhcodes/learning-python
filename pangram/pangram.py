# Function for figuring out a pangram

import string

def is_pangram(sentence):
    """Determine if a sentence is a pangram.
    :param sentence: str - the value in question
    :return: boolean - whether the sentence is a pangram or not 
    
    A pangram is a sentence using every letter of the alphabet at least once.
    """
    unwantedChars = set(string.punctuation + string.whitespace + "0123456789")
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    sentence = set(sentence.lower()) - unwantedChars
    return sentence == alphabet
