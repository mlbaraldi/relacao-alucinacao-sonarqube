
def multiply(a, b):
    # Calculate the product of the unit digits of a and b
    product = a % 10 * b % 10
    
    # If the product is greater than 10, return the sum of the digits
    if product > 10:
        return product % 10
    else:
        return product
