"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Amount of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    # keeps track of how many existing Aliens there are
    total_aliens_created = 0

    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        # update the number of existing Aliens
        Alien.total_aliens_created += 1
    
    
    def hit(self):
        """
        Modifies the Alien's health if hit by
        1 point.
        """
        self.health -= 1
    
    
    def is_alive(self):
        """
        Determines whether or not the alien
        is still alive.
        
        :return: Boolean
        """
        
        return self.health > 0
    
    
    def teleport(self, x_coordinate, y_coordinate):
        """
        Aliens have the ability to teleport.
        Takes new x-coordinates and y-coordinates,
        and changes the alien's cooridnates
        accordingly.
        
        :param x_coordinate, y_coordinate: int:
        """
        
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        
    
    def collision_detection(self, something):
        """
        Not ready to implement just yet.
        """
        
        pass


def new_aliens_collection(positions):
    """
    Create a list of Aliens objects, given a
    list of positions (as tuples).
    
    :param positions: tuple(int) - x-y coordinates
    :return: list(Alien)
    """
    
    return [Alien(position[0], position[1]) for position in positions]