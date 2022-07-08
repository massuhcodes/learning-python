# Get the slices from a string

def slices(series, length):
    """
    Given a string and specified length, return an array of slices of length
    
    :param series: string - the given string
    :param length: int - the specified length of the slice
    :return arr_of_slices: [string] or [] - an array of length-specified slices or nothing 
    """
    if len(series) < length and series != "":
        raise ValueError("slice length cannot be greater than series length")
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    if series == "":
        raise ValueError("series cannot be empty")
    arr_of_slices = []
    for i in range(len(series)):
        slice = series[i:i+length]
        if len(slice) == length:
            arr_of_slices.append(slice)
    return arr_of_slices
