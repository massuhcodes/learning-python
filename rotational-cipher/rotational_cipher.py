# Create an implementation of the rotational
# cipher, also called the Caesar cipher.

def rotate(text, key):
    """
    Rotate the text with the given key
    
    :param text: str - the given string
    :param key: int - the distance to rotate by
    
    :return rotated_text: the rotated text
    """
    rotated_text = ""
    for letter in text:
        if letter.islower():
            rotated_text += rotate_with_bounds('a','z',letter,key)
        elif letter.isupper():
            rotated_text += rotate_with_bounds('A','Z',letter,key)
        else:
            rotated_text += letter
    return rotated_text

def rotate_with_bounds(lower_bound, upper_bound, letter, key):
    """
    A helper method. If the distance passes the
    upper bound, add the overflow to the lower
    bound minus 1 (due to transition from z to a)
    """
    rotation_distance = ord(letter) + key
    if rotation_distance > ord(upper_bound):
        overflow = rotation_distance - ord(upper_bound) - 1
        return chr(ord(lower_bound) + overflow)
    return chr(rotation_distance)
    

print(rotate("Testing 1 2 3 testing", 4))