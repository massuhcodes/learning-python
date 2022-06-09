# convert a number into a string that contains raindrop sounds corresponing to certain potential factors

def convert(number):
    """Test the number in each case to get sounds of raindrops (7, 5, and 3 are the tests)
    :param number: int - the subject in question
    :return: str - the string value which can be either the sounds of raindrop or the number itself
    """
    raindropSounds = ""
    if number % 7 == 0:
        raindropSounds = "Plong" + raindropSounds
        if number % 5 == 0:
            raindropSounds = "Plang" + raindropSounds
            if number % 3 == 0:
                # divisible by 7, 5, and 3
                raindropSounds = "Pling" + raindropSounds
        elif number % 3 == 0:
            # divisible by 7, 3, except for 5
            raindropSounds = "Pling" + raindropSounds
    elif number % 5 == 0:
        raindropSounds = "Plang" + raindropSounds
        if number % 3 == 0:
            # divisible by 5 and 3 only
            raindropSounds = "Pling" + raindropSounds
    elif number % 3 == 0:
        raindropSounds = "Pling" + raindropSounds
    else:
        # return the number in string format if all else fails
        return str(number)
    return raindropSounds
