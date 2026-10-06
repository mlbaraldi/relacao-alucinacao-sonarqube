
def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    """
    if not nums:
        return 0  # Assuming return 0 for empty array, though problem states nums is given
    current_min = global_min = nums[0]
    for num in nums[1:]:
        current_min = min(num, current_min + num)
        global_min = min(global_min, current_min)
    return global_min
