"""Calculates the number of grains for both a board-square and the entire board"""

def square(number):
    """Calculate the number of grains for a board-square
    :param number: int - position number of a board-square
    :raises: ValueError - param number cannot be less than 0 nor greater than 64
    :return: int - the number of grains at the board-square
    """
    if number > 0 and number < 65:
        return pow(2, number - 1)
    else:
        raise ValueError("square must be between 1 and 64")


def total():
    """Calculate the number of grains for the entire board
    :return: int - the total number of grains in the board
    """
    total_grains = 0
    for number in range(1, 65):
        total_grains += square(number)
    return total_grains
