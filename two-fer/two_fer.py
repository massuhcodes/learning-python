# Return a statement

def two_fer(name="you"):
    """
    Return a statement based on the given name value
    
    :param name: str - the name value given (defaut is "you")
    "return" str - the statement with the name value
    """
    
    return "One for {0}, one for me.".format(name)
