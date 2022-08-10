# Create randomized names for robots

from string import ascii_uppercase, digits
from random import choice, seed

class Robot:
    def __init__(self):
        self.name = self.generateName()
        
    def reset(self):
        """
        Will generate a new name.
        """
        # seed for different output each execution
        seed("Must be a random name")
        self.name = self.generateName()
        
    def generateName(self):
        """
        A robot name consists of 2 uppercased letters and
        3 digits.
        
        :returns name: str - the name of the robot
        """
        name = ""
        for _ in range(2):
            name += choice(ascii_uppercase)
        for _ in range(3):
            name += choice(digits)
        return name