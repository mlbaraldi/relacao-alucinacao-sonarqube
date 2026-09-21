
def minSubArraySum(nums):
    min_sum = float('inf')
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            min_sum = min(min_sum, sum(nums[i:j+1]))
    return min_sum
