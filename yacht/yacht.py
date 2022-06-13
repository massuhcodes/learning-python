# Score categories.

# Useful for pythonic dictionaries
from collections import Counter

# Categories
YACHT = 12
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    """return the score of the category based on the given dice array value
    :param dice: [int] - five dice rolled
    :param category: int - the type in question
    :return: int - the score based on the category played
    Yacht is from the same family as Poker Dice, Generala and particulary
    Yahtzee, of which it is a precursor. In the game, five dice are rolled
    and the result can be entered in any of twelve categories. The score of
    a throw of the dice depends on the category chosen.
    """
    counter = Counter(dice)
    if category == YACHT:
        return 50 if len(counter) == 1 else 0
    elif (
        category == ONES or 
        category == TWOS or 
        category == THREES or 
        category == FOURS or 
        category == FIVES or 
        category == SIXES
        ):
        return counter[category] * category if category in counter else 0
    elif category == FULL_HOUSE:
        return sum(dice) if counter[max(counter, key=counter.get)] == 3 else 0
    elif category == FOUR_OF_A_KIND:
        return max(counter,key=counter.get) * FOURS if counter[max(counter, key=counter.get)] >= 4 else 0
    elif category == LITTLE_STRAIGHT:
        return 30 if sorted(dice) == [1,2,3,4,5] else 0
    elif category == BIG_STRAIGHT:
        return 30 if sorted(dice) == [2,3,4,5,6] else 0
    elif category == CHOICE:
        return sum(dice)