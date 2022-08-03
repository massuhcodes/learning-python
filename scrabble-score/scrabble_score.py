# Compute the Scrablle score

# how the score should be computed
rubric = {
    ('a','e','i','o','u','l','n','r','s','t'): 1,
    ('d','g'): 2,
    ('b','c','m','p'): 3,
    ('f','h','v','w','y'): 4,
    ('k'): 5,
    ('j','x'): 8,
    ('q','z'): 10
}

def score(word):
    """
    Given a word, compute the Scrablle score for that word.
    
    :param word: string - the given word to compute the score from
    
    :return total: - int - the score computed from the word
    """
    word = word.lower()
    total = 0
    for letter in word:
        for key in rubric.keys():
            if letter in key:
                total += rubric[key]
    return total
