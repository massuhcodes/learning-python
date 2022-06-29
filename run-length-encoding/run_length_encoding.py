# encode and decode string functionality

def decode(string):
    """
    Decode a string based on its content (e.g 34A4BC) to
    a non-numerical string
    
    :param string: str - string to decode
    :return: str - the decoded string
    """
    decoded = ""
    if string != "":
        multiplier = ""
        for char in string:
            if char.isdigit():
                multiplier += char
            else:
                # if multiplier is still empty, default
                # multiplier is 1
                if multiplier == "":
                    multiplier = "1"
                decoded += int(multiplier) * char
                # reset
                multiplier = ""
    return decoded


def encode(string):
    """
    Encode a string based on its non-numerical content
    (e.g AAABBBCCCD to 3A3B3CD)
    
    :param string: str - string to encode
    :return: str - the encoded string
    """
    encoded = ""
    if string != "":
        initial = string[0]
        count = 0
        for char in string:
            if char == initial:
                count += 1
            else:
                encoded += "{}{}".format(count,initial) if count > 1 else initial
                # reset
                initial = char
                count = 1
        # accounting for the final character value which does
        # get added to the encoded string
        encoded += "{}{}".format(count,initial) if count > 1 else initial
    return encoded
