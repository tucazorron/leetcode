def solution(nums, k):
    nums.sort()
    i, j, pairs = 0, 1, set()
    while j < len(nums):
        if i == j:
            j += 1
        elif nums[j] - nums[i] < k:
            j += 1
        elif nums[j] - nums[i] > k:
            i += 1
        else:
            pairs.add((nums[i], nums[j]))
            i += 1
            j += 1
    return len(pairs)
