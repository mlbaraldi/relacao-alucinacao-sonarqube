
def bf(planet1, planet2):
    '''
    Returns a tuple of planets between the orbits of planet1 and planet2, sorted by proximity to the sun.
    '''
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return ()
    i1 = planets.index(planet1)
    i2 = planets.index(planet2)
    start, end = sorted([i1, i2])
    between = planets[start + 1 : end]
    return tuple(between)
