EXPECTED_BAKE_TIME = 40
    
# equal to the time it takes to prepare a single layer
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.add()
    
    Args: 
        elapsed_bake_time (int): baking time already elapsed

    Returns:
        int: remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time

# and consider using 'PREPARATION_TIME' here
def preparation_time_in_minutes(layers):
    """Calculate the preparation time based on the number of layers.

    Args:
        layers (int): the number of layers in a lasagna

    Returns:
        int: the amount of time it takes to prepare a lasagna based on the number of layers
    """
    return layers * PREPARATION_TIME

def elapsed_time_in_minutes(layers, elapsed_bake_time):
    """Calculate the total number of minutes you've been cooking, or the sum of your preparation time and the time the lasagna has already spent baking in the oven.

    Args:
        layers (int): the number of layers in a lasagna
        elapsed_bake_time (int): the time the lasagna has been cooking

    Returns:
        int: the total number of bake time 
    """
    return preparation_time_in_minutes(layers) + elapsed_bake_time
