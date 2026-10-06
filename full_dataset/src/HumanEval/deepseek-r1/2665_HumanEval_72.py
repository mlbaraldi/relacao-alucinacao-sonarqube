
def will_it_fly(q,w):
    # Check if the list is a palindrome
    if q != q[::-1]:
        return False
    # Check if the sum of elements is within the allowed weight
    return sum(q) <= w
