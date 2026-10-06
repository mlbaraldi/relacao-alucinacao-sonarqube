
def order_by_points(nums):
    # Sort the list of integers in ascending order based on the sum of their digits
    sorted_nums = sorted(nums, key=lambda x: sum(map(int, str(x))))

    # If there are several items with similar sum of digits, order them based on their index in the original list
    sorted_nums = sorted(sorted_nums, key=lambda x: nums.index(x))

    return sorted_nums
