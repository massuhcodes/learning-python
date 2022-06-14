# Test whether given isbn is valid or not

def is_valid(isbn):
    """Test whether isbn is valid or not
    :param isbn: str - value in question
    :return: boolean - result whether test passed
    """
    filteredISBN = isbn.replace("-", "")
    if len(filteredISBN) != 10: return False
    total = 0
    for (char, index) in zip(filteredISBN, list(range(len(filteredISBN),0,-1))):
        if char == "X" and char == filteredISBN[-1]:
            total += index * 10
        elif char.isdigit():
            total += index * int(char)
        else:
            return False
    return total % 11 == 0