
def minSubArraySum(nums):
    if not nums:
        return 0

    min_sum = float('inf')
    current_sum = 0
    start = 0

    for end in range(len(nums)):
        current_sum += nums[end]

        while current_sum >= 0:
            min_sum = min(min_sum, current_sum)
            current_sum -= nums[start]
            start += 1

    return min_sum if min_sum != float('inf') else 0
