def len1(nums,k):
    pre=0
    map1={0:-1}
    ans=float('-inf')
    for i in range(len(nums)):
        pre+=nums[i]
        res=pre-k
        if pre not in map1:
            map1[pre]=i
        if res in map1:
            ans=max(ans, i-map1[res])
    return ans
nums = [1, -1, 5, -2, 3]
k = 3
print(len1(nums,k))