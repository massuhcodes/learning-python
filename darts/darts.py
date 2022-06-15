# Creating a function to calculate dart throw score

def score(x, y):
    """Calculates and returns earned score in a single toss of a Darts game
    :param x: int - the dart's horizontal distance from the center of the target
    :param y: int - the dart's vertical distance from the center of the target
    :return: int - the earned score based on where the dart landed
    """
    OUTER_RADIUS = 10
    MIDDLE_RADIUS = 5
    INNER_RADIUS = 1
    # using the pythagorean theorm to get the point's radius
    test = pow(pow(x,2) + pow(y,2), 0.5)
    if test > OUTER_RADIUS:
        return 0
    elif MIDDLE_RADIUS < test <= OUTER_RADIUS:
        return 1
    elif INNER_RADIUS < test <= MIDDLE_RADIUS:
        return 5
    elif test <= INNER_RADIUS:
        return 10
