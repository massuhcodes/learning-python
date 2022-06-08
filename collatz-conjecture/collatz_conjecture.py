# Using the collatz Conjecture to find out how many steps it takes to reach 1

def steps(number):
    """Given a number, return the number of steps required to reach 1
    :param number: int - the number in questions to reach 1
    :return: int - the numbers of steps taken to reach 1
    
    Take any positive integer n. If n is even, divide n by 2 to get n / 2.
    If n is odd, multiply n by 3 and add 1 to get 3n + 1. Repeat the process indefinitely.
    The conjecture states that no matter which number you start with, you will always reach
    1 eventually.
    """
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    steps = 0
    while number > 1:
        steps += 1
        number = number / 2 if number % 2 == 0 else 3*number + 1
    return steps