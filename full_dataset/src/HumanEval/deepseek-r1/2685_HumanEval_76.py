
def is_simple_power(x, n):
    if x == 1:
        return n != 0  # n^0 = 1 for any non-zero n
    if x == 0:
        return n == 0  # Only 0^k (k>0) equals 0
    if n == 0:
        return False   # x is non-zero, so can't be a power of 0
    if n == 1:
        return x == 1  # 1^k is always 1
    
    # Check for positive exponents (k >= 0)
    product = 1
    while True:
        product *= n
        if product == x:
            return True
        if abs(product) > abs(x):
            break
    
    # Check for negative exponents (k < 0)
    reciprocal_x = 1 / x
    product_recip = 1
    while True:
        product_recip *= n
        if product_recip == reciprocal_x:
            return True
        if product_recip > reciprocal_x:
            return False
