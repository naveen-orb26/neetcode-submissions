class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upperbound = max(piles)
        lowerbound = 1
        ans = upperbound
        
        while lowerbound<=upperbound:
            mid = lowerbound + (upperbound-lowerbound)//2
            totalhrs = sum((i+mid-1)//mid for i in piles)
            if totalhrs<=h:
                ans = mid
                upperbound = mid-1
            else:
                lowerbound = mid+1

        
        return ans


