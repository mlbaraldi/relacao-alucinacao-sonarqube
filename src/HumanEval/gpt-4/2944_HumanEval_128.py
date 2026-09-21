
def prod_signs(arr):
    if not arr:
        return None
    else:
        product_of_signs = 1
        sum_of_magnitudes = 0
        for num in arr:
            if num < 0:
                product_of_signs *= -1
                sum_of_magnitudes += abs(num)
            elif num > 0:
                sum_of_magnitudes += num
        return sum_of_magnitudes * product_of_signs
