
def fruit_distribution(s,n):
    # Split the string to get the number of apples and oranges
    parts = s.split()
    apples = int(parts[0])
    oranges = int(parts[2])

    # Subtract the number of apples and oranges from the total number of fruits
    mango = n - apples - oranges

    return mango
