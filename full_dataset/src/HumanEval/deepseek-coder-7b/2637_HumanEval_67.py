
def fruit_distribution(s,n):
    # Split the string to get the number of apples and oranges
    fruits = s.split(' and ')
    apples = int(fruits[0].split()[0])
    oranges = int(fruits[1].split()[0])

    # Calculate the number of mango fruits
    mango_fruits = n - apples - oranges

    return mango_fruits
