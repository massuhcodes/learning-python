# Write a robot simulator

NORTH = 1
EAST = 2
SOUTH = 3
WEST = 4

class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.coordinates = (x_pos, y_pos)
        self.direction = direction
    
    def move(self, steps):
        """
        Funtionality that allows the robot to change
        directions and advance
        
        :param steps: str - instructions to take (R, L, or A)
        """
        for step in steps:
            if step == "R":
                self.direction += 1
                if self.direction > 4:
                    self.direction = 1
            elif step == "L":
                self.direction -= 1
                if self.direction < 1:
                    self.direction = 4
            elif step == "A":
                x_coord, y_coord = self.coordinates
                if self.direction == 1:
                    y_coord += 1
                elif self.direction == 2:
                    x_coord += 1
                elif self.direction == 3:
                    y_coord -= 1
                elif self.direction == 4:
                    x_coord -= 1
                self.coordinates = (x_coord, y_coord)