# Determining the resistor value based on the given color

colorCodes = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9
}

def color_code(color):
    """
    Return the code based on the given color
    :param color: string - the color in question
    :return: int - the code for the color
    """
    return colorCodes[color]


def colors():
    """
    Returns a list of colors that would be found in a resistor
    :return: [string] - all the colors
    """
    return list(colorCodes.keys())
