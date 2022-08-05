# Given a string determine whether or not a string is
# valid per the Luhn formula

import re
import functools

class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        """
        Check if a given string is valid
        
        :param self.card_num: str - a string to test on
        :return: bool - whether or not the given string is valid
        
        The Luhn alogrithm is used to validate a variety
        of id numbers like credit cards and Canadian SSNs
        """
        # card_num should not be 1 or less
        if len(self.card_num) <= 1:
            return False
        # get the set of all non-digit characters found
        character_set = set(re.findall("[^\d]", self.card_num))
        # non-digit character should only be a space or none at all
        if " " in character_set and len(character_set) == 1 or character_set == set():
            # remove the empty space and convert to list
            card_num_list = list(re.sub(" ", "", self.card_num))[::-1]
            # the reduce length should still not be 1 or less
            if len(card_num_list) <= 1:
                return False
            # convert the array into an array of ints
            card_num_list = [int(item) for item in card_num_list]
            # apply to only every other index starting from 1
            for index in range(1, len(card_num_list), 2):
                number = card_num_list[index]
                double = number * 2
                # subtract 9 from double if greater than 9
                card_num_list[index] = double - 9 if double > 9 else double
            # total-up the items
            total = functools.reduce(lambda a,b: a+b, card_num_list)
            # total should be the divisible to 10 to be valid
            return total % 10 == 0
        else:
            return False