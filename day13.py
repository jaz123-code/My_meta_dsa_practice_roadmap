def first(nums,target):
    left=0
    right=len(nums)-1
    ans=-1
    while left<=right:
        mid=(right+left)//2
        if nums[mid]==target:
            ans=mid
            right=mid-1
        elif nums[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return ans
nums=[1, 2, 2, 2, 3]
target=2
print(first(nums,target))