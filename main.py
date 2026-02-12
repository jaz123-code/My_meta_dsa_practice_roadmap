def sub(a,k):
    prefixSum=0
    maxL=0
    hashMap={0: -1}
    for i in range(len(a)):
        prefixSum+=a[i]
        if prefixSum-k in hashMap:
            length=i-hashMap[prefixSum -k]
            maxL=max(maxL, length)
        if prefixSum not in hashMap:
            hashMap[prefixSum]=i
    return maxL
a=[1,2,3,4,5]
k=4
print(sub(a,k))