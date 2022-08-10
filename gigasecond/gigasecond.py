from datetime import timedelta

def add(moment):
    """
    Given a moment, determine the moment that would be after a
    gigasecond has passed (giga = 1e9)
    
    :param moment: datetime
    
    :returns - datetime
    """
    # use timedelta to add the seconds to the datetime which will
    # yield a new datetime
    return moment + timedelta(seconds=1e9)
