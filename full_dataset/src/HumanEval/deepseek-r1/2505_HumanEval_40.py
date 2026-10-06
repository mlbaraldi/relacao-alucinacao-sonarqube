

def triples_sum_to_zero(l: list):
    """
    Determines if there are three distinct elements in the list that sum to zero.
    """
    n = len(l)
    if n < 3:
        return False
    nums = sorted(l)
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicate elements to avoid redundant checks
        left, right = i + 1, n - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == 0:
                return True
            elif current_sum < 0:
                left += 1
            else:
                right -= 1
    return False
