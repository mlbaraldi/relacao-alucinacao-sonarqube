
def prod_signs(arr):
    if not arr:
        return None
    
    sum_mag = sum(abs(x) for x in arr)
    product = 1
    
    for num in arr:
        if num == 0:
            product = 0
            break
        product *= 1 if num > 0 else -1
    
    return sum_mag * product
