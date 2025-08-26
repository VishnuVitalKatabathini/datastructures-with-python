def threeSumClosest(nums,target):
    csum = {}
    nums.sort()
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        j, k = i + 1, len(nums) - 1
        while j < k:
            currSum = nums[i] + nums[j] + nums[k]
            diff = currSum - (target)
            if diff < 0:
                diff = -1 * diff
            csum[diff] = currSum
            if currSum <= target:
                j += 1
            elif currSum > target:
                k -= 1
    print(csum)
    min_diff = min(csum.keys())
    return csum[min_diff]

print(threeSumClosest([-4,2,2,3,3,3],0))