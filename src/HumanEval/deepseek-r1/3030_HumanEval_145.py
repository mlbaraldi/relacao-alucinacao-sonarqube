
def order_by_points(nums):
    """
    Sorts the given list of integers based on the sum of their digits.
    In case of a tie, the original order is preserved.
    """
    def sum_digits(n):
        return sum(int(digit) for digit in str(abs(n)))
    
    # Create a list of tuples containing the sum of digits, original index, and the number
    decorated = [(sum_digits(num), idx, num) for idx, num in enumerate(nums)]
    
    # Sort by the sum of digits first, then by the original index to maintain stability
    decorated.sort(key=lambda x: (x[0], x[1]))
    
    # Extract the numbers in the sorted order
    return [num for (sum_, idx, num) in decorated]
