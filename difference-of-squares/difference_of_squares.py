# Finding the difference between the square of the sum and the sum of the squares of the first N natural numbers

def square_of_sum(number):
    """Square the sum of the total
    :param number: int - the endpoint of the range to total
    :return: int - the square of the total
    """
    total = 0
    for num in range(1, number + 1):
        total += num
    return pow(total, 2)


def sum_of_squares(number):
    """Sum the squares
    :param number: int - the endpoint of the range to total
    :return: int - the total of the squares
    """
    total = 0
    for num in range(1, number + 1):
        total += pow(num, 2)
    return total


def difference_of_squares(number):
    """Find the difference between the square of the sum and sum of the squares
    :param number: int - the endpoint of the range to total
    :return: int - the difference
    """
    return square_of_sum(number) - sum_of_squares(number)
