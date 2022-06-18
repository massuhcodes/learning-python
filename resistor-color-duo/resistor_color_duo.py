# Get the value of the first two color bands

# color-value dictionary
colorCodes = {
    'black': '0',
    'brown': '1',
    'red': '2',
    'orange': '3',
    'yellow': '4',
    'green': '5',
    'blue': '6',
    'violet': '7',
    'grey': '8',
    'white': '9'
}

def value(colors):
    """
    Take each color name and output the combined value of the color bands
    
    :param colors: - [str]: an array of colors
    :return: int - the combined value of the color bands 
    """
    
    firstTwoColors = colors[:2]
    value = ''.join([colorCodes[color] for color in firstTwoColors])
    return int(value)
