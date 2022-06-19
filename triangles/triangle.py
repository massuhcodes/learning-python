# Determine if a triangle is equilateral, isosceles, or scalene

def equilateral(sides):
    """
    Determine if the sides form an equilateral triangle
    
    :param sides: [int] or [float] - an array of three sides
    :return: boolean - whether or not the sides form an equilateral triangle
    """
    
    return all([side == sides[0] and side != 0 for side in sides])


def isosceles(sides):
    """
    Determine if the sides form an isosceles triangle
    
    :param sides: [int] or [float] - an array of three sides
    :return: boolean - whether or not the sides form an isosceles triangle
    """
    
    a, b, c = sides
    return (a == b or b == c or a == c) and checkGeomety(a,b,c)


def scalene(sides):
    """
    Determine if the sides form an scalene triangle
    
    :param sides: [int] or [float] - an array of three sides
    :return: boolean - whether or not the sides form an scalene triangle
    """
    
    a, b, c = sides
    return (a != b and b != c and a != c) and checkGeomety(a,b,c)


def checkGeomety(a,b,c):
    """
    Determine if the sides form a triangle (Also reducing code smell by implementing DRY)
    
    :param a, b, c: int or float - sides of a triangle
    :return: boolean - whether or not the sides do form a triangle
    """
    return (
        checkTwoSidesLessThanThird(side1=a,side2=b,side3=c) and
        checkTwoSidesLessThanThird(side1=b,side2=c,side3=a) and
        checkTwoSidesLessThanThird(side1=a,side2=c,side3=b)
        )
    
    
def checkTwoSidesLessThanThird(side1,side2,side3):
    """
    Determine if the sides mathematically form a triangle
    
    :param side1, side2, side3: int or float - sides of a triangle
    :return: boolean - whether or not, mathematicallly, the sides do form a triangle
    
    For a shape to be a triangle at all, all sides have to
    be of length > 0, and them sum of the lengths of any
    two sides must be greater than or equal to the length
    of the third side
    """
    return (side1 + side2) >= side3