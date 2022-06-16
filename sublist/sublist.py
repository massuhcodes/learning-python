"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "sublist"
SUPERLIST = "superlist"
EQUAL = "equal"
UNEQUAL = "unequal"


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    len_of_list_one = len(list_one)
    len_of_list_two = len(list_two)
    # sublist route
    if len_of_list_one < len_of_list_two:
        for i in range(len_of_list_two):
            # compare list-one with an equal length sublist from list-two
            if list_one == list_two[i:i+len_of_list_one]:
                return SUBLIST
        else:
            return UNEQUAL
    # superlist route
    elif len_of_list_one > len_of_list_two:
        for i in range(len_of_list_one):
            # compare list-two with an equal length sublist from list-one
            if list_two == list_one[i:i+len_of_list_two]:
                return SUPERLIST
        else:
            return UNEQUAL
    # lists are in no way related
    else:
        return UNEQUAL