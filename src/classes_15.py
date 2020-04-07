# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor
"""this an app that makes Geocache location"""
# YOUR CODE HERE

class LatLon:
    """lat and Lon class"""
    def __init__(self, lat, lon):
        """coordinates"""
        self.lat = lat
        self.lon = lon

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE

class Waypoint(LatLon):
    """Waypoint class"""
    def __init__(self, name, lat, lon):
        """set places"""
        super().__init__(lat, lon)
        self.name = name

    def __str__(self):
        """return info"""
        return f"Name: {self.name} Lat: {self.lat} Lon: {self.lon}"

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE

class Geocache(LatLon):
    """Geocaching class"""
    def __init__(self, name, difficulty, size, lat, lon):
        """Geocache info"""
        super().__init__(lat, lon,)
        self.name = name
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        """Geocache Display info"""
        return f"Name: {self.name} Difficulty: {self.difficulty}\
                Size: {self.size} Lat: {self.lat} Lon: {self.lon}"

# Make a new Waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE

MYWAYPOINT = Waypoint("Catacombs", 41.70505, -121.51521)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(MYWAYPOINT)

# Make a new Geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

NEWGEOCACHE = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
print(NEWGEOCACHE)
