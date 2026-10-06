
def prod_signs(arr):
    if not arr:
        return None
    product = 1
    for num in arr:
        product *= num
    return abs(product)
