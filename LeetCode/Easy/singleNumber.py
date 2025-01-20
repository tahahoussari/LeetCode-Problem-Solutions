def single_number(nums):
    if len(nums) == 1:
        return nums[0]

    for i in range(len(nums)):
        ls = nums[:i] + nums[i+1:]
        if nums[i] not in ls:
            return nums[i]

    

print(single_number([2,2,1]))

print(single_number([4,1,2,1,2]))

print(single_number([1]))