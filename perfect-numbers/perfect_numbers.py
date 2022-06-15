# Creating a function to determine if a number is perfect,
# abundant, or deficient based on Nicomachus' (60 - 120) CE
# classification scheme for positive integers --
# aliquot sum (https://en.wikipedia.org/wiki/Aliquot_sum)


def classify(number):
    """ A perfect number equals the sum of its positive divisors.
    :param number: int a positive integer
    :return: str the classification of the input integer
    The aliquot sum is defined as the sum of the factors of
    a number not including the number itself.
    For example, the aliquot sum of 15 is (1+3+5) = 9
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    factors = {integer for integer in list(range(1,number)) if number % integer == 0}
    aliquotSum = sum(factors)
    if aliquotSum == number:
        return "perfect"
    elif aliquotSum > number:
        return "abundant"
    elif aliquotSum < number:
        return "deficient"
