# Recute the nursery rhyme 'This is the House that Jack built'

verses = [
    "the house that Jack built.",
    "the malt that lay in ",
    "the rat that ate ",
    "the cat that killed ",
    "the dog that worried ",
    "the cow with the crumpled horn that tossed ",
    "the maiden all forlorn that milked ",
    "the man all tattered and torn that kissed ",
    "the priest all shaven and shorn that married ",
    "the rooster that crowed in the morn that woke ",
    "the farmer sowing his corn that kept ",
    "the horse and the hound and the horn that belonged to "
]

def recite(start_verse, end_verse):
    """
    Recite the verse going down
    
    :param start_verse, end_verse: int - index is not zero-based
    :return: list(str) - a list of strings reciting down
    """    
    if start_verse == end_verse:
        return [recite_verse(end_verse)]
    else:
        verses_reciting_down = []
        for number in range(start_verse, end_verse+1):
            verses_reciting_down.append(recite_verse(number))
        return verses_reciting_down


def recite_verse(number):
    """
    Reciting verses going down
    
    :param number: int - the point where the story begins to recite down
    """
    story = "This is "
    for verse in verses[number-1::-1]:
        story += "{0}".format(verse)
    return story