
def bf(planet1, planet2):
    # Check if the planet names are valid
    if planet1 not in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"] or planet2 not in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        return ()

    # Get the indices of the planets in the order of their orbits
    planet_indices = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"].index(planet1), ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"].index(planet2)

    # Get the planets between the orbits of planet1 and planet2
    planets_between = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"][planet_indices[0]:planet_indices[1]]

    # Sort the planets by proximity to the Sun
    planets_between.sort(key=lambda x: x.distance_from_sun)

    return tuple(planets_between)
