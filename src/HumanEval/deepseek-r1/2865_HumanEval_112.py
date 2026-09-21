
def reverse_delete(s,c):
    c_set = set(c)
    filtered_str = ''.join([char for char in s if char not in c_set])
    is_palindrome = filtered_str == filtered_str[::-1]
    return (filtered_str, is_palindrome)
