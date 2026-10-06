
def minSubArraySum(nums):
    if not nums:
        return 0

    min_sum = float('inf')
    window_sum = 0

    for i in range(len(nums)):
        window_sum += nums[i]
        if window_sum < min_sum:
            min_sum = window_sum
        window_sum -= nums[i - len(nums) + 1] if i >= len(nums) else 0

    return min_sum
