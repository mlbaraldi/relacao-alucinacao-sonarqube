
def prod_signs(arr):
    if not arr:
        return None
    product = 1
    for num in arr:
        sign = 1 if num > 0 else -1 if num < 0 else 0
        product *= sign
    return product
