def maxw(nums):
    l = 0
    r = len(nums)-1
    max_area = 0
    while l < r:
        current_area = min(nums[l], nums[r]) * (r - l)
        max_area = max(max_area, current_area)
        if nums[l] < nums[r]:
            l += 1
        else:
            r -= 1
    return max_area
nums=[1,8,6,2,5,4,8,3,7]
print(maxw(nums))