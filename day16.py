import math

def minEatingSpeed(piles, h):
    # The result we want to minimize is the speed 'k'
    ans = max(piles) 
    
    def canEat(piles, k):
        hours = 0
        for pile in piles:
            # Ceiling division: how many hours for this pile at speed k
            hours += (pile + k - 1) // k
        return hours
    
    l = 1
    r = max(piles)
    
    while l <= r:
        mid = (l + r) // 2
        
        # If mid is 0, we'd get a division error, 
        # but since l=1, mid will be at least 1.
        if canEat(piles, mid) <= h:
            ans = mid      # This speed works! Try to find a smaller one.
            r = mid - 1
        else:
            l = mid + 1    # Too slow, need to eat faster.
            
    return ans

piles = [3, 6, 7, 11]
print(minEatingSpeed(piles, 8)) # Output: 4

