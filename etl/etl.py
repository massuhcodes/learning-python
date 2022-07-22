# Trasform the legacy scrabble data format 
# to the shiny new scrabble data

def transform(legacy_data):
    """
    Transform the legacy scrabble data format
    to the shiny new scrabble data
    
    :param legacy_data: dict(int: Array(str)) - the old scrabble format
    :return data: dict(str: int) - the new scrabble format
    """
    data = {}
    for key, letters in legacy_data.items():
        for letter in letters:
            data[letter.lower()] = key
    return data