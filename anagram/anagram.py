# Get anagrams from a given word

from collections import Counter

def find_anagrams(word, candidates):
    """
    Return a list of approved candidates that are anagrams to given word
    
    :param word: string - the given word
    :param candidates: [string] - candidates that may or may not be anagrams of the given word
    :return anagrams: [string] or [] - either the anagrams or an empty list
    """
    anagrams = []
    word = word.lower()
    for candidate in candidates:
        temp = candidate.lower()
        if temp == word:
            continue
        if Counter(temp) == Counter(word):
            anagrams.append(candidate)
    return anagrams