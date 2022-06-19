# Decipher binary strings into secret handshake

def commands(binary_str):
    """
    Given a binary string, decipher it in order to get
    the secret handshake
    
    "param binary_str: str - the given string
    "return: [str] - an array of steps to do when performing
    the secret handshake
    """
    handshake = []
    index_based_len = len(binary_str) - 1
    reverse_steps = False
    for (index, bit) in enumerate(binary_str):
        if bit == "1":
            normalized_binary_str = ('0' * index) + bit + ((index_based_len - index) * '0')
            if normalized_binary_str == "00001":
                handshake.insert(0, 'wink')
            elif normalized_binary_str == "00010":
                handshake.insert(0, 'double blink')
            elif normalized_binary_str == "00100":
                handshake.insert(0, 'close your eyes')
            elif normalized_binary_str == "01000":
                handshake.insert(0, 'jump')
            elif normalized_binary_str == "10000":
                reverse_steps = True
    return handshake[::-1] if reverse_steps else handshake