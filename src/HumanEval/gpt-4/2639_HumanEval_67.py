
def fruit_distribution(s,n):
    # Split the string into words
    words = s.split()
    # Get the number of apples and oranges from the string
    apples = int(words[0])
    oranges = int(words[3])
    # Calculate and return the number of mangoes
    return n - apples - oranges
