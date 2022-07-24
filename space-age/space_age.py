from pickle import MARK


class SpaceAge:
    
    MERCURY_ORBITAL_PERIOD = 0.2408467
    VENUS_ORBITAL_PERIOD = 0.61519726
    MARS_ORBITAL_PERIOD = 1.8808158
    JUPITER_ORBITAL_PERIOD = 11.862615
    SATURN_ORBITAL_PERIOD = 29.447498
    URANUS_ORBITAL_PERIOD = 84.016846
    NEPTUNE_ORBITAL_PERIOD = 164.79132
    EARTH_DAYS = 365.25
    EARTH_SECONDS = 31557600
    PRECISION = 2
    
    def __init__(self, seconds):
        self.seconds = seconds
        
    def on_earth(self):
        return round(self.get_earth_years(), SpaceAge.PRECISION)
    
    def on_mercury(self):
        return round(
            self.get_earth_years() / SpaceAge.MERCURY_ORBITAL_PERIOD,
            SpaceAge.PRECISION
        )
        
    def on_venus(self):
        return round(
            self.get_earth_years() / SpaceAge.VENUS_ORBITAL_PERIOD,
            SpaceAge.PRECISION
        )
        
    def on_mars(self):
        return round(
            self.get_earth_years() / SpaceAge.MARS_ORBITAL_PERIOD,
            SpaceAge.PRECISION
        )
        
    def on_jupiter(self):
        return round(
            self.get_earth_years() / SpaceAge.JUPITER_ORBITAL_PERIOD,
            SpaceAge.PRECISION
        )
        
    def on_saturn(self):
        return round(
            self.get_earth_years() / SpaceAge.SATURN_ORBITAL_PERIOD,
            SpaceAge.PRECISION
        )
        
    def on_uranus(self):
        return round(
            self.get_earth_years() / SpaceAge.URANUS_ORBITAL_PERIOD,
            SpaceAge.PRECISION
        )
        
    def on_neptune(self):
        return round(
            self.get_earth_years() / SpaceAge.NEPTUNE_ORBITAL_PERIOD,
            SpaceAge.PRECISION
        )

    def get_earth_years(self):
        return self.seconds / SpaceAge.EARTH_SECONDS