def mono(nums):
    stack=[]
    out=[0]*len(nums)
    for i in range(len(nums)):
        while stack and nums[stack[-1]]<nums[i]:
            idx=stack.pop()
            out[idx]=i-idx
        stack.append(i)
    return out
    
nums=[73,74,75,71,69,72,76,73]
print(mono(nums))