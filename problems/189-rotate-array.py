def solution(nums, k):
    k = k % len(nums)
    for i, v in enumerate(nums[-k:]+nums[:-k]):
        nums[i] = v
    return nums
