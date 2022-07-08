def solution(nums, target):
    dic = {}
    for i in range(len(nums)):
        if target - nums[i] not in dic:
            dic[nums[i]] = i
        return [i, dic[target - nums[i]]]
