class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        large = 0
        numset = set(nums)
        for num in numset:
            if (num-1) not in numset:
                currentnum = num
                currentstreak=1
                while (currentnum+1) in numset:
                    currentstreak+=1
                    currentnum +=1
                large = max(large,currentstreak)
        return large