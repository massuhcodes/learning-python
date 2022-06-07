"""Determine whether or not a given number is an armstrong number"""

def is_armstrong_number(number):
    """Find out whether or not the input number is indeed an armstrong number
    :param: int - number in question
    :return: bool - armstrong number validity
    """
    num_arr = list(str(number))
    total = 0
    for num in num_arr:
        total += pow(int(num), len(num_arr))
    return total == number